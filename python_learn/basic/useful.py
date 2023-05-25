# 好用但容易遺忘的內建 function
########################################
# # << filter >>
# # filter(判斷式, 要判斷的list)
# # 記得 filter 完 還要轉回來 對應的型態才能用
# # filter 會移除判斷為 False 的項目

# # 移除 list 裡面為 None 的項目
# def is_None(var) :
#     return var != None
# ll = [1,3,7,None, 8, None, 5]
# new_ll = list(filter(is_None, ll))
# print(new_ll)

########################################
# # << eval >>
# # List
# ll = eval("[[1,2],[3,4]]")
# print(type(ll), ll)
# # dict
# m = eval("{ 1:'a' }")
# print(type(m), m)
# # tuple
# t = eval("(1,'a')")
# print(type(t), t)
# # 運算式
# x = 3
# print("x*7 =",eval("x*7"))

########################################
# # << any >>
# # 如果裡面有任何項目為 True 就會是 True
# mylist = [False, True, False]
# print(any(mylist))

########################################
# # << all >>
# # 如果裡面有任何項目為 False 就會是 False
# mylist = [False, True, True]
# print(all(mylist))

# # 實驗 會不會for全部的項目 或 遇到False就停
#     # ANS : 只要遇到False就停止 不會繼續
#     # 因為下面 range(10)，但是 function 裡面 for 迴圈只有印到 3
# def not_3(num):
#     print("all for to",num)
#     return num != 3
# print("all result :", all(not_3(i) for i in range(10)))




