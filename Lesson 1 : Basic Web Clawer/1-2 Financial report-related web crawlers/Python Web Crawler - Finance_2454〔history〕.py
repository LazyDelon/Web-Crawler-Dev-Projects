import requests
import pandas as pd
from io import StringIO

sid = '2454'

URL = "https://query1.finance.yahoo.com/v7/finance/download/2454.TW?period1=1585045580&period2=1616581580&interval=1d&events=history&includeAdjustedClose=true"

responce = requests.get(URL)

df = pd.read_csv(StringIO(responce.text), index_col = "Date", parse_dates = ["Date"])

#用to_csv存檔，並命名為 “股票代號.csv”
#用「utf_8_sig」編碼
df.to_csv(sid+".csv", encoding="utf_8_sig")

df.Close.plot(figsize=(12,5))