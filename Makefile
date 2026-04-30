.PHONY: setup run-fixture run-live report clean test

setup:
	pip install -e ".[dev]"

# Full pipeline using committed fixture — no API keys needed for discovery/enrichment
run-fixture:
	outrich run --source fixture

# Full pipeline using live Apify — requires APIFY_TOKEN
run-live:
	outrich run --source apify

# Regenerate report from existing DB
report:
	outrich report

# Force fresh API calls (ignores cache)
run-fresh:
	outrich run --source apify --no-cache

clean:
	rm -f data/outrich.db data/sample_run/report.md

test:
	pytest tests/ -v
