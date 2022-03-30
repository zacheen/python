# @cache 會記錄之前計算的結果 如果代入相同的變數 會從cache裡面撈資料  
# 好像是 python 3.9 版才有的功能
# 現在只需要知道 如果會重複呼叫的話 就加@cache 我怕我更新版本會出什麼問題

# import time

# # -- @cache -----------------------------------------------------------
# import 
# 使用範例

# class no_use:
#     @cache
#     def use_cache(a,b):
#         ret = a+b
#         print(a,b,ret)
#         return ret

# start = time.time()
# no_use.use_cache(1,2)
# no_use.use_cache(1,2)
# end = time.time()
# print(end - start)






