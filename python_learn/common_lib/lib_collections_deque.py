from collections import deque
# 特性是從頭或從尾巴新增或刪除東西 都是 O(1)
# List 刪除尾端是 O(n)

## deque #######################################

# # <<< 語法 >>> <<< 用法 >>> 
# # <初始化>
de = deque()                           
de = deque([1,2,3])       
print("init :",de)
# # <加在最後>
de.append(4)
print("append(4) :",de)
# # <加在最前>
de.appendleft(0)
print("appendleft(0) :",de)
# # <取出最後>
print("de.pop() :",de.pop())
print("after pop() :",de)
# # <取出最前>
print("de.popleft() :",de.popleft())
print("after popleft() :",de)

# 其他用法都跟list一樣

## deque end #######################################
