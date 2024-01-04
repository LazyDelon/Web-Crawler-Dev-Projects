import json
import requests
import pandas as pd
import urllib.request

from bs4 import BeautifulSoup

def Get_Data(result, headers):

    County = []
    Town = []
    Name = []
    lat_list = []
    lng_list = []
    Address = []

    lst = len(result)

    for i in range(lst):

        
        new_city = urllib.parse.quote(result[i].get('City'))

        area_lst = len(result[i].get('Area'))

        for j in range(area_lst):

            new_area = urllib.parse.quote(result[i].get('Area')[j])

            URL = "https://api.watsons.com.tw/api/v2/wtctw/stores/watStores?currentPage=0&pageSize=20&region=" + new_city + "&district=" + new_area + "&isCceOrCc=false&fields=FULL&lang=zh_TW&curr=TWD"

            req = urllib.request.Request(URL, headers=headers)
            res = urllib.request.urlopen(req)

            data = json.loads(res.read().decode('utf_8_sig'))

            for df in data['stores']:

                df['縣市'] = df['address']['town']
                County.append(df['縣市'])

                df['鄉鎮市區'] = df['address']['district'][3:6]
                Town.append(df['鄉鎮市區'])

                df['門市名稱'] = df['displayName']
                Name.append(df['門市名稱'])

                df['地址'] = df['address']['displayAddress1']
                Address.append(df['地址'])

                df['latitude'] = df['geoPoint']['latitude']
                lat_list.append(df['latitude'])

                df['longitude'] = df['geoPoint']['longitude']
                lng_list.append(df['longitude'])

        results = {'縣市': County, '鄉鎮市區': Town, '門市名稱': Name, '地址': Address, '緯度': lat_list, '經度': lng_list}
        
        df = pd.DataFrame(results)
        df.to_csv("Store_Watsons.csv", index=0, encoding="utf_8_sig")
                