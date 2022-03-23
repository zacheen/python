# # iterable 的東西可為
#     # 某個list
#     # enumerate(iterable)

# # -- 型態 genexpr ----------------------------------------------
# # 語法 : 執行回傳 for var_name in iterable [判斷式] [for var_name in iterable[判斷式]] 
# # 如果有第二組就是雙層for迴圈
# # 這種東西不能 直接print(因為還沒執行)
# # 但可以透過一下方法執行它  
#     # []
#     # 轉型
#     # 當成 iterable 丟進某個function
# # (可以想成 待執行的iterable)
# # EX:

# # <單層的>
# ll = [1,3,4]
# print([x for x in ll])

# # <雙層的>
# ll = [1,3,4]
# print([x*y for x in ll if x%2==1 for y in ll])

# # <當成list 丟入function>
# print("sum : ",sum(x for x in ll))
# print("sum : ",sum([x for x in ll]))

# # Example : 如果是偶數 就加上位置後回傳
# ll = [1,3,4,6,7,8,9,11,12]
# columns = [str(each_num)+"_"+str(indx) for indx, each_num in enumerate(ll) if each_num % 2 == 0]
# print(columns)


