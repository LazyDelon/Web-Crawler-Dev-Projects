# 自動登入 Facebook 頁面

from selenium import webdriver
import time

# 關閉通知
options = webdriver.ChromeOptions()
prefs = {
    'profile.default_content_setting_values':
        {
            'notifications': 2
        }
}
options.add_experimental_option('prefs', prefs)
options.add_argument("disable-infobars")  

# 打啟動selenium 務必確認driver 檔案跟python 檔案要在同個資料夾中
driver = webdriver.Chrome(options=options)
driver.get("https://zh-tw.facebook.com/login/web/")
time.sleep(4)

#輸入email 
context = driver.find_element_by_css_selector('#email')
context.send_keys("xxx@gmail.com")
time.sleep(0.5)

#輸入password
context = driver.find_element_by_css_selector('#pass')
context.send_keys("xxx")
time.sleep(0.5)

#登入按鈕
commit = driver.find_element_by_css_selector('#loginbutton')
commit.click()
time.sleep(3)

# 抓第一筆貼文
getcontext = driver.find_element_by_css_selector('.userContentWrapper')
print(getcontext.text)

