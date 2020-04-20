from lookup import *
import pandas as pd
import os
from tqdm import tqdm

# read the days
with open('jizhi_specific.txt') as d:
    m = d.readlines()

path = 'D:/April_data/csv/'
dates = [x[:10] for x in m]
codes = os.listdir(path)
result = []
path2 = 'E:/research_codes/fun/Mar28/dates/'
for date in tqdm(dates):
    s = pd.read_csv(path2 + date + '.csv', converters={'code': str}, index_col=0)
    g = s[(s['open'] > 9.6)]
    codes = [x[1:] for x in g['code']]
    for code in codes:
        tmp = look_up(code, date)
        # 开盘涨停+首板+非一字
        if tmp[0] and tmp[3] and not tmp[2]:
            flag = '回封' if tmp[1] else '未回封'
            result.append(['\t' + code, date, flag, tmp[4], tmp[5]])
M = pd.DataFrame(result)
M.columns = ['代码', '日期', '回封与否', '开盘收益', '最高收益']
M.to_csv('result.csv', index=0, encoding='gbk')
