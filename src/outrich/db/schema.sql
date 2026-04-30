CREATE TABLE IF NOT EXISTS leads (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    linkedin_url    TEXT    UNIQUE NOT NULL,
    full_name       TEXT    NOT NULL,
    headline        TEXT,
    current_company TEXT,
    current_title   TEXT,
    location        TEXT,
    raw_profile     TEXT,   -- JSON blob of full RawProfile
    source          TEXT    NOT NULL,  -- 'apify_live' | 'fixture'
    discovered_at   TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS qualifications (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    lead_id             INTEGER UNIQUE NOT NULL REFERENCES leads(id) ON DELETE CASCADE,
    segment             TEXT    NOT NULL,
    relevance_score     INTEGER NOT NULL,
    reasoning           TEXT    NOT NULL,
    pain_points         TEXT,   -- JSON array
    scylla_angle        TEXT,
    tech_stack_signals  TEXT,   -- JSON array
    model_used          TEXT    NOT NULL,
    qualified_at        TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS messages (
    id                      INTEGER PRIMARY KEY AUTOINCREMENT,
    lead_id                 INTEGER NOT NULL REFERENCES leads(id) ON DELETE CASCADE,
    channel                 TEXT    NOT NULL,  -- 'linkedin_invite' | 'follow_up_email'
    subject                 TEXT,
    body                    TEXT    NOT NULL,
    personalization_hooks   TEXT,   -- JSON array
    model_used              TEXT    NOT NULL,
    drafted_at              TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(lead_id, channel)
);

CREATE TABLE IF NOT EXISTS send_log (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    message_id      INTEGER NOT NULL REFERENCES messages(id) ON DELETE CASCADE,
    mode            TEXT    NOT NULL,  -- 'dry_run' | 'live'
    status          TEXT    NOT NULL,  -- 'logged' | 'sent' | 'failed'
    triggered_at    TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_qual_segment_score
    ON qualifications(segment, relevance_score DESC);
