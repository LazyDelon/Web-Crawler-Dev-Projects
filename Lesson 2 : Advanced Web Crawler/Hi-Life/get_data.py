import requests
import pandas as pd

from bs4 import BeautifulSoup

def Get_Data(result):

    New_results = {"縣市": [""], "鄉鎮市區":  [""], '門市店號': [""], '門市店名': [""], '地址': [""]}

    Store = pd.DataFrame(New_results)
    Store_List = pd.DataFrame(New_results)

    t_results = []

    lst = len(result)

    for i in range(lst):
        
        URL = "https://www.hilife.com.tw/storeInquiry_street.aspx"

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36"
        }

        session = requests.Session()

        req = session.get(URL, headers=headers)
        # req = requests.post(URL, headers=headers)
        soup = BeautifulSoup(req.content, 'html.parser')

        VIEWSTATE = soup.find(id = '__VIEWSTATE')['value']
        GENERATOR = soup.find(id = '__VIEWSTATEGENERATOR')['value']
        EVENTVALIDATION = soup.find(id = '__EVENTVALIDATION')['value']

        form1 = {
            '__EVENTTARGET' : 'CITY',
            '__EVENTARGUMENT' : '',
            '__LASTFOCUS' : '',
            '__VIEWSTATE' : VIEWSTATE,
            '__VIEWSTATEGENERATOR' : GENERATOR,
            '__EVENTVALIDATION' : EVENTVALIDATION,
            'CITY': result[i].get('City'),
            'AREA': '中正區'
        } 
   
        req = session.post(URL, form1, headers=headers)
        
        soup = BeautifulSoup(req.content, 'html.parser')

        area_lst = len(result[i].get('Area'))
        for k in range(area_lst):
        
            VIEWSTATE = soup.find(id = '__VIEWSTATE')['value']
            GENERATOR = soup.find(id = '__VIEWSTATEGENERATOR')['value']
            EVENTVALIDATION = soup.find(id = '__EVENTVALIDATION')['value']

            form2 = {
                '__EVENTTARGET' : 'AREA',
                '__EVENTARGUMENT' : '',
                '__LASTFOCUS' : '',
                '__VIEWSTATE' : VIEWSTATE,
                '__VIEWSTATEGENERATOR' : GENERATOR,
                '__EVENTVALIDATION' : EVENTVALIDATION,
                'CITY': result[i].get('City'),
                'AREA': result[i].get('Area')[k]
            }

            
            req = session.post(URL, form2, headers=headers)

            soup = BeautifulSoup(req.content, 'html.parser')

            data = soup.find('div', 'searchResults')
            for results in data.find_all('tr'):

                Store_List['縣市'] = result[i].get('City')
                Store_List['鄉鎮市區'] = result[i].get('Area')[k]
                Store_List['門市店號'] = results.find_next('th')
                Store_List['門市店名'] = results.th.find_next('th')
                Store_List['地址'] = results.find('a').text
                
                Store = Store.append(Store_List)
                    
    Store.to_csv("Store_Hi-Life.csv", index=0, encoding="utf_8_sig")

            