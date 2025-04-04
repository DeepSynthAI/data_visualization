import pandas as pd
from visualization_functions import plot_line_chart, plot_bar_chart

# Load the dataset
df = pd.read_csv("dataset.csv")

# Plot line chart: Sales over Date
plot_line_chart(df, 'Date', 'Sales')

# Plot bar chart: Total Sales by Region
plot_bar_chart(df, 'Region', 'Sales')
