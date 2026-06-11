import pandas as pd

risk = input(
    "Enter Risk (Low/Moderate/High): "
)

df = pd.read_csv(
    "data/processed/scheme_performance_clean.csv"
)

filtered = df[
    df["risk_grade"]
    .str.contains(
        risk,
        case=False,
        na=False
    )
]

top3 = filtered.sort_values(
    "sharpe_ratio",
    ascending=False
).head(3)

print(
    top3[
        [
            "scheme_name",
            "risk_grade",
            "sharpe_ratio"
        ]
    ]
)
