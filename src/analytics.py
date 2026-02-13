import pandas as pd


df = pd.read_parquet("data/processed/cabin_maintenance_clean.parquet")


kpi = df.groupby("cabin_component").agg({
"failure_flag": "mean",
"maintenance_cost_usd": "mean"
}).reset_index()


print(kpi)