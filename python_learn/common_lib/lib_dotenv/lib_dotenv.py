import os
from dotenv import load_dotenv

# 讀取 .env檔 的設定 
load_dotenv(r".env")

# 獲取某個欄位的設定
MY_ID = os.getenv(r'MY_ID')
print(f"MY_ID : {MY_ID}")

# 獲取某個欄位的設定(讀取結果必定是 str)
MY_INT = os.getenv(r'MY_INT')
print(f"MY_INT : {MY_INT}")
print(f"MY_INT type : {type(MY_INT)}")