import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pydeck as pdk

# Load Data
data = pd.read_csv("main_data.csv") 

# Title
st.title("Air Quality Dashboard")

# Sidebar
st.sidebar.header("Project by Louis Widi Anandaputra\nFilter Data")
year = st.sidebar.selectbox("Select Year", data['year'].unique())
month = st.sidebar.selectbox("Select Month", data['month'].unique())
parameter = st.sidebar.selectbox("Select Parameter", ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3'])
selected_stations = st.sidebar.multiselect("Select Stations", data['station'].unique())

# Filter data
filtered_data = data[(data['year'] == year) & (data['month'] == month) & (data['station'].isin(selected_stations))]

# Time Series Analysis
st.header("Time Series Analysis")
st.write("Time Series Analysis for Air Quality Parameters")
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(x='hour', y=parameter, data=filtered_data, ax=ax)
st.pyplot(fig)

# Air Quality Metrics
st.header("Air Quality Metrics")
st.write("Select an air quality parameter to view its chart:")
selected_param = st.selectbox("Parameter", ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3'])
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(x='hour', y=selected_param, data=filtered_data, ax=ax)
st.pyplot(fig)

# Temperature and Pressure
st.header("Temperature and Pressure Analysis")
fig, ax = plt.subplots(2,figsize=(10, 5))
sns.lineplot(x='hour', y='TEMP', data=filtered_data, ax=ax[0], label="Temperature")
sns.lineplot(x='hour', y='PRES', data=filtered_data, ax=ax[1], label="Pressure")
st.pyplot(fig)

# Dew Point and Rain
st.header("Dew Point and Rain Analysis")
fig, ax = plt.subplots(2,figsize=(10, 5))
sns.lineplot(x='hour', y='DEWP', data=filtered_data, ax=ax[0], label="Dew Point")
sns.lineplot(x='hour', y='RAIN', data=filtered_data, ax=ax[1], label="Rain")
st.pyplot(fig)

# Wind Information
st.header("Wind Information Analysis")
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(x='hour', y='WSPM', data=filtered_data, ax=ax, label="Wind Speed")
st.pyplot(fig)

# Acquire Information about SO2, NO2, CO, and O3 levels
st.header("Acquire Information about SO2, NO2, CO, and O3 Levels")
parameter_to_acquire = st.selectbox("Select Parameter", ['SO2', 'NO2', 'CO', 'O3'])
st.subheader(f"Information about {parameter_to_acquire} levels:")
if parameter_to_acquire in data.columns:
    st.write(f"Mean {parameter_to_acquire} Level: {filtered_data[parameter_to_acquire].mean()}")
    st.write(f"Median {parameter_to_acquire} Level: {filtered_data[parameter_to_acquire].median()}")
    st.write(f"Standard Deviation of {parameter_to_acquire} Levels: {filtered_data[parameter_to_acquire].std()}")

# Export data (optional)
if st.button("Export Data"):
    filtered_data.to_csv(f"{parameter}_data.csv", index=False)

# Footer
st.text("Louis Widi Anandaputra - 2023")
