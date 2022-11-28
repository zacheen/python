# #------------------------------------
# # str 轉 int
# print(int("12"))

# # ascii
# # # char 轉 int
# print(ord("A"))
# # # int 轉 char
# print(chr(65))

# #------------------------------------
# # 判斷是不是字母
# print("sdjkfl".isalpha())
# print("a1s".isalpha())
# print("!a".isalpha())

# #------------------------------------
# # 判斷是不是數字
# print("123".isnumeric())
# print("a1s".isnumeric())
# print("!1".isnumeric())

# #------------------------------------
# # join 組合成字串
# # 注意 !! 只能用 str 組合
# # ll = [1,48,3] 
# ll = ["1","48","3"]
# retStr = '<間隔中間要田什麼>'.join(ll)
# print(retStr)

# # 如果是包含非字串的 list
# ll = [1,"48",3] 
# print("<間隔>".join([str(_) for _ in ll]))

# #------------------------------------
# # replace 字串替換  如果一次要替換多個 請看 import re "多個字符替換" 可以直接搜尋
# replace(待替換字串, 替換字串, 最多替換幾次)
# s = "123123"
# ss = s.replace(["1"], "4")
# print(ss)
# print(s) # 注意原本的不會替換

# #------------------------------------
# # 大寫換小寫 大小寫轉換
# print("AeG!eT".lower())
# print("AeG!eT".upper())


# # << 奇怪的用法 >>
# # <尋找有沒有某個字串> 會回傳開頭的位置 不存在回傳 -1
# txt = "Hello, welcome to my world."
# print(txt.find("welcome"))
# print(txt.find("welcome",8,len(txt)))  # 指定尋找範圍

# # <比較 >
# print("ZZ" < "Z")

# # <找字串最小的字>
# print(min("bacd"))

# # <查詢某個字的次數>
# print("aabc".count("a"))
