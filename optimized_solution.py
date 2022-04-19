import pandas as pd

shares_dataframe1 = pd.read_csv('dataset1_Python+P7.csv')

csv_dataset1 = 'dataset1_Python+P7.csv'

csv_dataset1_real_profit = 'dataset1_Python+P7_real_profit.csv'


def get_real_profit(shares, csv_shares_real_profit):
    real_profit_list = []
    for i in range(len(shares)):
        real_profit = shares.loc[i, 'price'] * (shares.loc[i, 'profit'] / 100)
        real_profit_list.append(real_profit)
    add_column_in_csv(shares, csv_shares_real_profit, real_profit_list)


def add_column_in_csv(input_file, output_file, real_profit_list):
    csv_input = input_file
    csv_input['real profit'] = real_profit_list
    csv_input.to_csv(output_file, index=False)
