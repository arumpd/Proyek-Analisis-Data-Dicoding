import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

sns.set(style='dark')

# Load data
@st.cache_data
def load_data():
    data = pd.read_csv("all_data.csv")  # Ganti "nama_file.csv" dengan nama file CSV Anda
    return data

data = load_data()

# Main title
st.title('Air Quality in China')

# Show the raw data
st.subheader('Raw Data')
st.write(data)

# Sidebar
st.sidebar.title('Arum Puspadewi \n arumpd171@gmail.com')

# Filter by station
selected_station = st.sidebar.selectbox('Select Station', data['station'].unique())

# Filter by year
selected_year = st.sidebar.slider('Select Year', min_value=int(data['year'].min()), max_value=int(data['year'].max()))

# Filtered data
filtered_data = data[(data['station'] == selected_station) & (data['year'] == selected_year)]

# Show filtered data
st.subheader('Filtered Data')
st.write(filtered_data)

# Plot scatter plot Ozone vs Temperature
st.subheader('Scatter Plot of Ozone vs Temperature')
fig, ax = plt.subplots()
sns.scatterplot(data=data, x='TEMP', y='O3', ax=ax)
st.pyplot(fig)

# Plot scatter plot Ozone vs Dew Point
st.subheader('Scatter Plot of Ozone vs Dew Point')
fig, ax = plt.subplots()
sns.scatterplot(data=data, x='DEWP', y='O3', ax=ax)
st.pyplot(fig)

# Plot scatter plot Ozone vs Wind Speed
st.subheader('Scatter Plot of Ozone vs Wind Speed')
fig, ax = plt.subplots()
sns.scatterplot(data=data, x='WSPM', y='O3', ax=ax)
st.pyplot(fig)

# Plot line chart of CO concentration by station and year
st.subheader('Trend of CO Concentration by Station and Year')
# Group data by station and year, then calculate mean CO concentration
grouped_data = data.groupby(['station', 'year']).agg({'CO': 'mean'}).reset_index()
# Create line chart for all stations
chart_data = grouped_data.pivot(index='year', columns='station', values='CO')
chart = st.line_chart(chart_data, use_container_width=True)