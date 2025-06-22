# break
# continue

# #------------------------------------
# # Range 間隔 (初始值,結束值,間隔)
# for x in range(2,8,3):
#     print(x)

# #------------------------------------
# # foreach 
# for x in [1,3,6,7]:
#     print(x)

# #------------------------------------
# # 如果同時要取 index 跟 value 使用 enumerate (list or str)

# s = "abcd"
# for idx, val in enumerate(s):
#     print(idx, val)

# # enumerate 可以設定起始 index
# s = "abcd"
# start_idx = 2
# for idx, val in enumerate(s ,start_idx):
#     print(idx, val)

# #------------------------------------
# # 坑 !! 不要對foreach的List進行改動  判斷結束會使用改動後的list進行判斷
# # 錯誤 會進無窮迴圈
# s = ["a"]
# for indx, word in enumerate(s) :
#     print("no copy :",indx, word)
#     s.append("N")

# 只要是 沒有創建一個新的 List 就會出問題
# s = ["a"]
# for indx, word in enumerate(s) :
#     print("no copy :",indx, word)
#     s.extend("N")

# # 使用 copy 才不會出問題
# s = ["a","b"]
# for indx, word in enumerate(s.copy()) :
#     print("copy :",indx, word)
#     s.append("N")
# print("after :",s)

# # 創建一個新的也不會出問題
# s = ["a","b","c"]
# for indx, word in enumerate(s) :
#     print("new :",indx, word)
#     s = list(s)
#     s.append("N")
# print("after :",s)

# # 使用 + 也不會出問題 (因為也等於創建了一個新的list)
# s = ["a","b","c"]
# for indx, word in enumerate(s) :
#     print("new :",indx, word)
#     s = list(s)
#     s += ["N"]
# print("after :",s)

# # string 也不會出問題
# s = "ab"
# for indx, word in enumerate(s) :
#     s = s+"N"
# print(s)

# #------------------------------------
# # 如果同時要取 index 跟 value (map)
# # map 不能直接用 enumerate !! 坑 
# m = {1:"a",2:"b"}
# for key, val in m.items():
#     print(key, val)

# # 如果直接取 只會取到 key 職
# for key in m:
#     print(key)

# print(list(range(5,-1)))


