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
# << filter >>

########################################
# << eval >>

# ll = eval("[[1,2],[3,4]]")
# print(type(ll))
# print(type(ll[0]))
# print(ll[0][0])

m = eval("{ 1:'a'}")
print(type(m))
print(type(m[1]))




