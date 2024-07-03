import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
data = pd.read_csv("AAPL.csv")

# Clean data (if necessary)
data['Date'] = pd.to_datetime(data['Date'])
data.set_index('Date', inplace=True)
data.sort_index(inplace=True)

# Streamlit app
st.title('AAPL Stock Data Analysis')

# Show the dataset
st.subheader('Raw Data')
st.write(data)

# Show basic statistics
st.subheader('Basic Statistics')
st.write(data.describe())

# Show correlation heatmap
plt.figure(figsize=(12, 10))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
st.pyplot()

# Additional analyses or visualizations can be added here

