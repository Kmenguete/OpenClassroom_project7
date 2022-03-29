import pandas as pd
from csv import writer
from csv import reader

# I want to maximize the profit generated by shares list.
# The maximum amount we can spend in shares is 500 euros.
# We have a backpack problem.

bruteforce_shares = pd.read_csv('bruteforce_shares.csv')


# print(bruteforce_shares.iloc[0])

# print(bruteforce_shares.at[0, 'name'])

# print(bruteforce_shares.at[3, 'price'])

# print(bruteforce_shares.at[6, 'profit'])


def get_price_of_share(shares, index):
    print(shares.at[index, 'price'])
    return shares.at[index, 'price']


def get_profit_of_share(shares, index):
    print(shares.at[index, 'profit'])
    return shares.at[index, 'profit']


def get_total_price_of_shares(shares):
    total_price_of_shares = shares['price'].sum()
    print(total_price_of_shares)
    return total_price_of_shares


def get_total_profit_of_shares(shares):
    total_profit_of_shares = shares['profit'].sum()
    print(total_profit_of_shares)
    return total_profit_of_shares


def get_real_profit(shares):
    for i in range(len(shares)):
        real_profit = shares.loc[i, 'price'] * (shares.loc[i, 'profit'] / 100)
        print("The real profit of share: " + str(shares.loc[i, 'name']) + " is " + str(real_profit))


def add_column_in_csv(input_file, output_file, transform_row):
    """
    Append a column in existing csv using csv.reader / csv.writer classes
    """
    # Open the input_file in read mode and output_file in write mode
    with open(input_file, 'r') as read_object, \
            open(output_file, 'w', newline='') as write_object:
        csv_reader = reader(read_object)
        csv_writer = writer(write_object)
        for row in csv_reader:
            transform_row(row, csv_reader.line_num)
            csv_writer.writerow(row)
