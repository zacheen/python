########################################


########################################
# # << min >>  << max >>
# # <list>
# ll = [1, 4, 2, 9, 7, 8, 9, 3, 1]
# print(min(ll))
# # print(ll.min()) # 錯誤語法
# # <map> 會回傳 key 的最大或最小值
# m = {"c":"a","a":9,"b":9}
# print(min(m))

# # # < default= >
# # print(min([])) # 傳入空的 list 會跳 ValueError
# print(min([] , default = 0)) # 這時可以給預設值

# # < key = >
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
# << abs >> 絕對值
# print("abs",abs(-3))
# print("abs",abs(3))

