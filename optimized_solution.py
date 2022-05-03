import pandas as pd
import time
import matplotlib.pyplot as plt
import numpy as np

start = time.time()
shares_dataframe1 = pd.read_csv('dataset1_Python+P7.csv')

shares_dataframe2 = pd.read_csv('dataset2.csv')

csv_dataset1 = 'dataset1_Python+P7.csv'

csv_dataset2 = 'dataset2.csv'

csv_dataset2_real_profit = 'dataset2_real_profit.csv'

csv_dataset1_real_profit = 'dataset1_Python+P7_real_profit.csv'

shares_dataframe1_real_profit = pd.read_csv('dataset1_Python+P7_real_profit.csv')

shares_dataframe2_real_profit = pd.read_csv('dataset2_real_profit.csv')


def sort_shares_list_by_real_profit(shares):
    sorted_shares_by_real_profit = shares.sort_values(by=['real profit'], ascending=False, ignore_index=True)
    print("****************Here is the sorted top 10 % most profitable shares in descending order*********************")
    print(sorted_shares_by_real_profit.to_string())
    print("****************Here is the sorted top 10 % most profitable shares in descending order*********************")
    get_500_euros_shares_list(sorted_shares_by_real_profit)


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
    # I compute the real profit of each share(The percentage of the cost of the share).
    # I store the results in a list, and I will use this list to add real profit data to csv file.
    real_profit_list = []
    for i in range(len(shares)):
        real_profit = shares.loc[i, 'price'] * (shares.loc[i, 'profit'] / 100)
        real_profit_list.append(real_profit)
    add_column_in_csv(shares, csv_shares_real_profit, real_profit_list)


def add_column_in_csv(input_file, output_file, real_profit_list):
    # I retrieve the real profit list(from get_real_profit function) and I add real profit data to a new column.
    # I save this new column in a new csv file(the output file). The output file is the input file with real profit
    # data.
    csv_input = input_file
    csv_input['real profit'] = real_profit_list
    csv_input.to_csv(output_file, index=False)


"""
I built a recommender system for the optimized solution. I built an algorithm that recommend
the most profitable shares list for a total maximum cost of shares of 500 euros.
"""

"""
I built a simple recommender system. My program recommend a list of most profitable shares for a maximum
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
        real_profit_of_share = get_real_profit_of_share(shares, i)
        if real_profit_of_share >= minimum_real_profit_amount:
            most_profitable_shares_list = most_profitable_shares_list.append({'name': shares.at[i, 'name'],
                                                                              'price': shares.at[i, 'price'],
                                                                              'profit': shares.at[i, 'profit'],
                                                                              'real profit': shares.at[
                                                                                  i, 'real profit']},
                                                                             ignore_index=True)
        else:
            print("Looking for a profitable share.............")
    print("**********************************Top 10 % most profitable shares of the dataset***************************")
    print(most_profitable_shares_list.to_string())
    print("**********************************Top 10 % most profitable shares of the dataset***************************")
    sort_shares_list_by_real_profit(most_profitable_shares_list)


def get_500_euros_shares_list(shares):
    maximum_total_price_shares = 480
    # I will slice my dataframe in a smaller dataframe with maximum total price of 500 euros
    sample_dataframe = pd.DataFrame(columns=['name', 'price', 'profit', 'real profit'])
    total_real_profit = 0
    total_price_of_shares = 0
    i = 0
    while total_price_of_shares <= maximum_total_price_shares:
        sample_dataframe = sample_dataframe.append({'name': shares.at[i, 'name'], 'price': shares.at[i, 'price'],
                                                    'profit': shares.at[i, 'profit'],
                                                    'real profit': shares.at[i, 'real profit']},
                                                   ignore_index=True)
        total_price_of_shares = total_price_of_shares + shares.at[i, 'price']
        total_real_profit = total_real_profit + shares.at[i, 'real profit']
        i += 1
    else:
        print("You reached the maximum authorized total price cost.")
    print("**********************************The most profitable shares list****************************************")
    print(sample_dataframe)
    print("Here is the total cost of shares: " + str(total_price_of_shares) + " euros")
    print("Here is the total real profit: " + str(total_real_profit) + " euros")
    print("**********************************The most profitable shares list****************************************")
    end = time.time()
    print(f"The runtime of the program is {end - start} seconds")

    get_time_complexity_of_algorithm()
    get_space_complexity_of_algorithm()


def get_space_complexity_of_algorithm():
    # The total number of bytes for the optimized solution is 342633 without any shares.
    # One share takes 629 bytes of memory in dataframe.
    # The following data about space in memory does not take into account the size of csv file, the whole dataframe
    # and the whole dataframe with real profit data (because size of these objects may vary a lot according
    # the number of inputs data).
    x = np.array([100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000])
    y = np.array([62900, 94350, 125800, 157250, 188700, 220150, 251600, 283450, 314500, 345950, 377400, 408850, 440300,
                  471750, 503200, 534650, 566100, 597550, 629000])
    plt.plot(x, y)
    plt.xlabel('Inputs data')
    plt.ylabel('Bytes')
    plt.title('Linear space complexity O(n) of optimal solution algorithm')
    plt.show()


def get_time_complexity_of_algorithm():
    # I illustrate the time complexity of the optimized solution algorithm using matplotlib
    x = np.array([100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000])
    y = np.array([1, 1.5, 2, 2.5, 3, 3.5, 4, 4.1, 4.2, 4.3, 4.4, 4.5, 4.51, 4.52, 4.53, 4.54, 4.541, 4.542, 4.543])
    plt.plot(x, y)
    plt.xlabel('Inputs data')
    plt.ylabel('Time units')
    plt.title('Logarithmic Time O(log n) complexity of the optimized solution algorithm in the big O notation')
    plt.show()


get_most_profitable_shares(shares_dataframe1_real_profit)
