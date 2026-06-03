import os
import sqlite3
import pandas as pd

# Paths
RAW = "data\\raw"
DB_PATH = "data\\db\\bluestock_mf.db"

# Create db folder
os.makedirs("data\\db", exist_ok=True)

print("Starting ETL Pipeline...\n")

# Connect to SQLite
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()
print(f"✓ Connected to database: {DB_PATH}\n")

# Read schema and create tables
with open("sql\\schema.sql", "r") as f:
    schema = f.read()
cursor.executescript(schema)
conn.commit()
print("✓ Tables created from schema.sql\n")

# Load fund_master CSV
print("Loading fund_master...")
try:
    fm_files = [f for f in os.listdir(RAW) if "fund_master" in f.lower()]
    if fm_files:
        df_fm = pd.read_csv(os.path.join(RAW, fm_files[0]))
        print(f"  Columns found: {list(df_fm.columns)}")
        df_fm.to_sql("fund_master", conn, 
                     if_exists="replace", 
                     index=False)
        print(f"  ✓ Loaded {len(df_fm)} rows into fund_master\n")
    else:
        print("  ✗ fund_master CSV not found\n")
except Exception as e:
    print(f"  ✗ Error: {e}\n")

# Load NAV history CSVs
print("Loading NAV history files...")
nav_files = [f for f in os.listdir(RAW) if f.startswith("nav_")]
all_nav = []

for filename in nav_files:
    try:
        df = pd.read_csv(os.path.join(RAW, filename))
        all_nav.append(df)
        print(f"  ✓ Loaded {filename} — {len(df)} rows")
    except Exception as e:
        print(f"  ✗ Error reading {filename}: {e}")

if all_nav:
    df_nav = pd.concat(all_nav, ignore_index=True)
    df_nav.to_sql("nav_history", conn,
                  if_exists="replace",
                  index=False)
    print(f"\n  ✓ Total NAV rows loaded: {len(df_nav)}\n")

# Verify data
print("Verifying database...\n")
tables = ["fund_master", "nav_history"]
for table in tables:
    try:
        count = cursor.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
        print(f"  ✓ {table}: {count} rows")
    except Exception as e:
        print(f"  ✗ {table}: {e}")

conn.close()
print("\n✓ ETL Pipeline complete!")
print(f"✓ Database saved at: {DB_PATH}")