import pandas as pd
import os
path = 'D:/April_data/'
spath = 'D:/April_data/csv/'
def process(code):
    code_path = path + code + '.txt'
    save_path = spath + code + '.csv'
    with open(code_path) as w:
        g = w.readlines()
    x = [y.split(';') for y in g]
    m = pd.DataFrame(x)
    columns= ['date', 'open', 'high', 'low', 'close', 'vol', 'vol2']
    m.columns = columns
    m.to_csv(save_path,  index=0)

codes = [x[:6] for x in os.listdir(path)]
for code in codes:
    try:
        process(code)
    except Exception:
        print(code)
