import pandas as pd

shares_dataframe1 = pd.read_csv('dataset1_Python+P7.csv')

csv_dataset1 = 'dataset1_Python+P7.csv'

csv_dataset1_real_profit = 'dataset1_Python+P7_real_profit.csv'

shares_dataframe1_real_profit = pd.read_csv('dataset1_Python+P7_real_profit.csv')


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

# print(shares_dataframe1_real_profit.head(10))

"""
My program should pick shares with highest real profit, store it into a list and the total cost of shares should 
not exceed 500 euros.
"""

average_real_profit = shares_dataframe1_real_profit['real profit'].mean()

# print("Here is the average real profit of our dataset 1: " + str(average_real_profit))
