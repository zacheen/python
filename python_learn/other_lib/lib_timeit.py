# 專門用來計時程式碼執行時間的 Lib
import timeit

import time

def my_sleep():
    time.sleep(2)

# 測試執行所花時間
# number 是執行次數
print(timeit.timeit('time.sleep(2)', number=3))
print(timeit.timeit(my_sleep, number=3))

