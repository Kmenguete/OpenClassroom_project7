import pandas as pd
import seaborn as sns

# import plotly.express as px


color = sns.color_palette()
shares_dataframe2 = pd.read_csv('dataset2_Python+P7.csv')


# fig = px.scatter(shares_dataframe2, x='price', y='profit')
# fig.update_traces(marker_color="rgb(100,0,149)", marker_line_color="rgb(215,193,80)", marker_line_width=1.5)
# fig.update_layout(title_text='relationship between cost and profitability for dataset2')
# fig.show()


def remove_outliers(shares):
    shares.drop([shares.loc[shares['price'] < 0]])
    print(shares.to_string())


remove_outliers(shares_dataframe2)
