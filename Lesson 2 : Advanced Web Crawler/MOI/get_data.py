import os
import sqlite3
import pandas as pd
from glob import glob
from operator import index
from numpy import expand_dims


def get_data(path):

    files = glob('109年內政大數據資料應用組競賽用資料集_村里.csv')

    df = pd.concat(
            (pd.read_csv(file,header=0, usecols=['COUNTY_ID',
                                                 'COUNTY',
                                                 'TOWN_ID',
                                                 'TOWN',
                                                 'V_ID',
                                                 'VILLAGE']
                        ,dtype={'name': str, 'tweet': str}) for file in files), ignore_index=True)

    # 查詢是否已有資料夾，無資料夾則新增一個
    folder = path + "整合\\"
    if not os.path.isdir(folder):
        os.makedirs(folder)

    df.columns = ['COUNTY_ID','COUNTY','TOWN_ID','TOWN','V_ID','VILLAGE']

    df.to_csv(folder + "Change1.csv", encoding="utf_8-sig", index = False)


# aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa


    files = glob('109年內政大數據資料應用組競賽用資料集_村里.csv')

    df = pd.read_csv('109年內政大數據資料應用組競賽用資料集_村里.csv')

    csv_list = []

    for i in range(1,77):
        
        datalist = 'COLUMN' + str(i)
        
        df = pd.concat(
                (pd.read_csv(file,header=0, usecols=[datalist], squeeze=True
                            ,dtype={'name': str, 'tweet': str}) for file in files), ignore_index=True)

        
        df.columns = [datalist]

        csv_list.append(df)
    
    df = pd.DataFrame(csv_list)

    df.to_csv(folder + "Change2.csv", encoding="utf_8-sig", index = True)


# aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa


    files = glob('109年內政大數據資料應用組競賽用資料集_村里.csv')

    df = pd.read_csv('109年內政大數據資料應用組競賽用資料集_村里.csv')

    csv_list = []

    for i in range(100,135):
        
        datalist = 'COLUMN' + str(i)
        
        df = pd.concat(
                (pd.read_csv(file,header=0, usecols=[datalist], squeeze=True
                            ,dtype={'name': str, 'tweet': str}) for file in files), ignore_index=True)

        
        df.columns = [datalist]

        csv_list.append(df)
    
    df = pd.DataFrame(csv_list)
    
    df.to_csv(folder + "Change3.csv", encoding="utf_8-sig", index = True)
    
    print(df)
# aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa


def combine_all_data(path):

    # 查詢是否已有資料夾，無資料夾則新增一個
    folder = path + "整合\\"
    if not os.path.isdir(folder):
        os.makedirs(folder)

    df = pd.read_csv(folder + "Change2.csv", encoding='utf_8-sig')

    num = (len(df.columns))+1
    df = df.values.tolist()
    #設定一個空陣列，放置列數
    num_list = []
    for i in range(1, num):
        num_list += [i]
    #將陣列從int轉str
    num_list = [str(i) for i in num_list]
    df = pd.DataFrame(columns = num_list, data = df)

    #把 Dataframe 轉成 2D numpy array
    data = df.values
    #找到數據的 key
    index1 = list(df.keys())
    #行列互換，再利用map函數將zip內的元組轉列表
    data = list(map(list, zip(*data)))
    data = pd.DataFrame(data, index=index1)
    
    data.to_csv(folder + "Change2.csv", encoding='utf_8-sig', header=0, index = False)
    

# aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa


    df = pd.read_csv(folder + "Change3.csv", encoding='utf_8-sig')

    num = (len(df.columns))+1
    df = df.values.tolist()
    #設定一個空陣列，放置列數
    num_list = []
    for i in range(1, num):
        num_list += [i]
    #將陣列從int轉str
    num_list = [str(i) for i in num_list]
    df = pd.DataFrame(columns = num_list, data = df)

    #把 Dataframe 轉成 2D numpy array
    data = df.values
    #找到數據的 key
    index1 = list(df.keys())
    #行列互換，再利用map函數將zip內的元組轉列表
    data = list(map(list, zip(*data)))
    data = pd.DataFrame(data, index=index1)
    
    data.to_csv(folder + "Change3.csv", encoding='utf_8-sig', header=0, index = False)


# aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa


def get_merge(path):

    # 查詢是否已有資料夾，無資料夾則新增一個
    folder = path + "整合\\"
    if not os.path.isdir(folder):
        os.makedirs(folder)

    files = glob(folder + "Change*.csv")

    #串列中包含兩個Pandas DataFrame
    df_list = [pd.read_csv(file) for file in files]
    
    result = pd.concat([df_list[0],df_list[1],df_list[2]], axis=1, ignore_index=False)

    result.to_csv(folder + "Change.csv", index=False, encoding='utf-8-sig')


# aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa


def csv_db(path):

    # 查詢是否已有資料夾，無資料夾則新增一個
    folder = path + "資料庫\\"
    if not os.path.isdir(folder):
        os.makedirs(folder)

    conn = sqlite3.connect(folder + "database.db")

    df = pd.read_csv(path+"整合\\" + "Change.csv", encoding="utf-8-sig") 

    df.to_sql("all", conn, if_exists="replace", index=False)