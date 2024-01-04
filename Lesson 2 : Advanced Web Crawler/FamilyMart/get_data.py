import json
import pandas as pd

def Get_Data(City):

    lst = len(City)

    County = []
    Town = []
    Name_list = []
    X_list = []
    Y_list = []
    Address_list = []

    for i in range(lst):
        
        data = open('familymart//'+ City[i] +'.json', encoding='utf_8_sig')
        data = json.load(data)
        

        # df = pd.DataFrame(data)
        # print(data)
        for df in data:
            df['縣市'] = df['addr'][0:3]
            County.append(df['縣市'])

            df['鄉鎮市區'] = df['addr'][3:6]
            Town.append(df['鄉鎮市區'])

            df['門市店名'] = df['NAME']
            Name_list.append(df['門市店名'])

            df['地址'] = df['addr']
            Address_list.append(df['地址'])

            df['y'] = df['py']
            Y_list.append(df['y'])

            df['x'] = df['px']
            X_list.append(df['x'])
            
    results = {'縣市': County, '鄉鎮市區': Town ,'門市店名': Name_list, '地址': Address_list, 'y': Y_list, 'x': X_list}
    
    df = pd.DataFrame(results)
    df.to_csv("Store_FamilyMart.csv", index=0, encoding="utf_8_sig")
