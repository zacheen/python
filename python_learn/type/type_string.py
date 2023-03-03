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
# # 判斷是不是包含 subString
# print("123 in 01234 :", "123" in "01234")
# print("123 in 01234 :", "01234".__contains__("123"))

# print("1235 in 01234 :", "1235" in "01234")
# print("1235 in 01234 :", "01234".__contains__("1235"))

# #------------------------------------
# # 找出 subString 的位置 (如果沒有回傳 -1)
# print("01234 find 123 :", "01234".find("123"))
# print("1234 find 123 :", "1234".find("123"))
# print("01234 find 1235 :", "01234".find("1235"))

# print("1235 in 01234 :", "1235" in "01234")

# #------------------------------------
# # # split 分割字串
# s = "1\t2\t3\n4\n"
# print("use \\t to split :",s.split("\t"))
# # # 注意 split 只能使用一個字串去切割, 不能使用多個
# # #     如果要使用多個 應該要使用 re.split()
# # # 或是使用 replace 
# # # 用 ["\t", "\n"] 分割
# split_list = ["\t", "\n"]
# for split_word in split_list :
#     s = s.replace(split_word,"@@@")
# print("use \\t, \\n to split :", s.split("@@@"))
# # # 需要注意的是 應該要替換成真的不會用到的字串
# # 錯誤範例
# # 想要使用 "and" 跟 "d" 跟 "t" 分割 (所以先把 "t", "and" 轉換成 "d", 再用 "d" 分割)
# s = "I want this ant toy and gameboy"
# print("wrong : "+ str(s.replace("t","d").replace("and","d").split("d")))
# # 錯誤 : ['I w', ' ', 'his ', ' ', 'oy ', ' gameboy']
# print("right : "+ str(s.replace("t","@@@").replace("and","@@@").replace("d","@@@").split("@@@")))
# # 正確 : ['I wan', ' ', 'his an', ' ', 'oy ', ' gameboy']

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
