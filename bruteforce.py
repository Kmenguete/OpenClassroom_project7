import pandas as pd
# import pandas_profiling as pp

# Visualization Imports
# import seaborn as sn
# import plotly.express as px


shares_dataframe1 = pd.read_csv('dataset1_Python+P7.csv')

# I am generating a pandas profiling report
# shares_dataframe1_report = pp.ProfileReport(shares_dataframe1)

# I am creating a data visualization in order to know if a correlation exist between the cost of a share
# and its profitability
# color = sn.color_palette()

# figure = px.scatter(shares_dataframe1, x='profit', y='price')
# figure.update_traces(marker_color="rgb(158,11,200)", marker_line_color="rgb(15,179,104)", marker_line_width=1.5)
# figure.update_layout(title_text='Is there a positive correlation between the cost of a share and its profitability?')
# relationship_cost_profitability = figure.show()

# print(relationship_cost_profitability)

# print(shares_dataframe1_report.to_file('dataframe1_report'))

# results of my dataset analysis: There is not any relationship between cost of shares and their profitability.
# Finding the list of most profitable shares is a lottery.


def get_most_profitable_shares_list(shares_list):
    return shares_list
