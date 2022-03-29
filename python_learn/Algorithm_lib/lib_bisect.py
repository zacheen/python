import bisect
# bisect.bisect_left(a, x, lo=0, hi=len(a), *, key=None)
    # 回傳此項目在相同項目中第一個位置
    # 在 a 當中找到一個位置，讓 x 插入後 a 仍然是排序好的。
        # 如果 a 裡面已經有 x 出現，插入的位置會在所有 x 的前面（左邊）。回傳值可以被當作 list.insert() 的第一個參數
    # 參數 lo 和 hi 用來指定 list 中應該被考慮的子區間，預設是考慮整個 list 
    # key 指定帶有單個參數的 key function，用於從每個輸入元素中提取比較鍵。默認值為 None (直接比較元素)。

# bisect.bisect_right(a, x, lo=0, hi=len(a), *, key=None)
    # 回傳此項目在相同項目中最後一個位置"的後面" 
        # (所以這個位置並不是target 而是可以插入的位置)

# bisect.bisect(a, x, lo=0, hi=len(a), *, key=None)
    # 同 bisect_left 或 bisect_right
    # 可以設定為 left 或 right (預設為 right)

# # 尋找位置 #####################################
# #indx 0,1,2,3,4,5,6,7,8
# l =  [0,1,2,5,5,5,6,7,8]
# left = bisect.bisect_left(l, 5)
# print("bisect_left :",left)
# l.insert(left,"X")
# print("insert place :", l)

# l =  [0,1,2,5,5,5,6,7,8]
# right = bisect.bisect_right(l, 5)
# print("bisect_right :",right)
# l.insert(right,"X")
# print("insert place :", l)

# l =  [0,1,2,5,5,5,6,7,8]
# print("bisect :",bisect.bisect(l, 5))

# # 插入位置 #####################################
# key python 3.10 版才有
#indx 0,1,2,3,4,5,6,7,8
# l =  [0,1,2,5,5,5,6,7,8]
# bisect.insort_left(l, 5.1, key = lambda x: int(x))
# print("insort_left :",l)

# l =  [0,1,2,5,5,5,6,7,8]
# bisect.insort_right(l, 5.1, key = lambda x: int(x))
# print("insort_right :",l)

# l =  [0,1,2,5,5,5,6,7,8]
# right = bisect.insort(l, 5.1)
# print("insort :", l)
