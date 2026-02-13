# Skywise Cabin Analytics

End-to-end **Python & PySpark data engineering project** simulating an aviation cabin analytics platform inspired by the Skywise ecosystem. The project demonstrates data ingestion, ETL pipelines, analytics, and an interactive dashboard to monitor cabin component reliability and maintenance costs.

---
## 🎯 Problem Statement

Modern airlines generate large volumes of cabin maintenance and operational data from aircraft components such as seats, in-flight entertainment (IFE), lighting systems, galleys, and lavatories.

**However, this data is often:**
- Disconnected across systems
- Difficult to analyze in real time
- Underutilized for predictive insights

**As a result, airlines face challenges like:**
- Unexpected cabin component failures
- Increased maintenance costs
- Poor passenger experience
- Aircraft operational delays

There is a need for a data-driven analytics platform that can consolidate cabin data, generate insights, and support proactive maintenance decisions.

---

## 💡 Solution

The Skywise Cabin Analytics project simulates an end-to-end aviation analytics platform that transforms raw cabin maintenance data into actionable insights.

Key Solution Components

**1️⃣ Data Generation & Ingestion**
A synthetic dataset with 5000+ records replicates real-world cabin maintenance scenarios.

**2️⃣ ETL & Data Processing**
- Python-based ETL for cleaning and transformation
- PySpark pipeline to simulate scalable data processing

**3️⃣ Data Modeling & Analytics**
- The system computes key performance indicators such as:
- Failure rate by cabin component
- Average maintenance cost
- Severity distribution

**4️⃣ Interactive Dashboard**
A Streamlit dashboard provides visual insights to help engineers and operations teams monitor reliability and trends.

**5️⃣ Automation**
A pipeline runner automates the full workflow from data generation to dashboard launch.

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
## ✅ Impact

This project demonstrates how airlines can:
- Detect reliability issues early
- Optimize maintenance planning
- Reduce operational disruptions
- Improve passenger experience

It showcases a practical implementation of data engineering + analytics for engineering services, aligning with real-world aviation analytics platforms.
---

## 📂 Project Structure

```text
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
├── README.md
└── .gitignore
```




