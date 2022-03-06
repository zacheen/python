# # 回傳值 兩個對兩個 (概念同 Tuple)
# def func(aa):
#     return aa+1 , aa+2

# aa1,aa2 = func(10)
# print(aa1)
# print(aa2)

# # ----------------------
# # 回傳值 兩個對一個 
# def func(aa):
#     return aa+1 , aa+2

# aa1 = func(10)
# print(aa1)
# print(aa1[0])

# # ----------------------
# # 回傳值 數量不對(三個對兩個)
# def func(aa):
#     return aa+1 , aa+2 , aa+3

# aa1,aa2 = func(10)
# print(aa1)
# print(aa2)

# # ----------------------
# # 沒有回傳值
# def func(aa):
#     aa = aa+1
# print(func(10))

# # ----------------------
# # 回傳後即停止
# def func(aa):
#     aa = aa+1
#     return aa
#     print("AAAAAAAAAAAAAAAAA")
# print(func(10))

# # ----------------------
# # 回傳後停止 運用方式 (while 不用break 即可跳出)
# ll = [1]
# def func(a,b):
#     global ll
#     while True:
#         ll.append(a)
#         a += 1
#         if a >= b :
#             return 
    
# func(5,8)
# print(ll)

# # ----------------------
# # 回傳後停止 for 1
# def func(aa):
#     for x in range(5):
#         aa = aa+1
#         return aa
#     print(aa)
#     return aa

# print(func(10))

# # ----------------------
# # 回傳後停止 for 2
# def func(aa):
#     for x in range(5):
#         aa = aa+1
#         if aa%3 == 0:
#             return aa
#     print(aa)
#     return aa

# print(func(10))

# # ----------------------
# # 回傳後停止 if 
# def func(aa):
#     if aa < 0 :
#         return "小於0"
#         print("AAAAAAAAAAAAA")
#     if aa > 0 :
#         return "大於0"
#         print("AAAAAAAAAAAAA")
#     print("BBBBBBBBBBBBBBB")

# print(func(10))
# print(func(-10))
# print(func(0))

# # ---------------------------------------
# # 回傳後停止 兩層迴圈
# # 印出三角形
# # 方法1 使用 for
# def func(a):
#     return_str = ""
    
#     for x in range(a) :
#         for y in range(x) :
#             return_str = return_str + str(x)
#         return_str = return_str + "\n"
#     return return_str
    
# ll = func(6) 
# print(ll)

# # ---------------
# # 回傳後停止 兩層迴圈
# # 印出三角形
# # 方法2 使用 while
# def func(a):
#     return_str = ""
#     x = 0
#     while True :
#         y = 0
#         while True :
#             return_str = return_str + str(x)
#             if y == a :
#                 return return_str
#             if x == y :
#                 break
#             y = y+1
#         return_str = return_str + "\n"
#         x = x+1
        
# ll = func(6)
# print(ll)
