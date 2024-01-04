import requests
import pandas as pd

def Financia_report(Stock_Number, Financial_Statement):
    
    if Financial_Statement == 'BS':
        URL = "https://mops.twse.com.tw/mops/web/ajax_t164sb03"
        Financial_Statement = "資產負債表";

    elif Financial_Statement == 'IS':
        URL = "https://mops.twse.com.tw/mops/web/ajax_t164sb04"
        Financial_Statement = "綜合損益表";
        
    elif Financial_Statement == 'CF':
        URL = "https://mops.twse.com.tw/mops/web/ajax_t164sb05"
        Financial_Statement = "現金流量表";
        
    elif Financial_Statement == 'SE':
        URL = "https://mops.twse.com.tw/mops/web/ajax_t164sb06"  
        Financial_Statement = "權益變動表";
        
    else:
        print('No Such Report Found!')
    
    Form_Data = {
        'encodeURIComponent': '1',
        'step': '1',
        'firstin': '1',
        'off': '1',
        'queryName': 'co_id',
        'inpuType': 'co_id',
        'TYPEK': 'all',
        'isnew': 'true',
        'co_id': str(Stock_Number),
    }
    
    req = requests.post(URL, Form_Data)
    df = pd.read_html(req.text)[1].fillna("")
    
    df.to_csv(Financial_Statement + '_' + Stock_Number + '.csv', encoding='utf_8_sig')
    df = pd.read_csv(Financial_Statement + '_' + Stock_Number + '.csv')
           
    return df

Financia_report('2330', 'BS')
Financia_report('2330', 'IS')
Financia_report('2330', 'CF')
Financia_report('2330', 'SE')