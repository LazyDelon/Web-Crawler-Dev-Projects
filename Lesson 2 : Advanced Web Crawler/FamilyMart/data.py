import requests
import pandas as pd
import get_data as gd

from bs4 import BeautifulSoup

City = [
    '基隆市',
    '台北市',
    '新北市',
    '桃園市',
    '新竹市',
    '新竹縣',
    '苗栗縣',
    '台中市',
    '彰化縣',
    '雲林縣',
    '南投縣',
    '嘉義縣',
    '嘉義市',
    '台南市',
    '高雄市',
    '屏東縣',
    '台東縣',
    '花蓮縣',
    '宜蘭縣',
    '連江縣',
    '金門縣',
    '澎湖縣'
]

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36"}


gd.Get_Data(City)
# gd.Get_StoreData(City)




