# 透過 追蹤網路的超連結 抓取 下一個網頁的資訊 - 連續抓取頁面實務

# 抓取 PTT 八卦版 的 網頁原始碼[HTML]
import urllib.request as req 

def getData(URL):

    # 建立一個 Request 物件，附加 Request Headers 的資訊
    request = req.Request(URL, headers={
        "cookie":"over18=1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"
    })
    
    with req.urlopen(request) as responce:
        data = responce.read().decode("utf-8")
        
    # 解析原始碼，取得每篇文章標題
    import bs4
    
    root = bs4.BeautifulSoup(data, "html.parser")
    
    # 尋找所有 class="title"的 div 標籤
    titles = root.find_all("div", class_="title")
    
    # 如果標題包含 a 標籤〔沒有則刪除〕，印出來
    for title in titles:
        if title.a != None:
            print(title.a.string)
            print("https://www.ptt.cc" + title.a.get("href"))
            
    # 利用 a 標籤 裡面的文字，來抓取 超連結 網址
    NextLink = root.find("a", string="‹ 上頁")
    return NextLink["href"]

    # 確認網址是否完整 - 相對網址
    # print(NextLink["href"])
            
PageURL = "https://www.ptt.cc/bbs/Gossiping/index.html"

count = 0
print("\n")
print("---------------")

while count < 5:
    PageURL = "https://www.ptt.cc" + getData(PageURL)
    count = count + 1
    
    print("---------------")

