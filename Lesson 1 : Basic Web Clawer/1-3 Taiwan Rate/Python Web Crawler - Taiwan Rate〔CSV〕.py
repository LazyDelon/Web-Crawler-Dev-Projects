# 抓取 台銀匯率 的 網頁原始碼[HTML]
import csv
import requests

URL = "https://rate.bot.com.tw/xrt?Lang=zh-TW"

# 使用 requests.get(URL)，來取得網頁回傳內容
req = requests.get("https://rate.bot.com.tw/xrt?Lang=zh-TW")

# 把 requests.get()回傳的內容，放在 req物件 的 text屬性中，存至 web_content
web_content = req.text

# 解析原始碼，取得每篇文章標題
from bs4 import BeautifulSoup

data = BeautifulSoup(web_content, "html.parser")

Name = data.find_all("div", class_="hidden-phone print_show")
Cash = data.find_all("td", class_="rate-content-cash text-right print_hide")
Now = data.find_all("td", class_="rate-content-sight text-right print_hide")

with open('Taiwan Rate.csv', 'w', encoding='utf-8-sig', newline='') as f:

    writer = csv.writer(f)
    writer.writerow(("幣別", "現金買入", "現金賣出" ,"即時買入" ,"即時賣出"))

    for Count in range(0, 19):
        print("{}\t{}\t\t{}\t\t{}\t\t{}".format(
              Name[Count].text.strip(),
              Cash[Count*2].text.strip(),
              Cash[Count*2+1].text.strip(),
              Now[Count*2].text.strip(),
              Now[Count*2+1].text.strip() ))

        templist = []
        templist.append(Name[Count].text.strip())
        templist.append(Cash[Count*2].text.strip())
        templist.append(Cash[Count*2+1].text.strip())
        templist.append(Now[Count*2].text.strip())
        templist.append(Now[Count*2+1].text.strip())
    
        writer.writerow(templist)
    
    
    