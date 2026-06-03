import pandas as pd

df = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)

returns = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in returns:
    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    )

df["expense_ratio_pct"] = pd.to_numeric(
    df["expense_ratio_pct"],
    errors="coerce"
)

anomalies = df[
    (df["expense_ratio_pct"] < 0.1)
    |
    (df["expense_ratio_pct"] > 2.5)
]

print("Anomalies")
print(anomalies.shape)

df.to_csv(
    "data/processed/scheme_performance_clean.csv",
    index=False
)

print(df.shape)