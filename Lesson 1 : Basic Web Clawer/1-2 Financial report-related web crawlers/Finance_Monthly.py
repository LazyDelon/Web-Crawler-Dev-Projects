# 110.05 營收
import time
import requests
import pandas as pd

from io import StringIO

def Monthly(year, month):
    
    URL = "https://mops.twse.com.tw/nas/t21/sii/t21sc03_"+str(year)+'_'+str(month)+".html"
    
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"
    }
    
    req = requests.get(URL, headers=headers)
    req.encoding='big5'
    
    dfs = pd.read_html(StringIO(req.text), encoding='big5')
    df = pd.concat([df for df in dfs if df.shape[1] <= 11 and df.shape[1] > 5])
    
    if 'levels' in dir(df.columns):
        df.columns = df.columns.get_level_values(1)
    else:
        df = df[list(range(10))]
        column_index = df.index[(df[0] == '公司代號')][0]
        df.columns = df.iloc[column_index]
        
    df['當月營收'] = pd.to_numeric(df['當月營收'], 'coerce')
    df = df[~df['當月營收'].isnull()]
    df = df[df['公司代號'] != '合計']
    
    df = df.set_index(['公司代號', '公司名稱'])
    df.to_csv(str(year) + '_' + str(month) + '.csv', encoding='utf_8_sig')
    df = pd.read_csv(str(year) + '_' + str(month) + '.csv', index_col=['公司代號', '公司名稱'])
    
    time.sleep(20)
    return df

Monthly(110, 5)