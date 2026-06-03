-- Drop tables if they exist
DROP TABLE IF EXISTS fund_master;
DROP TABLE IF EXISTS nav_history;

-- Fund master table
CREATE TABLE fund_master (
    scheme_code     INTEGER PRIMARY KEY,
    scheme_name     TEXT,
    fund_house      TEXT,
    category        TEXT,
    sub_category    TEXT,
    risk_grade      TEXT
);

-- NAV history table
CREATE TABLE nav_history (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    scheme_code INTEGER,
    date        TEXT,
    nav         REAL,
    scheme_name TEXT,
    FOREIGN KEY (scheme_code) REFERENCES fund_master(scheme_code)
);