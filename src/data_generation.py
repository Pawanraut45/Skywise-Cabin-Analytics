import pandas as pd
import numpy as np
from datetime import datetime, timedelta


np.random.seed(42)


records = 5000
aircraft_ids = [f"A320_{i}" for i in range(1, 21)]
components = ["Seat", "IFE", "Lavatory", "Lighting", "Galley"]
issue_types = ["Electrical", "Mechanical", "Software"]
severities = ["Low", "Medium", "High"]
airports = ["BLR", "DEL", "BOM", "HYD", "MAA"]


start_date = datetime(2023, 1, 1)


data = []

for _ in range(records):
    failure = np.random.choice([0, 1], p=[0.7, 0.3])
    data.append({
        "aircraft_id": np.random.choice(aircraft_ids),
        "flight_date": start_date + timedelta(days=np.random.randint(0, 365)),
        "cabin_component": np.random.choice(components),
        "issue_type": np.random.choice(issue_types),
        "severity": np.random.choice(severities),
        "failure_flag": failure,
        "repair_time_hours": np.random.uniform(0.5, 10) if failure else 0,
        "maintenance_cost_usd": np.random.uniform(100, 5000) if failure else 0,
        "airport_code": np.random.choice(airports)
          })


df = pd.DataFrame(data)
df.to_csv("data/raw/cabin_maintenance_raw.csv", index=False)