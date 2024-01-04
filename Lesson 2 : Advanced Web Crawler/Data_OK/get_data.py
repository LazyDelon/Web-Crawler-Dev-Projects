import pandas as pd
import urllib.request 
from bs4 import BeautifulSoup

def Get_Data(City):

    results = {'縣市': [""], '鄉鎮市區': [""], '門市店名': [""], '地址': [""]}
    
    Store = pd.DataFrame(results)
    Store_list = pd.DataFrame(results)

    for index, city in enumerate(City):

        new_city = urllib.parse.quote(city)
       
        URL = "https://www.okmart.com.tw/convenient_shopSearch_Result.aspx?city=" + new_city
        
        res = urllib.request.Request(URL)
        req = urllib.request.urlopen(res)
        
        req_txt = req.read()
        content = req_txt.decode()

        soup = BeautifulSoup(content, 'html.parser')
        
        keyword_li = soup.find_all("li")

        for li in keyword_li:

            Name = li.find('h2').text.strip()
            Address = li.find('span').text.strip()
            town = Address[3:6]

            Store_list['縣市'] = city
            Store_list['鄉鎮市區'] = town
            Store_list['門市店名'] = Name
            Store_list['地址'] = Address
            
            Store = Store.append(Store_list)
            
    Store.to_csv("Store_OK.csv", index=0, encoding="utf_8_sig")
