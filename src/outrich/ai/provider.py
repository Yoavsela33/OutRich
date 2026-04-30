import json
import logging
from typing import Type, TypeVar

import anthropic
import instructor
from google import genai
from google.genai import types as genai_types
from pydantic import BaseModel

from outrich.config import Settings

logger = logging.getLogger(__name__)

T = TypeVar("T", bound=BaseModel)


class AIProvider:
    """Claude-primary, Gemini-fallback structured-output provider."""

    def __init__(self, settings: Settings) -> None:
        self._settings = settings
        self._claude: instructor.Instructor | None = None
        self._gemini: genai.Client | None = None

        if settings.anthropic_api_key:
            self._claude = instructor.from_anthropic(
                anthropic.Anthropic(api_key=settings.anthropic_api_key)
            )

        if settings.gemini_api_key:
            self._gemini = genai.Client(api_key=settings.gemini_api_key)

        if not self._claude and not self._gemini:
            raise ValueError(
                "At least one of ANTHROPIC_API_KEY or GEMINI_API_KEY must be set."
            )

    def complete(
        self,
        response_model: Type[T],
        system: str,
        user: str,
        max_tokens: int = 2048,
    ) -> tuple[T, str]:
        """Return (parsed_result, model_name). Tries Claude first, falls back to Gemini."""
        if self._claude:
            try:
                result = self._claude.messages.create(
                    model=self._settings.claude_model,
                    max_tokens=max_tokens,
                    system=system,
                    messages=[{"role": "user", "content": user}],
                    response_model=response_model,
                )
                return result, self._settings.claude_model
            except Exception as exc:
                if not self._gemini:
                    raise
                logger.warning(
                    "Claude failed (%s: %s) — falling back to Gemini",
                    type(exc).__name__,
                    exc,
                )

        # Gemini path — google.genai SDK with JSON mode + pydantic validation
        prompt = f"System Instructions:\n{system}\n\nUser:\n{user}"
        response = self._gemini.models.generate_content(  # type: ignore[union-attr]
            model=self._settings.gemini_model,
            contents=prompt,
            config=genai_types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=response_model,
            ),
        )
        return response_model.model_validate_json(response.text), self._settings.gemini_model
