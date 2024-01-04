file_path = "All.csv"

import pymysql

try:

    conn = pymysql.connect(host='localhost', user='root', password='', db='stock', charset='utf8')
    
    cur = conn.cursor()
    
    print('資料庫連接成功！')
    
except:

    print('資料庫連接失敗！')
    
with open(file_path, 'r', encoding='utf-8-sig') as f:
    reader = f.readline()
    print(reader)
    
import importlib,sys
importlib.reload(sys)
import pandas as pd
 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
DB_CONNECT_STRING = 'mysql+pymysql://root:@localhost/stock?charset=utf8'
engine = create_engine(DB_CONNECT_STRING, echo=True)
DB_Session = sessionmaker(bind=engine)
session = DB_Session()
 
csv_data = pd.read_csv('All.csv', encoding='utf-8')
print(csv_data.shape)
pd.io.sql.to_sql(frame=csv_data, name='All', con=engine, index=False, if_exists='append')

