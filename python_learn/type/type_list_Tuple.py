# #------------------------------------
# # # <初始化> 初始化指定大小list
# ll = [False]*10
# # # <初始化> list
ll = [1,2,3,5,6,7,8,9,8]
print("init :",ll)
# # # <增加項目> O(1)
# ll.append(4)
# print("append :",ll)
# # # <插入項目> insert(位置, val) O(n)
# ll.insert(3,10)
# print("insert :",ll)
# # # <刪除多個或一個>
# del(ll[2:3])
# print("del :",ll)
# # # <取出 X 的 index>
# print("index :",ll.index(8) )
# # # <取出第N個項目之後的 X 的 index>
# # # index(target, start, end)
# print("index next :",ll.index(8, ll.index(8)+1) )
# # # <取出 X 的 index> (如果不存在)
# try : 
#     print("index :",ll.index(100) )
# except ValueError:
#     print("this value is not in list")
# # # <計算 X 總共有幾個>
# print("count :",ll.count(8) )
# print("count :",ll.count(100) ) # 如果不存在 會回傳 0
# # # <取出第N個項目> (不是取出某個值)
# print("pop 5 :",ll.pop(5))
# print("pop 5 :",ll)
# # # pop 最後一個項目
# print("pop last :",ll.pop())
# print("pop last :",ll)
# # # <刪除某個值>
# ll.remove(5)
# print("remove :",ll)
# # # <不確定有沒有此值的取出>
# try :
#     ll.remove(100)
# except ValueError :
#     print("didnt have this value")
# print("remove2 :",ll)

# #------------------------------------
# # 初始化 Tuple 基本上用法跟 list 一樣 只是不能更改
# tt = ()
# print(tt)

# #------------------------------------
# # list 冒號取值 (開頭:結尾:間隔)  如果有一格不填代表要取值到list結束
# ll = [1,2,3,4,5,6,7,8,9,10,11,12]
# print(ll[3:-2:2])
# print(ll[2::2])
# print(ll[8::-1])

# # 數字可以取到最後一項 甚至可以超出
# print(ll[5:])
# print(ll[5:len(ll)])
# print(ll[5:12])
# print(ll[5:13]) # 超出範圍

# #------------------------------------
# # list 排序 sort
# ll = [1,3,6,4,0,2]
# # 如果不想要改 原本的list  sorted(list, key, reverse)
# print("sorted :",sorted(ll))
# print("original :",ll)
# # 要改動原本的list
# ll.sort()
# print(ll)

# #------------------------------------
# # list 排序 sort 反向 reverse
# ll = [1,3,6,4,0,2]
# print(ll)
# ll.sort(reverse=True)
# print(ll)

# #------------------------------------
# # list 排序 sort 使用自定義function ( key )
# # 如果是一樣的順序就會按照原本的排序

# # 1. 使用 function
# def myFunc(e):
#     return len(e)
# cars = ['Ford', 'EMW', 'Mitsubishi', 'ABC', 'BMW', 'VW', 'DMW', 'CMW']
# cars.sort(reverse=True, key=myFunc)
# print(cars)

# # 2. 使用 lambda
# cars = ['Ford', 'EMW', 'Mitsubishi', 'ABC', 'BMW', 'VW', 'DMW', 'CMW']
# cars.sort(reverse=True, key = lambda x : (len(x), x) )
# print(cars)

# #------------------------------------
# # list 排序 sort 使用自定義function ( compare )
# # 如果是一樣的順序就會按照原本的排序 ?? (看起來是這樣還沒驗證)
# # 使用第二個值來排序
# def hash_value(item1):
#     return item1[1]
# ll = [("no mean", 6), ("no mean", 8), ("no mean", 23), ("no mean", 10), ("no mean", -7), ("no mean", -4)]
# ll = sorted(ll, key=hash_value)
# print(ll)

# #------------------------------------
# # list 反向 反轉 reverse 
# ll = [1,3,6,4,0,2]
# print(ll)
# # 方法1 如果只是要 for 某個東西的 reverse
# print("reverse() : ",list(reversed(ll)))
# print("reverse() : ",ll)
# # 方法2 如果真的是要動到原本的
# print(".reverse : ",ll.reverse())
# print(".reverse : ",ll)

# #------------------------------------
# # list 反向 反轉 reverse 某個區間
# # 包含 l,r 兩個位置
# def reverse(nums, l, r):
#     while l < r:
#         nums[l], nums[r] = nums[r], nums[l]
#         l += 1
#         r -= 1

# ll = [0,1,2,3,4,5,6,7]
# reverse(ll,3,6)
# print("reverse region :", ll)

# #------------------------------------
# # 隨機 隨機list的順序
# import random
# random.shuffle(ll)
# print("shuffle :",ll)

# #------------------------------------
# # 如果要用 compare 來 sort
# class ClassForSort(int):
#     def __lt__(x, y):
#         return x > y

# ll = [1,5,3,7,3,8,9]
# ll = sorted(ll, key=ClassForSort)
# print(ll)

# #------------------------------------
# list comprehensive 快速建立規律list
# 語法
# [運行function for var_Name in List_Name ]
# var_Name 通常會傳入 運行function

# # 範例1 轉型
# nums = [1,2,3]
# def change(x):
#     return str(x)
# ll = [change(x) for x in nums]
# print("list comprehensive 1 : ",ll)

# # 範例2 取奇數
# nums = [1,2,3]
# def change(x):
#     return x*2-1
# ll = [change(x) for x in nums]
# print("list comprehensive 2 : ",ll)

# #------------------------------------
# # 判斷兩個 List 有無重複項目
# ll = [1,2]
# ll2 = [2,3,4]
# if len(set(ll) & set(ll2)) == 0 :
#     print("ll 與 ll2 沒有東西重疊")
# else:
#     print("ll 與 ll2 有東西重疊")

# #------------------------------------
# # list 會連動 坑
# # 跟 string 不會連動 做比較
# str1 = [1,2,3]
# str2 = str1
# str2 += [4,5]
# print(str2)
# print(str1)

# #------------------------------------
# # 判斷這個 list 裡面是否有任何東西 == len(l) >= 1
# # l = [1,2]
# l = []
# if l :
#     print("l have thing")
# else :
#     print("l dont have thing")

#-------------------------------------------------------------------------------------------
# # <<< 之前踩過的坑 >>>

# # copy 只會複製 目前這一層而已
# red = ['flower', 'blood', [55, 6]]
# red_list = list(red)
# red_slice = red[:]
# red_copy = red.copy()
# import copy
# red_deepcopy = copy.deepcopy(red)

# print("ori   :",red)
# print("list  :",red_list)
# print("slice :",red_slice)
# print("copy  :",red_copy)
# print("deep  :",red_deepcopy)
# red[0] = 100  # 這是第一層 所以其他不會被影響
# red[2][0] = 88  # 這是第二層 其他會跟著被影響
# print("ori   :",red)
# print("list  :",red_list)
# print("slice :",red_slice)
# print("copy  :",red_copy)
# print("deep  :",red_deepcopy)

# # 不可使用 * 初始化 List 多維陣列
# len_x = 4
# len_y = 3
# ll = [[False]*len_y]*len_x 
# ll[0][0] = True  
# # 每個list的第一個 都變成 True 了  因為不是用 copy
# print(ll)
# # <<正確>> # 二維的 2D
# ll = [[False]*len_y for _ in range(len_x)] # <- 要用 for 迴圈 (目前最快的方法)
# ll[0][0] = True  
# print(ll)

# # 在計算時 pop (前面的會先計算)
# ll = [1,2,3,4]
# print("ll.pop()+ll[-1] :",ll.pop()+ll[-1]) # 7
# ll = [1,2,3,4]
# print("ll[-1]+ll.pop() :",ll[-1]+ll.pop()) # 8

# # 把最後一個項目加到 倒數第二個後 刪除
# ll = [1,2,3,4]
# ll[-1] = ll[-2]+ll.pop()  # 這樣寫比較直覺
# print("ll :",ll) # 8

# # list * 2 不是把裡面的數值*2，而是增加項目
# ll = [1,2,3]
# print(ll*2)
# # 是 [1, 2, 3, 1, 2, 3]，不是 [2,4,6]

