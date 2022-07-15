import time
import sys
# !!!! 坑 print 當 CPU 吃滿後 有可能不會馬上印出來 
# 所以要下 sys.stdout.flush() 強制 output 馬上印出來

# 取得當下時間
print(time.time())
# time 轉 字串
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())))

# 測試執行所花時間
start = time.time()
""" do something """
time.sleep(2)
end = time.time()
print("所花時間:",end - start)
sys.stdout.flush()


