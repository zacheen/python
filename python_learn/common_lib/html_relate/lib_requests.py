import requests

import time

# 取得 網頁跳轉 之後的網址
def get_redirect_url(url) :
    web = requests.get(url)                        # 取得網頁內容
    return web.url

# 以測試過不用 sleep 即可跳轉 # for i in range(10) : 
url = 'https://drive.google.com/uc?id=1GYS0jp4T2ZaCL0eQAH5n6wAcPIGCVL0R&confirm=t'
print(get_redirect_url(url))
