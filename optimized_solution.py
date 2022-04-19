import pandas as pd
from csv import writer
from csv import reader

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
    """
    Append a column in existing csv using csv.reader / csv.writer classes
    """
    # Open the input_file in read mode and output_file in write mode
    with open(input_file, 'r') as read_object, \
            open(output_file, 'w', newline='') as write_object:
        # Create a csv.reader object from the input file object
        csv_reader = reader(read_object)
        # Create a csv.writer object from the output file object
        csv_writer = writer(write_object)
        # Read each row of the input csv file as list
        for row in csv_reader:
            # Pass the list / row in the transform function to add column text for this row
            # transform_row(row, csv_reader.line_num)
            # Write the updated row / list to the output file
            csv_writer.writerow(row)


get_real_profit(shares_dataframe1, csv_dataset1, csv_dataset1_real_profit)
