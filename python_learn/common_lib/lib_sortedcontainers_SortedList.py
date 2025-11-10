# 如果要合併兩個已經排序好的 List，應該要用 heapq.merge

from sortedcontainers import SortedList
from operator import neg 

## SortedXX 系列的語法完全相同
## SortedList #######################################
ll = [3,5,1,2,7,6,4]
# # <初始化>
sl = SortedList(ll)
print("數字從小到大 :\n\t",sl)
# <相反方向> key=neg 只能用在 int
sl_rev = SortedList(ll, key=neg)
print("數字從大到小 :\n\t",sl_rev)
# key=neg 只能用在 int (所以這裡會跳錯)
# sl_rev = SortedList('gallahad', key=neg)
# print("從大到小 :",sl_rev)
# <自訂義大小>
sl_rev = SortedList('gallahad', key=lambda x: -ord(x)) # 如果要大到小就加"負號"
print("字母從大到小 :\n\t",sl_rev)

sl = SortedList('gallahad')
# # <<< 語法 >>> <<< 用法 >>> 
# 語法跟 SortedSet 相同
# <新增項目> 同 set 用法
sl.add('e')
print("after add\'e\' :\n\t",sl)
# <新增多個項目>
sl.update(['k','i','j'])
print(r"after update(['k','i','j']) :\n\t",sl)

# <取值> 同 list 用法
print("sl[0] :",sl[0])
print("sl[-1] :",sl[-1])
# <取出最後面的項目>
    # 如果是預設順序從小到大，就會取出最大的項目
print("pop 項目 :",sl.pop())
print("after pop :\n\t",sl)
# <取出範圍內的"值">
print("irange a~j :\n\t",list(sl.irange('a', 'j')))
# <取出範圍內的"index">
print("islice 2,6 :\n\t",list(sl.islice(2, 6)))  # 目前不知道 islice 的優點
print("[]     2,6 :\n\t",sl[2: 6])

# 查找項目位置
print("\'d\' 的位置 :",sl.bisect_left('d'))

# # <刪除> 同 set,list 用法
# 方法 1 del
del sl[0]
print("after del sl[0] :\n\t",sl)

# 方法 2 remove (刪除項目不存在時會報錯)
sl.remove('g')
print("after remove\'e\' :\n\t",sl)
# sl.remove('g') # (刪除項目不存在時會報錯)
# print("after remove\'e\'",sl)
    # remove 的時間複雜度應該是 O(log n)

# 方法 3 discard (刪除項目不存在時"不"會報錯)
sl.discard('h') 
print("after discard\'h\' :\n\t",sl)
sl.discard('h') 
print("after discard\'h\' :\n\t",sl)




