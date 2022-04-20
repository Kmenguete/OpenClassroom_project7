import pandas as pd

shares_dataframe1 = pd.read_csv('dataset1_Python+P7.csv')

csv_dataset1 = 'dataset1_Python+P7.csv'

csv_dataset1_real_profit = 'dataset1_Python+P7_real_profit.csv'

shares_dataframe1_real_profit = pd.read_csv('dataset1_Python+P7_real_profit.csv')


def get_real_profit_of_share(shares, index):
    print(shares.at[index, 'real profit'])
    return shares.at[index, 'real profit']


def get_total_price_of_shares(shares):
    total_price_of_shares = shares['price'].sum()
    print(total_price_of_shares)
    return total_price_of_shares


def get_total_real_profit_of_shares(shares):
    total_real_profit_of_shares = shares['real profit'].sum()
    print(total_real_profit_of_shares)
    return total_real_profit_of_shares


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


"""
I envision to build a recommender system for the optimized solution. I will build an algorithm that will recommend
the most profitable shares list for a total maximum cost of shares of 500 euros.
"""

"""
I will build a simple recommender system. My program will recommend a list of most profitable shares for a maximum
total cost of 500 euros.
"""

"""
My program should pick shares with highest real profit, store it into a list and the total cost of shares should 
not exceed 500 euros.
"""


def get_most_profitable_shares(shares):
    # Computing a minimum real profit in order to get the 10% most profitable shares of the dataset.
    minimum_real_profit_amount = shares['real profit'].quantile(0.9)
    # From the dataframe of the dataset I will create a smaller dataframe which contain only the 10% most profitable
    # shares.
    most_profitable_shares_list = pd.DataFrame(columns=['name', 'price', 'profit', 'real profit'])
    for i in range(0, len(shares)):
        real_profit_of_shares = get_real_profit_of_share(shares, i)
        if real_profit_of_shares >= minimum_real_profit_amount:
            most_profitable_shares_list = most_profitable_shares_list.append({'name': shares.at[i, 'name'],
                                                                              'price': shares.at[i, 'price'],
                                                                              'profit': shares.at[i, 'profit'],
                                                                              'real profit': shares.at[
                                                                                  i, 'real profit']},
                                                                             ignore_index=True)
        else:
            print("Looking for a profitable share.............")
    print("Here are the 10 % most profitable shares of the entire dataset: ")
    print(most_profitable_shares_list.to_string())


def get_500_euros_shares_list(shares):
    maximum_total_price_shares = 500
    # I will slice my dataframe in a smaller dataframe with maximum total price of 500 euros
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


get_most_profitable_shares(shares_dataframe1_real_profit)
