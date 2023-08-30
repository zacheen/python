from bs4 import BeautifulSoup
import requests

# url = 'https://water.taiwanstat.com/'
# web = requests.get(url)                        # 取得網頁內容
# web.encoding = 'UTF-8'
# soup = BeautifulSoup(web.text, "html.parser")  # 轉換成標籤樹
# title = soup.title                             # 取得 title
# print(title)                                   # 印出 title ( 台灣水庫即時水情 )

url = 'https://drive.google.com/drive/folders/1MQ6PTRBZQCdCDIhZdlsLJIrSV-njgeBj'
web = requests.get(url)                        # 取得網頁內容
web.encoding = 'UTF-8'
soup = BeautifulSoup(web.text, "html.parser")  # 轉換成標籤樹
# print(soup.find("div")) # 尋找第一個 div 區塊出現的位置
for all_div in soup.find_all('div'): # 找出全部的 div
    data_id = all_div.get('data-id') # 取出某個欄位的名稱 (若沒找到則為 None)
    if data_id != None :
        print(data_id)