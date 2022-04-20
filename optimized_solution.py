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


def get_most_profitable_shares_list(shares):
    # Computing a minimum real profit in order to get the 10% most profitable shares of the dataset.
    minimum_real_profit_amount = shares['real profit'].quantile(0.9)
    maximum_total_price_shares = 500
    total_real_profit_of_shares = get_total_real_profit_of_shares(shares)
    # From the dataframe of the dataset I will create a smaller dataframe that respect the requirements of customers.
    most_profitable_shares_list = pd.DataFrame(columns=['name', 'price', 'profit', 'real profit'])
    total_price_of_shares = 0
    i = 0
    real_profit_of_shares = get_real_profit_of_share(shares, i)
    while total_price_of_shares <= maximum_total_price_shares and real_profit_of_shares >= minimum_real_profit_amount:
        most_profitable_shares_list = most_profitable_shares_list.append({'name': shares.at[i, 'name'],
                                                                          'price': shares.at[i, 'price'],
                                                                          'profit': shares.at[i, 'profit'],
                                                                          'real profit': shares.at[
                                                                              i, 'real profit']},
                                                                         ignore_index=True)
        total_price_of_shares = total_price_of_shares + shares.at[i, 'price']
        i += 1
    else:
        print("You reached the maximum authorized total price cost.")
    print("Here is the most profitable shares list: ")
    print(most_profitable_shares_list)
    print("Here is the total price of shares: " + str(total_price_of_shares) + " euros")
    print("Here is the total real profit of shares: " + str(total_real_profit_of_shares) + " euros")
    print("Every shares are among the 10% most profitable shares of the global dataset. "
          "Every shares has a real profit higher or equal"
          "to the following amount: " + str(minimum_real_profit_amount) + " euros")
    return most_profitable_shares_list, total_price_of_shares, total_real_profit_of_shares, minimum_real_profit_amount
