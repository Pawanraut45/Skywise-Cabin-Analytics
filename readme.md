# Skywise Cabin Analytics

End-to-end **Python & PySpark data engineering project** simulating an aviation cabin analytics platform inspired by the Skywise ecosystem. The project demonstrates data ingestion, ETL pipelines, analytics, and an interactive dashboard to monitor cabin component reliability and maintenance costs.

---

## 🚀 Project Goals

- Build a realistic engineering analytics pipeline
- Demonstrate Python + PySpark skills
- Perform data modeling and KPI analysis
- Deliver an interactive dashboard for insights

---

## 🧩 Tech Stack

- Python (Pandas, NumPy)
- PySpark
- Streamlit
- Plotly
- Parquet (PyArrow)

---

## 📊 Dataset

Synthetic aviation cabin maintenance dataset with **5000+ records**.

### Features
- Aircraft ID
- Flight date
- Cabin component
- Issue type & severity
- Failure flag
- Repair time
- Maintenance cost
- Airport code

Dataset is generated using `src/data_generation.py`.

---

## 🏗️ Architecture

Raw Data → Python ETL → PySpark Processing → Analytics → Dashboard

---

## 📂 Repository Structure
skywise-cabin-analytics/
│
├── data/
│   ├── raw/
│   │   └── cabin_maintenance_raw.csv
│   ├── processed/
│   │   └── cabin_maintenance_clean.parquet
│
├── src/
│   ├── data_generation.py
│   ├── etl_python.py
│   ├── etl_pyspark.py
│   ├── analytics.py
│   └── dashboard.py
│
├── notebooks/
│   └── exploratory_analysis.ipynb
│
├── pipeline.py
├── requirements.txt
└── README.md
