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
numeric_data = data.select_dtypes(include=['float64', 'int64'])
correlation_matrix = numeric_data.corr()

fig1 = plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Heatmap of Correlation Between Variables')
st.pyplot(fig1)

# Trend of CO Concentration by Station and Year
fig2 = plt.figure(figsize=(10, 5))
sns.lineplot(data, x="year", y="CO", hue="station", marker='o')
plt.title('Trend of CO Concentration by Station and Year')
plt.xlabel('Year')
plt.ylabel('CO Concentration')
plt.legend(title='Station', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
st.pyplot(fig2)
