import pandas as pd
import pandas_profiling as pp
import seaborn as sns

import plotly.express as px


color = sns.color_palette()
shares_dataframe1 = pd.read_csv('dataset1_Python+P7.csv')
shares_dataframe2 = pd.read_csv('dataset2.csv')

# The total number of algorithms required to clean dataset is not comprehensive. As new datasets will be used for
# optimized solution and bruteforce algorithm, I may add new functions according future operations that may need to
# be maid on future datasets in order to clean and analyze them.


def remove_outliers(shares):
    clean_dataframe = pd.DataFrame(columns=['name', 'price', 'profit'])
    for i in range(0, len(shares)):
        price_of_share = shares.at[i, 'price']
        if price_of_share >= 0:
            clean_dataframe = clean_dataframe.append({'name': shares.at[i, 'name'], 'price': shares.at[i, 'price'],
                                                      'profit': shares.at[i, 'profit']}, ignore_index=True)
        else:
            print("The price of this share does not make sense: " + str(price_of_share))
    clean_dataframe.to_csv('dataset2.csv', index=False)
    print(clean_dataframe.to_string())


def generate_dataframe_report(shares, output_file):
    shares_report = pp.ProfileReport(shares)
    print(shares_report.to_file(output_file=output_file))
    return shares_report


def visualize_shares(shares):
    figure = px.scatter(shares, x='price', y='profit')
    figure.update_traces(marker_color="rgb(100,0,149)", marker_line_color="rgb(215,193,80)", marker_line_width=1.5)
    figure.update_layout(title_text='relationship between cost and profitability for dataset2')
    figure.show()
    return figure
