# generator genexpr yeild
    # type(g) 會印出
    # <generator object <genexpr> at ...>

# generator 有很多種
    # genexpr 請看 type_genexpr
    # 有 yeild 的 function

# # genexpr的完整語法 : 
    # # "(var_name [前判斷式] for var_name in iterable [後判斷式])"
    # #  ^這個括號是一定要有的 (如果要產生 genexpr 的話)

# # -- 型態 genexpr ----------------------------------------------
# # < 1.基本語法 > : 有 "()" 括號 跟 "for" 跟 可 iterable 的東西
    # # EX: (x for x in [1,2,3])

    # # 可 iterable 的東西可為
        # # 某個list
        # # enumerate(iterable)
        # # range (range自己也是一種 Class)

# # < 2.可以加上判斷式 > ----------------------------------------------
# # 判斷式"給值"
# # 判斷式正常用法 : 如果是偶數 才賦予值
# x = 4 #3
# x = x if x%2==0 else 0
# print(x)
# # [] 裡面的判斷式用法
# # 用法1 : 只挑出符合的項目 (用法跟 filter 有點像)
# ll = [1,3,4,6,7,8,9,11,12]
# new_ll = [x for x in ll if x%2 == 0] # 挑出偶數的項目
# print("if back  :", new_ll)
# # 用法2 : 把不符合的項目改成其他值
# ll = [1,3,4,6,7,8,9,11,12]
# new_ll = [x if x%2 == 0 else 0 for x in ll ] # 把奇數(不符合的項目)改成0
# print("if front  :", new_ll)

# # < 3.完整語法 > : (var_name [前判斷式] for var_name in iterable [後判斷式])
       # # ^這個括號是一定要有的 (如果要產生 genexpr 的話)
# # 如果有第二組就是雙層for迴圈
# # 這種東西不能 直接print(因為還沒執行)
# # 但可以透過以下方法得到全部的值
#     # []
#     # 轉型
#     # 當成 iterable 丟進某個 function
# # (可以想成 待執行的iterable)

# << 各種創建範例 >> ##################################
ll = [1,3,4]
# # <單層的>
# print("單層的 :",[x for x in ll])

# # <雙層的>
# print("雙層的 :",[x*y for x in ll if x%2==1 for y in ll])

# # <當成list 丟入function>
# print("sum : ",sum(x for x in ll))
# print("sum : ",sum([x for x in ll]))

ll = [1,3,4,6,7,8,9,11,12]
# # Example : 如果是偶數 就加上位置後回傳
# columns = [str(each_num)+"_"+str(indx) for indx, each_num in enumerate(ll) if each_num % 2 == 0]
# print(columns)
########################################################

# # <實驗> ########################################################
# # 範例 genexpr 本身不能直接 print
# g = (x for x in ll if x%2==0 ) # 只取偶數
# print("print :",g)
# print("next(g) :",next(g))
# print("g.__next__() :",g.__next__())