# 抓取 台銀匯率 的 網頁原始碼[HTML]

import requests

URL = "https://rate.bot.com.tw/xrt?Lang=zh-TW"

# 使用 requests.get(URL)，來取得網頁回傳內容
req = requests.get(URL)

headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"
}

# 把 requests.get()回傳的內容，放在 req物件 的 text屬性中，存至 web_content
web_content = req.text

# 解析原始碼，取得每篇文章標題
from bs4 import BeautifulSoup

data = BeautifulSoup(web_content, "html.parser")

Name = data.find_all("div", class_="hidden-phone print_show")
Cash = data.find_all("td", class_="rate-content-cash text-right print_hide")
Now = data.find_all("td", class_="text-right display_none_print_show print_width")

print("幣別\t現金買入\t現金賣出\t即時買入\t即時賣出")

for Count in range(0, 19):
    print("{}\t{}\t{}\t{}\t{}".format(
          Name[Count].text.strip(),
          Cash[Count*2].text.strip(),
          Cash[Count*2+1].text.strip(),
          Now[Count*2].text.strip(),
          Now[Count*2+1].text.strip() ))
