import atexit

def when_exit():
    print("execute before exit!")

atexit.register(when_exit)

# <確定都會觸發>
# # 結束方法1 : 正常結束
# # 結束方法2 : error 退出
# print(1/0)
# # 結束方法2 : 運行中 ctrl + C
# import time
# time.sleep(100)

