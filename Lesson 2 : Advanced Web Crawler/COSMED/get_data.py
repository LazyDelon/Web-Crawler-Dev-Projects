import json

import urllib.parse
import urllib.request

import pandas as pd

def Get_Data(City):

    ID = []
    Name = []
    County = []
    Town = []
    lat_list = []
    lng_list = []
    Address = []

    for index, city in enumerate(City):

        new_city = urllib.parse.quote(city)

        URL = "https://www.cosmed.com.tw/api/getStore.aspx?t=store&c="+ new_city +"&d=&s="

        req = urllib.request.Request(URL)
        res = urllib.request.urlopen(req)
        
        data = json.loads(res.read())
        
        for df in data['data']:

            df['縣市'] = df['ZipCodeName1']
            County.append(df['縣市'])
            
            df['門市店號'] = df['ZipCode']
            ID.append(df['門市店號'])

            df['門市店名'] = df['StoreNM']
            Name.append(df['門市店名'])

            df['鄉鎮市區'] = df['ZipCodeName2']
            Town.append(df['鄉鎮市區'])

            df['地址'] = df['ZipCodeName1'] + df['ZipCodeName2'] + df['Address']
            Address.append(df['地址'])
            
            df['lat'] = df['lat']
            lat_list.append(df['lat'])
            
            df['lng'] = df['lng']
            lng_list.append(df['lng'])
            
    results = {'縣市': County, '鄉鎮市區': Town, '門市店名': Name, '門市店號': ID, '地址': Address, '緯度': lat_list, '經度': lng_list}
    
    df = pd.DataFrame(results)
    df.to_csv("Store_COSMED.csv", index=0, encoding="utf_8_sig")
