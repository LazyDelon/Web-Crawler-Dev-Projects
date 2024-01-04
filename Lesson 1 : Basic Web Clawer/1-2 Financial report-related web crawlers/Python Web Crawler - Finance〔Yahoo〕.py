import csv
import requests,datetime
from bs4 import BeautifulSoup

now = datetime.datetime.now()

today = now.strftime('%Y/%m/%d')

stock_ids = open("stocklist.txt").read().splitlines()

for stock_id in stock_ids:
 url = 'https://tw.stock.yahoo.com/q/q?s='+stock_id
 
 try:
  page = requests.get(url)
  soup = BeautifulSoup(page.content, 'html.parser')
  
  table = soup.find_all(text='成交')[0].parent.parent.parent
  stock_name = table.select('tr')[1].select('td')[0].text
  stock_price = table.select('tr')[1].select('td')[2].text
  
  stock_name2 = stock_name.strip('加到投資組合')
  
  slist = [today,stock_id,stock_price,stock_name2]
  
  print('|'.join(slist)) 
 except:
  print('錯誤或無此代碼!!')
  
 with open('All.csv', 'a', encoding='utf-8-sig', newline='') as f:
      
     writer = csv.writer(f)
     
     writer.writerow(["日期", "股票代號", "成交價" ,"公司名稱"])
         
     templist = []
     templist.append(today)
     templist.append(stock_id)
     templist.append(stock_price)
     templist.append(stock_name2)
              
     writer.writerow(templist)
     writer.writerow("\n")