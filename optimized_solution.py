import pandas as pd

shares_dataframe1 = pd.read_csv('dataset1_Python+P7.csv')

csv_dataset1 = 'dataset1_Python+P7.csv'


def get_real_profit(shares, csv_shares):
    real_profit_list = ['real profit', ]
    for i in range(len(shares)):
        real_profit = shares.loc[i, 'price'] * (shares.loc[i, 'profit'] / 100)
        real_profit_list.append(real_profit)
    add_column_in_csv(csv_shares)


def add_column_in_csv(csv_file):
    return csv_file


get_real_profit(shares_dataframe1, csv_dataset1)
