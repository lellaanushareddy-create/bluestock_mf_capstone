import os
import pandas as pd

# ----------------------------
# Path Configuration
# ----------------------------
RAW = os.path.join("data", "raw")

print("\nFiles found in data/raw:\n")

# Check if folder exists
if not os.path.exists(RAW):
    print(f"ERROR: Folder not found -> {RAW}")
    exit()

# List all contents
all_items = os.listdir(RAW)

for item in all_items:
    item_path = os.path.join(RAW, item)

    if os.path.isdir(item_path):
        print(f"[DIR]  {item}")
    else:
        print(f"[FILE] {item}")

print("\nNow reading CSV files...\n")

# ----------------------------
# Read CSV Files Only
# ----------------------------
csv_files = [
    f for f in all_items
    if os.path.isfile(os.path.join(RAW, f))
    and f.lower().endswith(".csv")
]

if len(csv_files) == 0:
    print("No CSV files found in data/raw")

for filename in csv_files:

    filepath = os.path.join(RAW, filename)

    try:
        df = pd.read_csv(filepath)

        print("\n" + "=" * 60)
        print(f"FILE: {filename}")
        print("=" * 60)

        print(f"Shape (rows x cols): {df.shape}")

        print("\nColumns:")
        print(list(df.columns))

        print("\nFirst 3 rows:")
        print(df.head(3))

        print("\nData Types:")
        print(df.dtypes)

        print("\nMissing Values:")
        print(df.isnull().sum())

    except Exception as e:
        print(f"\nERROR reading {filename}")
        print(e)

print("\n✓ Data ingestion complete!")