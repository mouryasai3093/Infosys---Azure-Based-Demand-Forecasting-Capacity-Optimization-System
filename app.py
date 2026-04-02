import streamlit as st
import pandas as pd

st.title("Azure Demand Forecast Dashboard")

df = pd.read_csv("forecast_output.csv")

st.subheader("Actual vs Forecast")

df_sample = df.iloc[:20]

st.line_chart(df_sample[['demand_units', 'forecast']])

st.subheader("Key Metrics")
st.write("Total Forecast:", df['forecast'].sum())
st.write("Peak Forecast:", df['forecast'].max())
