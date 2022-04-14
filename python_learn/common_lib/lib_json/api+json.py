# 這個檔案只是記錄 怎麼用json打API 並不能跑
import json 
import requests
def send_url(url):
    print("url :", url)
    try:
        my_data = {
            "id" : Tool_Main.get_id() ,
            "companyurl": Tool_Main.get_url(), 
            "gameurl":url
        }
        response = requests.post("http://"+Tool_Main.ip+"/crawler/save", headers=headers, data=json.dumps(my_data) )
        print(response.json())
    except Exception :
        print("posting backend error")