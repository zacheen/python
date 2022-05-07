# 技巧 
# 有時候append的條件比較簡單 可以先判斷這個 剩下的再處理

# 第一種 是不會再加入新的項目的
def def_stack(ll):
    stack = []
    for item in ll:
        if stack and "頂端合併條件" :
            top = stack.pop()  # 記得要 pop
            "符合條件後要做的事"
        else :
            stack.append(item)
    return stack

# # 第一種 EX: 如果相鄰兩個字母是一樣就刪除
# def removeDuplicates(ll):
#     stack = []
#     for item in ll:
#         if stack and item == stack[-1] :
#             top = stack.pop()  # 記得要 pop
#             # 在這裡 取出之後就沒事了
#         else :
#             stack.append(item)
#     return "".join(stack)
# print("移除重複字母",removeDuplicates("azxxzya"))

# 第二種 是會再加入新的項目的
def def_stack(ll):
    stack = []
    for item in ll:
        while stack and "頂端合併條件" :
            top = stack.pop()  # 記得要 pop
            item = "符合條件後要做的事" # 覆寫到 item
        stack.append(item)
    return stack

# # 第二種 EX : 如果與隔壁有公因數就合併成最小公倍數
# import math
# def replaceNonCoprimes(ll):
#     stack = []
#     for item in ll:
#         while stack :
#             ret = math.gcd(stack[-1], item)
#             if ret > 1 :
#                 item = (stack.pop() * item) // ret
#             else :
#                 break
#         stack.append(item)
#     return stack
# print("合併成最小公倍數",replaceNonCoprimes([5,7,35]))