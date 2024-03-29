import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='dark')

# Load data
data = pd.read_csv("dashboard/all_data.csv")

# Main title
st.title('Air Quality in China')

# Show the raw data
st.subheader('Raw Data')
st.write(data)

# Sidebar
st.sidebar.title('Arum Puspadewi \n arumpd171@gmail.com')

# Filter station
selected_station = st.sidebar.selectbox('Select Station', data['station'].unique())

# Filter year
selected_year = st.sidebar.slider('Select Year', min_value=int(data['year'].min()), max_value=int(data['year'].max()))

# Filtered data
filtered_data = data[(data['station'] == selected_station) & (data['year'] == selected_year)]

# Show filtered data
st.subheader('Filtered Data')
st.write(filtered_data)

# Heatmap of Correlation Between Variables
correlation_matrix = data[['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3', 'TEMP', 'PRES', 'DEWP', 'RAIN', 'WSPM']].corr()

st.subheader('Heatmap of Correlation Between Variables')
fig1 = plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
st.pyplot(fig1)

# Trend of CO Concentration by Station and Year
st.subheader('Trend of CO Concentration by Station and Year')
fig2, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(data, x="year", y="CO", hue="station", marker='o', linewidth=2)
plt.xlabel('Year')
plt.ylabel('CO Concentration')
plt.legend(title='Station', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
st.pyplot(fig2)
