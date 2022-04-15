# 修飾器   好處是可以在不改動原function的情況下 新增功能
# @funcA
# def funcB():
# 執行funcB時 效果等同執行 funcA(funcB)

import time

# # -- @cache -----------------------------------------------------------
# @cache 會記錄之前計算的結果 如果代入相同的變數 會從cache裡面撈資料 
# cache是要自己實作的 
        # 但是leetcode有內建
        # https://docs.python.org/3/library/functools.html
        # 裡面說 python3.9 好像有內建 可是我試了失敗
# 方法1 使用function實作
# def cache(func):
#     data = {}
#     def wrapper(*args, **kwargs):
#         key = f'{func.__name__}-{str(args)}-{str(kwargs)})'
#         if key in data:
#             result = data.get(key)
#             # print('cached')
#         else:
#             result = func(*args, **kwargs)
#             data[key] = result
#             # print('calculated')
#         return result
#     return wrapper
# 方法2 使用class實作
class cache:
    def __init__(self, func):
        self.func = func
        self.data = {}

    def __call__(self, *args, **kwargs):
        func = self.func
        data = self.data
        key = f'{func.__name__}-{str(args)}-{str(kwargs)})'
        if key in data:
            result = data.get(key)
            # print('cached')
        else:
            result = func(*args, **kwargs)
            data[key] = result
            # print('calculated')
        return result

# < 使用範例 >
# @cache # 可以註解這行 看第二次的 use_cache(1,2) 會不會執行
def use_cache(a,b):
    ret = a+b
    print(a,b,ret)
    time.sleep(1)
    return ret
        
start = time.time()
use_cache(1,2)
use_cache(1,2)
end = time.time()
print(end - start)


# @lru_cache(None)
# 效果等同 @cache  不過會根據使用的次數  調整記憶體空間
# 比較常用的取用就會比較快



