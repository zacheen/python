import time
import sys
# !!!! 坑 print 當 CPU 吃滿後 有可能不會馬上印出來 
# 所以要下 sys.stdout.flush() 強制 output 馬上印出來

# # 取得當下時間
# print(time.time())
# # 把時間轉成 我們看得懂的時間
# print("現在小時 :",time.localtime(time.time()).tm_hour)
# # time 轉 字串
# print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())))

# # 測試執行所花時間
#     # 如果要計時還有另外一個 lib 可以用 : timeit
# start = time.time()
# """ do something """
# time.sleep(2)
# end = time.time()
# print("所花時間:",end - start)
# sys.stdout.flush()


