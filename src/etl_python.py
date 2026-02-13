import pandas as pd


raw_path = "data/raw/cabin_maintenance_raw.csv"
output_path = "data/processed/cabin_maintenance_clean.parquet"
output_path1 = "data/processed/cabin_maintenance_clean.csv"

df = pd.read_csv(raw_path)
df['flight_date'] = pd.to_datetime(df['flight_date'])
df = df.drop_duplicates()

df.to_parquet(output_path, index=False)
df.to_csv(output_path1, index=False)
