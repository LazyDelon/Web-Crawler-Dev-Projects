import requests
import pandas as pd

from io import StringIO
from datetime import date

#今天日期
Today = date.today().strftime('%Y-%m-%d')

URL = "https://www.twse.com.tw/fund/BFI82U?response=html&dayDate=&weekDate=&monthDate=&type=day"

headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"
}

req = requests.get(URL, headers=headers)
req.encoding='big5'
    
dfs= pd.read_html(URL.format())
dfs[0].columns = dfs[0].columns.droplevel()

New_dfs = dfs[0]
New_dfs['Date'] = Today
New_dfs['Date'] = pd.to_datetime(New_dfs['Date'])

New_csv = New_dfs
New_csv.to_csv('Institutional Investors_Price.csv', encoding='utf_8_sig')
New_csv = pd.read_csv('Institutional Investors_Price.csv')

#印出
New_dfs