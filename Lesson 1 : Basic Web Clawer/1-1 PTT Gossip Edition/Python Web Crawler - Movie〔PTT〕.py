# 抓取 PTT 電影版 的 網頁原始碼[HTML]
import urllib.request as req

URL = "https://www.ptt.cc/bbs/HardwareSale/index.html"

# 建立一個 Request 物件，附加 Request Headers 的資訊
request = req.Request(URL, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"
})

with req.urlopen(request) as responce:
    data = responce.read().decode("utf-8")
    
# 解析原始碼，取得每篇文章標題
import bs4

root = bs4.BeautifulSoup(data, "html.parser")

# 尋找 class="title"的 div 標籤
titles = root.find_all("div", class_="title")

print("\n")

for title in titles:
    if title.a != None:
        print(title.a.string)