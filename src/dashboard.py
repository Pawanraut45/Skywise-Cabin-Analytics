import streamlit as st
import pandas as pd
import plotly.express as px


df = pd.read_parquet("data/processed/cabin_maintenance_clean.parquet")


st.title("Skywise Cabin Analytics Dashboard")


fig = px.bar(df, x="cabin_component", y="maintenance_cost_usd",
color="severity", title="Maintenance Cost by Cabin Component")


st.plotly_chart(fig)