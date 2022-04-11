import pandas as pd
from csv import writer
from csv import reader

# from itertools import combinations

# from itertools import permutations

# I want to maximize the profit generated by shares list.
# The maximum amount we can spend in shares is 500 euros.
# We have a backpack problem.

bruteforce_shares = pd.read_csv('bruteforce_shares.csv')

bruteforce_shares_real_profit = pd.read_csv('bruteforce_shares_real_profit.csv')

csv_bruteforce_shares = 'bruteforce_shares.csv'

csv_bruteforce_shares_real_profit = 'bruteforce_shares_real_profit.csv'

"""
The profit of one share is a percentage of its cost.
The real profit of one share is the absolute value of this percentage. For example a share that cost 25 euros and has a
profit of 8% has a real profit of 2 euros because 25 * (8/100) = 2.
"""


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


def get_total_real_profit_of_shares(shares):
    total_real_profit_of_shares = shares['real profit'].sum()
    print(total_real_profit_of_shares)
    return total_real_profit_of_shares


# The get_real_profit function is used to compute the real profit of each share.


def get_real_profit(shares, csv_shares, csv_shares_real_profit):
    real_profit_list = ['real profit', ]
    for i in range(len(shares)):
        real_profit = shares.loc[i, 'price'] * (shares.loc[i, 'profit'] / 100)
        real_profit_list.append(real_profit)
    add_column_in_csv(csv_shares, csv_shares_real_profit, lambda row, line_num: row.append(real_profit_list[line_num - 1
                                                                                                            ]))


# The add_column_in_csv function is used to add a new column to our csv file, and is called in
# get_real_profit function.


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

""" 
Finally I will first, create a global function that return all possible combinations of shares list with a maximum 
total price of 500 euros. Once I get all possible combinations of shares list, I will call a function that will return
the most profitable shares list.
"""

"""
def get_most_profitable_shares_list(dataframes_dict):
    dataframes = list(dataframes_dict.keys())
    for index in range(0, len(dataframes)):
        if dataframes_dict[dataframes[index]] == max(dataframes_dict.values()):
            print("**********************Dataframe************************")
            print("Here is the most profitable shares list: ")
            print(dataframes[index])
            print("Here is the total real profit: ")
            print(str(max(dataframes_dict.values())))
            print("**********************End of Dataframe*****************")
            break
        else:
            print("**********************Dataframe************************")
            print("The following shares list is not the most profitable: ")
            print(dataframes[index])
            print("Here is the total real profit of the above shares list: ")
            print(str(dataframes_dict[dataframes[index]]))
            print("**********************End of Dataframe*****************")
"""


def get_most_profitable_shares_list(dataframes_list):
    maximum_total_price_of_shares = 500
    profitable = []
    for i in range(0, len(dataframes_list)-1):
        total_price_of_shares = get_total_price_of_shares(dataframes_list[i])
        total_real_profit = get_total_real_profit_of_shares(dataframes_list[i])
        while total_price_of_shares <= maximum_total_price_of_shares:
            profitable.append(total_real_profit)
            print("************************Dataframe " + str(i) + "*************************************")
            print(dataframes_list[i])
            print("Here is total price of shares: " + str(total_price_of_shares))
            print("Here is the total real profit of shares: " + str(total_real_profit))
        else:
            if total_real_profit == max(profitable):
                print("************************Dataframe " + str(i) + "*************************************")
                print("Here is the most profitable shares list: ")
                print("Here is total price of shares: " + str(total_price_of_shares))
                print("Here is the total real profit of shares: " + str(total_real_profit))
                break
            else:
                print("An error occurred during the execution of the program.")
                break


def get_500_euros_shares_list(shares):
    maximum_total_price_shares = 500
    # I will first slice my dataframe in smaller dataframe with maximum total price of 500 euros
    sample_dataframe = pd.DataFrame(columns=['name', 'price', 'profit', 'real profit'])
    total_price_of_shares = 0
    i = 0
    while total_price_of_shares <= maximum_total_price_shares:
        sample_dataframe = sample_dataframe.append({'name': shares.at[i, 'name'], 'price': shares.at[i, 'price'],
                                                    'profit': shares.at[i, 'profit'],
                                                    'real profit': shares.at[i, 'real profit']},
                                                   ignore_index=True)
        total_price_of_shares = total_price_of_shares + shares.at[i, 'price']
        i += 1
    else:
        print("You reached the maximum authorized total price cost.")
    print(sample_dataframe)


"""

def get_all_possible_combinations(shares):
    maximum_total_price_shares = 500
    dataframes_dict = {}
    i = 1
    while i <= 20:
        for index in list(combinations(shares.index, i)):
            total_real_profit = get_total_real_profit_of_shares(shares.loc[index, :])
            total_price_of_shares = get_total_price_of_shares(shares.loc[index, :])
            print("***********Dataframe********************************")
            print(shares.loc[index, :])
            print("Here is the total real profit of the above shares list: " + str(total_real_profit))
            print("Here is the total price of shares list: " + str(total_price_of_shares))
            print("***********end of Dataframe**************************")
            if total_price_of_shares <= maximum_total_price_shares:
                dataframes_dict[str(shares.loc[index, :])] = total_real_profit
            else:
                print("***********too**expensive**Dataframe********************************")
                print("The following dataframe is too expensive for our program: ")
                print(shares.loc[index, :])
                print("Here is the total price of shares list: " + str(total_price_of_shares))
                print("Here is the total real profit of the above shares list: " + str(total_real_profit))
                print("***********end**of**too**expensive**Dataframe************************")
                break
        get_most_profitable_shares_list(dataframes_dict)
        i += 1


get_all_possible_combinations(bruteforce_shares_real_profit)

"""


def get_all_possible_combinations(shares):
    combinations = []
    for i in range(2 ** 20):
        combination = str(bin(i)).replace("0b", "")
        dataframe_combination = pd.DataFrame(columns=['name', 'price', 'profit', 'real profit'])
        for j in range(len(combination)):
            if combination[j] == "1":
                dataframe_combination = dataframe_combination.append(
                    {'name': shares.at[j, 'name'], 'price': shares.at[j, 'price'],
                     'profit': shares.at[j, 'profit'],
                     'real profit': shares.at[j, 'real profit']}, ignore_index=True)
            else:
                pass
        print("************************Dataframe " + str(i) + "*************************************")
        print(dataframe_combination)
        print("Here is the binary combination: " + combination)
        combinations.append(dataframe_combination)
    get_most_profitable_shares_list(combinations)


get_all_possible_combinations(bruteforce_shares_real_profit)
