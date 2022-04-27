# 好用但容易遺忘的內建 function
########################################
# # << min >>  << max >>
# # <list>
# ll = [1, 4, 2, 9, 7, 8, 9, 3, 1]
# print(min(ll))
# # print(ll.min()) # 錯誤語法
# # <map> 會回傳 key 的最大或最小值
# m = {"c":"a","a":9,"b":9}
# print(min(m))

# # 使用 key 技巧
# # min max sort bisect 只要是可以帶入key參數的都適用
# # 技巧1 < 如果是 tuple 會先比前面的 如果前面都一樣才會比下一個 >
# ll = [(1,3,7),(3,1,3),(1,3,9),(1,5,3),(1,5,9),(1,3,5),(3,-1,-1)]
# ll.sort()
# print(ll)
# # 技巧2 < 所以如果有比較的順序可以用成 tuple >
# # 找出最靠近0的數字 如果一樣大取大的
# print(min([-4,-2,1,4,8], key = lambda x : (abs(x), -x) ))
# print(min([2,1,-1]     , key = lambda x : (abs(x), -x) ))
# print(min([2,-1,1]     , key = lambda x : (abs(x), -x) ))

########################################
# # << sum >>
# # # <list>
# ll = [1, 4, 2, 9]
# print(sum(ll))
# # print(ll.sum()) # 錯誤
# # # <map> 回傳 key 的 sum
# m = {0:"a",1:9, 4:9}
# print(sum(m))

########################################
# << abs  >>
# print("abs",abs(-3))
# print("abs",abs(3))

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
# << eval >>

# ll = eval("[[1,2],[3,4]]")
# print(type(ll))
# print(type(ll[0]))
# print(ll[0][0])

# m = eval("{ 1:'a'}")
# print(type(m))
# print(type(m[1]))


########################################
# # << any >>
# # 如果裡面有任何項目為 True 就會是True
# mylist = [False, True, False]
# print(any(mylist))

