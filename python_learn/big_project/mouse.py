# mouse 修飾器   好處是可以在不改動原function的情況下 新增功能
# @funcA
# def funcB():
# 執行funcB時 效果等同執行 funcA(funcB)

import time

# # # -- @cache -----------------------------------------------------------
# # @cache 會記錄之前計算的結果 如果代入相同的變數 會從cache裡面撈資料 
# # 方法0 從 Lib import 
from functools import cache
from functools import lru_cache

# # 方法1 使用function實作
# # def cache(func):
# #     data = {}
# #     def wrapper(*args, **kwargs):
# #         key = f'{func.__name__}-{str(args)}-{str(kwargs)})'
# #         if key in data:
# #             result = data.get(key)
# #             # print('cached')
# #         else:
# #             result = func(*args, **kwargs)
# #             data[key] = result
# #             # print('calculated')
# #         return result
# #     return wrapper
# # 方法2 使用class實作
# class cache:
#     def __init__(self, func):
#         self.func = func
#         self.data = {}

#     def __call__(self, *args, **kwargs):
#         func = self.func
#         data = self.data
#         key = f'{func.__name__}-{str(args)}-{str(kwargs)})'
#         if key in data:
#             result = data.get(key)
#             # print('cached')
#         else:
#             result = func(*args, **kwargs)
#             data[key] = result
#             # print('calculated')
#         return result

# # < 使用範例 >
# @cache # 可以註解這行 看第二次的 use_cache(1,2) 會不會執行
# def use_cache(a,b):
#     ret = a+b
#     print(a,b,ret)
#     time.sleep(1)
#     return ret
        
# start = time.time()
# use_cache(1,2)
# use_cache(1,2)
# end = time.time()
# print(end - start)

# # 如果要清除 cache 的記憶體
# # FUNCTION_NAME..cache_clear()
# use_cache.cache_clear()

# # -- @functools.wraps -----------------------------------------------------------
# __module__, __name__, __qualname__, __doc__, and __annotations__
# 上面這些資訊會印出 原本 function 的 而不是 @function 的

def logged(func):
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)
    return with_logging

@logged
def f(x):
   """does some math"""
   return x + x * x
print(f(10))

# 印出 f.__doc__ 的時候應該是希望印出 f 的說明文字
# (因為我們是在使用 f(10) )
print("f.__doc__ :",f.__doc__) # None
# 但不是 所以就出現了 @functools.wraps

# 使用 @functools.wraps 的正確寫法 
import functools
def logged(func):
    @functools.wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)
    return with_logging

@logged
def f(x):
   """does some math"""
   return x + x * x

print(f.__name__)  # 'f'
print(f.__doc__)   # 'does some math'

# # --  -----------------------------------------------------------
