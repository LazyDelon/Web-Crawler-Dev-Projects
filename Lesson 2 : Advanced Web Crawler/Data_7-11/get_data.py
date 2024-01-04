import requests
import pandas as pd

from bs4 import BeautifulSoup


def Get_Data(result):

    TownNameList = []

    lst = len(result)

    for i in range(lst):

        form = {
            "commandid": "GetTown",
            "cityid": result[i].get("CityID")
        }
        
        res = requests.post('https://emap.pcsc.com.tw/EMapSDK.aspx', data=form) 
        
        # html.parser
        soup = BeautifulSoup(res.content, 'lxml')
        # print(soup)
        

        TownName = soup.find_all("townname")

        for name in TownName:
            if name not in TownNameList:
            # TownNameList = name.text
                TownNameList.append(name.text)
    return TownNameList


def Get_StoreData(result):

    ID_list = []
    Name_list = []
    X_list = []
    Y_list = []
    Address_list = []

    lst = len(result)

    for i in range(lst):
        
        form = {
            "commandid": "SearchStore",
            "city": result[i].get("City"),
            "town": Get_Data(result)
        }

        res = requests.post('https://emap.pcsc.com.tw/EMapSDK.aspx', data=form) 

        soup = BeautifulSoup(res.content, 'xml')

        POIID = soup.find_all("POIID")
        for id in POIID:
            ID_list.append(id.text)

        POIName = soup.find_all("POIName")
        for name in POIName:
            Name_list.append(name.text)

        X = soup.find_all("X")
        for x in X:
            X_list.append( float(x.text)/1000000 )
        
        Y = soup.find_all("Y")
        for y in Y:
            Y_list.append( float(y.text)/1000000 )

        Address = soup.find_all("Address")
        for address in Address:
            Address_list.append(address.text)

    results = {'門市店號': ID_list, '門市店名': Name_list, 'Y': Y_list, 'X': X_list, '地址': Address_list}
    print(results)
    # df = pd.DataFrame(results)

    # df = df.drop_duplicates()
    # # print(df)
    # df.to_csv("Store_7-11.csv", index=0, encoding="utf_8_sig")
    # print(results)

    # print("______________")
  