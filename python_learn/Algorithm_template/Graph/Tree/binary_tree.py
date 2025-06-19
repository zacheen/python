# <<通用>>
# <遍歷每個項目> (從小到大的項目遍歷)
## template ##########################
# from collections import deque
# queue = deque([root])
# while queue :
#     now_n = queue.popleft()
#     if now_n.left != None :
#         queue.append(now_n.left)
#         ...
#     if now_n.right != None :
#         queue.append(now_n.right)
#         ...
## template end ##########################

# <特別的金字塔>
#                  1
#             2         3
#         4     5     6     7
#     8    9  10 11 12 13 14 15
# 16   17 ...    ^
    # 特性 : 
        # 左 = val*2
        # 右 = val*2+1

# <路線> : 
    # 去第一位(因為一定是1)
    # 從高位開始，0代表向左，1代表向右
# print(f'{11:b}') # 1011 : 左右右
## template ##########################
# for c in f'{target:b}'[1:]:
#     if c == "0" :
#         now_n = now_n.left
#     else :
#         now_n = now_n.right
## template end ##########################



# 目前不知道有啥用 #######################
#                  0
#             1         2
#         3     4     5     6
#     7    8  9  10 11 12 13 14
# 15   16 ...    ^
# 特性 : 
    # 左 = val*2+1
    # 右 = val*2+2