# #------------------------------------
# # str 轉 int / str to int
# print(int("12"))
# # int 轉 str / int to str
# print(str(12))

# # char 轉 int (ascii) / char to int
# print(ord("A"))
# # # int 轉 char / int to char
# print(chr(65))

# # bit 轉 str / bit to str
# print(f'{17:0>{6}b}')
# print(f'{17:b}')
# # str 轉 bit(int) / str to bit(int)
# print(int("10001", 2))
# #------------------------------------
# # 判斷是不是字母
# print("sdjkfl".isalpha())     # True
# print("a1s".isalpha())        # False
# print("!a".isalpha())         # False
# print("中文字".isalpha())     # True...

# #------------------------------------
# # 判斷是不是小寫字母
# print("sdjkfl".islower())     # True
# print("a1s".islower())        # True...
# print("!a".islower())         # True...
# print("中文字".islower())     # False

# #------------------------------------
# # 如果只想判斷是英文字母(排除中文字)
# print("sdjkfl".islower() and "sdjkfl".isalpha())    # True
# print("a1s".islower() and "a1s".isalpha())          # False
# print("!a".islower() and "!a".isalpha())            # False
# print("中文字".islower() and "中文字".isalpha())     # False

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
# # find(str, beg=0, end=len(string))
# # 找出 subString 的開頭位置 (如果沒有回傳 -1)
# print("01234 find 123 :", "01234".find("123"))
# print("1234 find 123 :", "1234".find("123"))
# print("01234 find 1235 :", "01234".find("1235"))

# # 限制範圍 
# print("limit", "00123456".find("123",2,4)) # end位置不包含
# print("limit", "00123456".find("123",2,5))

# # rfind(str, beg=0, end=len(string))
# # 回傳最右邊先找到的項目
# print("12002378490012434  find 00 :", "12002378490012434".find("00"))
# print("12002378490012434 rfind 00 :", "12002378490012434".rfind("00"))

# # 如果只是要判斷有沒有存在用 in 就好
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
# # replace(待替換字串, 替換字串, 最多替換幾次)
# s = "123123"
# ss = s.replace("1", "4")
# print(ss)
# print(s) # 注意原本的不會替換

# #------------------------------------
# # 大寫換小寫 大小寫轉換
# print("AeG!eT".lower())
# print("AeG!eT".upper())

# # <比較 >
# print("ZZ" < "Z")

# # <找字串最小的字>
# print(min("bacd"))

# # <查詢某個字的次數>
# print("aabc".count("a"))
