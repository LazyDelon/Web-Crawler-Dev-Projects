# 抓取 PChome 24 的 網頁原始碼[Json格式]
import json
import requests 

URL = "https://ecshweb.pchome.com.tw/search/v3.3/all/results?q=msi&page=1&sort=sale/dc"

req = requests.get(URL)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"
}

web_content = json.loads(req.text)

web_data = web_content['prods']

# print(len(web_data)) 所抓取到 PChome24的商品數量

for product in web_data:
    print(product['name'])
    print(product['price'])
    print("\n")