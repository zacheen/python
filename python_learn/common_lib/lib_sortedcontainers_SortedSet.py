from sortedcontainers import SortedSet
from operator import neg 

## SortedXX 系列的語法完全相同
## SortedSet #######################################
# # <初始化>
ll = [3,5,1,2,7,6,4]
# # <初始化>
ss = SortedSet(ll)
print("數字從小到大 :",ss)
# <相反方向> key=neg 只能用在 int
ss_rev = SortedSet(ll, key=neg)
print("數字從大到小 :",ss_rev)
# key=neg 只能用在 int (所以這裡會跳錯)
# ss_rev = SortedSet('gallahad', key=neg)
# print("從大到小 :",ss_rev)
# <自訂義大小>
ss_rev = SortedSet('gallahad', key=lambda x: -ord(x)) # 如果要大到小就加"負號"
print("字母從大到小 :",ss_rev)

ss = SortedSet('gallahad')
# # <<< 語法 >>> <<< 用法 >>> 
# <新增項目> 同 set 用法
ss.add('e')
print("after add\'e\' :",ss)
# # <取值> 同 list 用法
print("sl[0] :",ss[0])
print("sl[-1] :",ss[-1])

# # <刪除> 同 set,list 用法
# 方法 1 del
del ss[0]
print(ss)
# 方法 2 remove
ss.remove('g')
print(ss)
# ss.remove('g') # (刪除項目不存在時會報錯)
# print("after remove\'e\'",ss)
# 方法 3 discard (刪除項目不存在時"不"會報錯)
ss.discard('h') 
print("after discard\'h\' :",ss)
ss.discard('h') 
print("after discard\'h\' :",ss)

# 查找項目位置
print("\'d\' 的位置 :",ss.bisect_left('d'))

