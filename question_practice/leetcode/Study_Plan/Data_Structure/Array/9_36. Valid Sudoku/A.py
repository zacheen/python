# my 
class Solution:
    def isValidSudoku(self, board: List[List[str]]):
        # 橫的 跟 直的 可以合併
        check_ver = [set() for _ in range(len(board[0]))]
        for each_line in board :
            check_hor = set()
            for i, val in enumerate(each_line) :
                if val != "." :
                    if val in check_hor or val in check_ver[i] :
                        return False
                    else :
                        check_hor.add(val)
                        check_ver[i].add(val)
        
        # 橫的
#         for each_line in board :
#             check = set()
#             for val in each_line :
#                 if val != "." :
#                     if val in check :
#                         return False
#                     else :
#                         check.add(val)
                        
#         # 直的
#         check = [set() for _ in range(len(board[0]))]
#         for each_line in board :
#             for i, val in enumerate(each_line) :
#                 if val != "." :
#                     if val in check[i] :
#                         return False
#                     else :
#                         check[i].add(val)
                        
        
                        
        # 九宮格
        for start_x in [0,3,6] :
            for start_y in [0,3,6] :
                check = set()
                for i in range(start_x, start_x+3) :
                    print(board[i][start_y:start_y+3])
                    for val in board[i][start_y:start_y+3] :
                        if val != "." :
                            if val in check :
                                return False
                            else :
                                check.add(val)
        return True
                        
# given ans
    # str(i // 3) + str(j // 3) 這個東西要熟悉 要能立即反應 (O)
# 因為數量不大 所以速度跟上面的差不多
# class Solution:
#     def isValidSudoku(self, board: List[List[str]]):
#         seen = set()

#         for i in range(9):
#             for j in range(9):
#                 c = board[i][j]
#                 if c == '.':
#                     continue
#                 if c + '@row ' + str(i) in seen or \
#                     c + '@col ' + str(j) in seen or \
#                     c + '@box ' + str(i // 3) + str(j // 3) in seen:
#                         return False
#                 seen.add(c + '@row ' + str(i))
#                 seen.add(c + '@col ' + str(j))
#                 seen.add(c + '@box ' + str(i // 3) + str(j // 3))
#         return True

s = Solution()
print(s.isValidSudoku())



