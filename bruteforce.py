import pandas as pd
import pandas_profiling as pp

shares_dataframe1 = pd.read_csv('dataset1_Python+P7.csv')

shares_dataframe1_top = shares_dataframe1.head(5)

shares_dataframe1_report = pp.ProfileReport(shares_dataframe1)

print(shares_dataframe1_report.to_file('dataframe1_report'))
