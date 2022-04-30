# my Runtime: 189 ms, faster than 95.05% of Python3
class Solution:
    def findDiagonalOrder(self, mat):
        # print(mat[0][1])
        # [哪一列][哪一行]
        total_line = len(mat)+len(mat[0])
        x_bond = len(mat)
        y_bond = len(mat[0])
        now_line = 0
        direction = (1,-1)
        
        ans = []
        while True :
            ll = []
            if now_line < y_bond :
                now_x = 0
                now_y = now_line
            else :
                now_y = y_bond - 1
                now_x = now_line - y_bond + 1
                if now_x >= x_bond :
                    break
            while True :
                print(now_x,now_y)
                ll.append(mat[now_x][now_y])
                now_x += direction[0]
                now_y += direction[1]
                if now_x >= x_bond or now_y < 0 :
                    break
            
            # 每次都是往左下掃 如果是偶數就reverse
            if now_line % 2 == 0 :
                ll.reverse()
            ans += ll
            now_line += 1

        return ans



# given ans 跟我一開始的想法一樣
# direction = direction*-1
# 看是超出哪一邊 就更新成新一條線的第一個位置

s = Solution()
print(s.findDiagonalOrder( [[1 ,2 ,3 ,4]
                           ,[5 ,6 ,7 ,8]
                           ,[9 ,10,11,12]
                           ,[13,14,15,16]
                           ]))
print(s.findDiagonalOrder([[1 ,2 ,3]
                          ,[4 ,5 ,6]
                          ,[7 ,8 ,9]
                          ,[10,11,12]
                          ]))
# print(s.findDiagonalOrder([[1,2],[3,4]]))
