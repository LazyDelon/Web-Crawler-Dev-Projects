# 抓取 Yahoo！ 即將上市 的 網頁原始碼[HTML]
import requests

URL = "https://movies.yahoo.com.tw/movie_thisweek.html"
# 使用 requests.get(URL)，來取得網頁回傳內容
req = requests.get(URL)

headers={
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"        
}
# 把 requests.get()回傳的內容，放在 req物件 的 text屬性中，存至 web_content
web_content = req.text
    
# 解析原始碼，取得每篇文章標題
from bs4 import BeautifulSoup
soup = BeautifulSoup(web_content, "html.parser")

titles = soup.find_all("div", class_="release_info")

# strip 同時去掉左右的空隙
# split(':')[-1] 對冒號進行分割

for title in titles:

    Name = title.find("div", class_="release_movie_name").a.text.strip()
    En_Name = title.find("div", class_="en").a.text.strip()
    
    Level_Name = title.find("div", class_="level_name").text.strip()
    # Level = title.find("div", class_="leveltext").span.text.strip()
    
    Time = title.find("div", class_="release_movie_time").text.split(':')[-1].strip()
    
    if title.span != None:
        Level = title.span.text
        print("{}〔{}〕 {}:{} {}".format(Name, En_Name, Level_Name, Level, Time))