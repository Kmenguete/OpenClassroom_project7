import csv
import pandas as pd

shares_dataframe1 = pd.read_csv('dataset1_Python+P7.csv')

csv_dataset1 = 'dataset1_Python+P7.csv'

csv_dataset1_real_profit = 'dataset1_Python+P7_real_profit.csv'


def get_real_profit(shares, csv_shares, csv_shares_real_profit):
    real_profit_list = ['real profit', ]
    for i in range(len(shares)):
        real_profit = shares.loc[i, 'price'] * (shares.loc[i, 'profit'] / 100)
        real_profit_list.append(real_profit)
    add_column_in_csv(csv_shares, csv_shares_real_profit)


def add_column_in_csv(input_file, output_file):
    with open(input_file, 'r') as csv_input:
        with open(output_file, 'w') as csv_output:
            writer = csv.writer(csv_output, lineterminator='\n')
            reader = csv.reader(csv_input)
            new_column = []
            row = next(reader)
            row.append('real profit')
            new_column.append(row)
            for row in reader:
                row.append(row[0])
                new_column.append(row)
            writer.writerow(new_column)


get_real_profit(shares_dataframe1, csv_dataset1, csv_dataset1_real_profit)
