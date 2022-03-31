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

# Trying to get all possible combinations of shares list
"""
n = len(bruteforce_shares_real_profit)
n_integers = [i for i in range(2**n)]

binaries_n = [bin(i)[2:] for i in n_integers]

combinations = ['0'*(n-len(k)) + k for k in binaries_n]
"""
"""
def get_valid_combinations():
    max_cost = 500
    valid_combinations = []
    for combination in combinations:
        cost_combination = 0
        real_profit_combination = 0
        for i in range(n):
            if combination[i] == '1':
                cost_combination = cost_combination + bruteforce_shares_real_profit.at[i, 'price']
                real_profit_combination = real_profit_combination + bruteforce_shares_real_profit.at[i, 'real profit']
        if cost_combination <= max_cost:
            valid_combinations.append((combination, real_profit_combination))
        else:
            pass
"""

""" 
Finally I will first, create a global function that return all possible combinations of shares list with a maximum 
total price of 500 euros. Once I get all possible combinations of shares list, I will call a function that will return
the most profitable shares list.
"""


def get_most_profitable_shares_list():
    pass


def get_all_possible_combination(shares):
    maximum_total_price_shares = 500
    # I will first slice my dataframe in smaller dataframe with maximum total price of 500 euros
    sample_dataframe = pd.DataFrame(columns=['name', 'price', 'profit', 'real profit'])
    total_price_of_shares = 0
    i = 0
    while total_price_of_shares <= maximum_total_price_shares:
        print(shares.iloc[i])
        sample_dataframe = sample_dataframe.append({'name': shares.at[i, 'name'], 'price': shares.at[i, 'price'],
                                                    'profit': shares.at[i, 'profit'],
                                                    'real profit': shares.at[i, 'real profit']},
                                                   ignore_index=True)
        total_price_of_shares = total_price_of_shares + shares.at[i, 'price']
        i += 1
    else:
        print("You reached the maximum authorized total price cost.")
    print(sample_dataframe)


get_all_possible_combination(bruteforce_shares_real_profit)
