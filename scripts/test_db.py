import sqlite3

DB_PATH = "data\\db\\bluestock_mf.db"
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

print("Testing database queries...\n")

# Query 1
print("Total funds:")
result = cursor.execute("SELECT COUNT(*) FROM fund_master").fetchone()
print(f"  {result[0]} funds\n")

# Query 2
print("Fund houses:")
result = cursor.execute("SELECT DISTINCT fund_house FROM fund_master").fetchall()
for row in result:
    print(f"  - {row[0]}")

# Query 3
print("\nLatest 5 NAV records:")
result = cursor.execute("""
    SELECT scheme_name, date, nav 
    FROM nav_history 
    ORDER BY date DESC 
    LIMIT 5
""").fetchall()
for row in result:
    print(f"  {row[0]} | {row[1]} | {row[2]}")

conn.close()
print("\n✓ Database verified successfully!")