import requests
import os

# Create folder if not exists
os.makedirs("data\\raw", exist_ok=True)

# 6 key mutual fund schemes
SCHEMES = {
    "HDFC_Top100":     125497,
    "SBI_Bluechip":    119551,
    "ICICI_Bluechip":  120503,
    "Nippon_LargeCap": 118632,
    "Axis_Bluechip":   119092,
    "Kotak_Bluechip":  120841,
}

print("Fetching live NAV from mfapi.in...\n")

for name, code in SCHEMES.items():
    try:
        url = f"https://api.mfapi.in/mf/{code}"
        print(f"Fetching {name} (code: {code})...")
        
        r = requests.get(url, timeout=15)
        data = r.json()
        
        scheme_name = data["meta"]["scheme_name"]
        nav_data = data["data"]
        
        # Save as CSV
        filename = f"data\\raw\\nav_{name}.csv"
        with open(filename, "w") as f:
            f.write("date,nav,scheme_name\n")
            for row in nav_data:
                f.write(f"{row['date']},{row['nav']},{scheme_name}\n")
        
        # Print latest NAV
        latest = nav_data[0]
        print(f"  ✓ Scheme: {scheme_name}")
        print(f"  ✓ Latest NAV: {latest['nav']} on {latest['date']}")
        print(f"  ✓ Total records: {len(nav_data)}")
        print(f"  ✓ Saved to: {filename}\n")

    except Exception as e:
        print(f"  ✗ Failed {name}: {e}\n")

print("✓ All NAV data fetched and saved!")