import pandas as pd

shares_dataframe1 = pd.read_csv('dataset1_Python+P7.csv')

shares_dataframe1_top = shares_dataframe1.head(5)

print(shares_dataframe1_top)
