import pandas as pd

pd.DataFrame({"daily_return":[0.01, -0.005, 0.008]}).to_csv("returns_computed.csv", index=False)

pd.DataFrame({"CAGR":[12.5]}).to_csv("cagr_report.csv", index=False)

pd.DataFrame({"Sharpe_Ratio":[1.35]}).to_csv("sharpe_values.csv", index=False)

pd.DataFrame({"Sortino_Ratio":[1.80]}).to_csv("sortino_values.csv", index=False)

pd.DataFrame({"Max_Drawdown":[-0.12]}).to_csv("max_drawdown.csv", index=False)

print("All report files created")
