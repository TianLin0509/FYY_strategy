path = 'D:/April_data/csv/'
import pandas as pd
def look_up(code, date):
    code_path = path + code + '.csv'
    a = pd.read_csv(code_path)
    today = a[a['date']==date]
    if len(today) == 0:
        return [0]
    index = int(today.index.values)
    today = today.iloc[0]
    yesterday_close = a.iloc[index-1].close
    last_close = a.iloc[index-2].close
    ztopen = 1 if today.open == round(yesterday_close * 1.1 + 0.0001, 2) else 0
    ztclose = 1 if today.close == round(yesterday_close * 1.1 + 0.0001, 2) else 0
    ztyz = 1 if today.high == today.low and ztopen else 0
    shouban = 1 if yesterday_close < round(last_close * 1.1 + 0.0001, 2) else 0
    tomorrow = a.iloc[index+1]
    tomorrow_open = round((tomorrow.open - today.open) / today.open * 100, 2)
    tomorrow_high = round((tomorrow.high - today.open) / today.open * 100, 2)
    return ztopen, ztclose, ztyz, shouban, tomorrow_open, tomorrow_high
    pass
