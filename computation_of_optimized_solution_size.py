import pandas as pd
import sys


shares_dataframe1 = pd.read_csv('dataset1_Python+P7.csv')

shares_dataframe2 = pd.read_csv('dataset2.csv')

csv_dataset1 = 'dataset1_Python+P7.csv'

csv_dataset2 = 'dataset2.csv'

csv_dataset2_real_profit = 'dataset2_real_profit.csv'

csv_dataset1_real_profit = 'dataset1_Python+P7_real_profit.csv'

shares_dataframe1_real_profit = pd.read_csv('dataset1_Python+P7_real_profit.csv')

shares_dataframe2_real_profit = pd.read_csv('dataset2_real_profit.csv')

shares_dataframe1_size = sys.getsizeof(shares_dataframe1)

shares_dataframe2_size = sys.getsizeof(shares_dataframe2)

csv_dataset1_size = sys.getsizeof(csv_dataset1)

csv_dataset2_size = sys.getsizeof(csv_dataset2)

csv_dataset2_real_profit_size = sys.getsizeof(csv_dataset2_real_profit)

csv_dataset1_real_profit_size = sys.getsizeof(csv_dataset1_real_profit)

shares_dataframe1_real_profit_size = sys.getsizeof(shares_dataframe1_real_profit)

shares_dataframe2_real_profit_size = sys.getsizeof(shares_dataframe2_real_profit)

print("Here is the size of shares_dataframe1 variable in memory: " + str(shares_dataframe1_size) + " bytes")

print("Here is the size of shares_dataframe2 variable in memory: " + str(shares_dataframe2_size) + " bytes")

print("Here is the size of csv_dataset1 variable in memory: " + str(csv_dataset1_size) + " bytes")

print("Here is the size of csv_dataset2 variable in memory: " + str(csv_dataset2_size) + " bytes")

print("Here is the size of shares_dataframe1_real_profit in memory: " + str(shares_dataframe1_real_profit_size) +
      " bytes")

print("Here is the size of shares_dataframe2_real_profit in memory: " + str(shares_dataframe2_real_profit_size) +
      " bytes")

print("Here is the size of csv_dataset1_real_profit variable in memory: " + str(csv_dataset1_real_profit_size) +
      " bytes")

print("Here is the size of csv_dataset2_real_profit variable in memory: " + str(csv_dataset2_real_profit_size) +
      " bytes")

one_share_in_dataframe = shares_dataframe1.iloc[0]

one_share_in_dataframe_real_profit = shares_dataframe1_real_profit.iloc[0]

size_one_share_in_dataframe = sys.getsizeof(one_share_in_dataframe)

size_one_share_in_dataframe_real_profit = sys.getsizeof(one_share_in_dataframe_real_profit)

print("Here is the size of one share in dataframe: " + str(size_one_share_in_dataframe) + " bytes")

print("Here is the size of one share in dataframe with real profit data: " +
      str(size_one_share_in_dataframe_real_profit) + " bytes")
