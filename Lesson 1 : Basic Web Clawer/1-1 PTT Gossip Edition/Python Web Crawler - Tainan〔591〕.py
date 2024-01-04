# 抓取 591 租屋網 的 網頁原始碼[HTML]
import requests

URL = "https://rent.591.com.tw/?kind=0&region=15"

req = requests.get(URL)

headers={ 
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"
}

web_content = req.text
    
# 解析原始碼，取得每篇文章標題
from bs4 import BeautifulSoup

soup = BeautifulSoup(web_content, "html.parser")

titles = soup.find_all("li", class_="pull-left infoContent")
prices = soup.find_all("div", class_="price")

templist = []
p_list = []

def Title(titles):
    
    for title in titles:
            
        Name = title.find("h3").a.text.strip()
        # data = title.find("p", class_="lightBox").text.strip()
        address = title.find("em").text.strip()
        # price = soup.find_all("div", class_="price")
            
        if title.p.text != None:
                        
            data = title.p.text.strip()
                
            templist.append("{}\n{}\t{}\t{}\n{}\t".
                            format(
                            Name, data.split("|")[-3].strip(), 
                            data.split("|")[-2].strip(), 
                            data.split("|")[-1].strip(), 
                            address ))
            # return("{}\n{}\t{}\t{}\t".format(Name, data.split("|")[-3].strip(), data.split("|")[-2].strip(), data.split("|")[-1].strip() ))

def Price(prices):    
    
    for price in prices:
    
        if price.i.text != None:
            
            price = price.i.text.strip()
            # return("{}元/月".format(price))
            
            p_list.append("{}元/月".format(price))                        

Title(titles)
Price(prices)

dic = {} # 使用大括號{}創建字典

for i in range(0, len(templist)):
    dic[templist[i]] = p_list[i]

for title_list, price_list in dic.items():
    print(title_list, price_list)
    print("\n")
    
    
    