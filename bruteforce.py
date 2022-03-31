import pandas as pd
from csv import writer
from csv import reader

# I want to maximize the profit generated by shares list.
# The maximum amount we can spend in shares is 500 euros.
# We have a backpack problem.

bruteforce_shares = pd.read_csv('bruteforce_shares.csv')

bruteforce_shares_real_profit = pd.read_csv('bruteforce_shares_real_profit.csv')

csv_bruteforce_shares = 'bruteforce_shares.csv'

csv_bruteforce_shares_real_profit = 'bruteforce_shares_real_profit.csv'


# print(bruteforce_shares.iloc[0])

# print(bruteforce_shares.at[0, 'name'])

# print(bruteforce_shares.at[3, 'price'])

# print(bruteforce_shares.at[6, 'profit'])


def get_price_of_share(shares, index):
    print(shares.at[index, 'price'])
    return shares.at[index, 'price']


def get_real_profit_of_share(shares, index):
    print(shares.at[index, 'real profit'])
    return shares.at[index, 'real profit']


def get_total_price_of_shares(shares):
    total_price_of_shares = shares['price'].sum()
    print(total_price_of_shares)
    return total_price_of_shares


def get_total_profit_of_shares(shares):
    total_profit_of_shares = shares['profit'].sum()
    print(total_profit_of_shares)
    return total_profit_of_shares


def get_real_profit(shares, csv_shares, csv_shares_real_profit):
    real_profit_list = ['real profit', ]
    for i in range(len(shares)):
        real_profit = shares.loc[i, 'price'] * (shares.loc[i, 'profit'] / 100)
        real_profit_list.append(real_profit)
    add_column_in_csv(csv_shares, csv_shares_real_profit, lambda row, line_num: row.append(real_profit_list[line_num - 1
                                                                                                            ]))


def add_column_in_csv(input_file, output_file, transform_row):
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
            transform_row(row, csv_reader.line_num)
            # Write the updated row / list to the output file
            csv_writer.writerow(row)


sorted_shares_by_real_profit = bruteforce_shares_real_profit.sort_values('real profit')


def get_most_profitable_shares(shares_list, max_cost):
    sorted_shares_list = shares_list.sort_values('real profit')
    total_cost = 0
    most_profitable_shares = pd.DataFrame(columns=['name', 'price', 'profit', 'real profit'])
    i = 0
    while i < len(sorted_shares_list) and total_cost < max_cost:
        cost_share = get_price_of_share(sorted_shares_list, i)
        if total_cost + cost_share <= max_cost:
            most_profitable_shares.append({'name': sorted_shares_list.at[i, 'name'],
                                           'price': sorted_shares_list.at[i, 'price'],
                                           'profit': sorted_shares_list.at[i, 'profit'],
                                           'real profit': sorted_shares_list.at[i, 'profit']}, ignore_index=True)
            total_cost = total_cost + cost_share
        else:
            pass
        i = i + 1
    print(most_profitable_shares)
    return most_profitable_shares


get_most_profitable_shares(bruteforce_shares_real_profit, 500)
