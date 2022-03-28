import pandas as pd

# I want to maximize the profit generated by shares list.
# The maximum amount we can spend in shares is 500 euros.
# We have a backpack problem.

bruteforce_shares = pd.read_csv('bruteforce_shares.csv')

# print(bruteforce_shares.iloc[0])

# print(bruteforce_shares.at[0, 'name'])

# print(bruteforce_shares.at[3, 'price'])

# print(bruteforce_shares.at[6, 'profit'])


def get_price_of_share(shares, index):
    return shares.at[index, 'price']


def get_profit_of_share(shares, index):
    return shares.at[index, 'profit']
