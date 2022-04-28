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
