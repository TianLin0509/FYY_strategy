import pandas as pd

M = pd.read_csv('result.csv')
M.to_csv('result2.csv', index=0, encoding='gbk')