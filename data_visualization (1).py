import matplotlib.pyplot as plt
import pandas as pd

# Create a DataFrame from the data
df = pd.read_csv("2019-20-enforcement-data-food-standards.csv")

# 1. Line Plot with Multiple Lines
def create_line_plot(dataframe, x_col, y_cols, labels, title):
    plt.figure(figsize=(10, 5))
    for i, y_col in enumerate(y_cols):
        plt.plot(dataframe[x_col], dataframe[y_col], label=labels[i])
    plt.xlabel(x_col)
    plt.ylabel('Values')
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()

# Create a line plot with multiple lines
create_line_plot(df, 'Country', ['Totalnumberofestablishments(includingnotyetratedandoutside)(1)',
                                'Numberofestablishmentsnotyetratedforintervention(1)',
                                'TotalnumberofestablishmentssubjecttoWrittenwarnings'],
                 ['Total Establishments', 'Not Yet Rated Establishments', 'Written Warnings'],
                 'Establishment Data Over Time')

# 2. Scatter Plot
def create_scatter_plot(dataframe, x_col, y_col, labels, title):
    plt.figure(figsize=(10, 5))
    plt.scatter(dataframe[x_col], dataframe[y_col])
    plt.xlabel(labels[0])
    plt.ylabel(labels[1])
    plt.title(title)
    plt.grid(True)
    plt.show()

# Create a scatter plot
create_scatter_plot(df, 'Totalnumberofestablishments(includingnotyetratedandoutside)(1)',
                   'TotalnumberofestablishmentssubjecttoWrittenwarnings',
                   ['Total Number of Establishments','Written Warnings'],
                   'Scatter Plot: Establishments vs. Written Warnings')

# 3. Bar Chart
def create_bar_chart(dataframe, x_col, y_col,labels, title):
    plt.figure(figsize=(10, 5))
    plt.bar(dataframe[x_col], dataframe[y_col])
    plt.xlabel(labels[0])
    plt.ylabel(labels[1])
    plt.title(title)
    plt.grid(axis='y')
    plt.show()

# Create a bar chart
create_bar_chart(df, 'Country', 'ProfessionalFullTimeEquivalentPosts-occupied *',
                 ['Country', 'Full Time Equivalent Posts Occupied'],
                 'Professional Full-Time Equivalent Posts Occupied')

# Show the visualizations
plt.show()
