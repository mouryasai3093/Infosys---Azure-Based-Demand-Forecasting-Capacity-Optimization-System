import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Azure Demand Forecast Dashboard")

# Load file
df = pd.read_csv("forecast_output.csv")

st.subheader("Actual vs Forecast")

df_sample = df.iloc[:20]

plt.figure(figsize=(8,4))
plt.plot(df_sample['demand_units'], 'o-', label='Actual')
plt.plot(df_sample['forecast'], 's--', label='Forecast')

plt.legend()
plt.xlabel("Time")
plt.ylabel("Demand")
plt.title("Demand Forecast")

st.pyplot(plt)
