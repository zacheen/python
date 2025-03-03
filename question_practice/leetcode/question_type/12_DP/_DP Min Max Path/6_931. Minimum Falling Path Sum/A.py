# my Runtime: 120 ms, faster than 99.57% of Python3
class Solution:
    def minFallingPathSum(self, matrix):
        edge = len(matrix)-1
        
        for row in range(1, len(matrix)) :
            for col in range(len(matrix)) : # because of Constraints
                prev_row = row-1
                if col == 0 :
                    matrix[row][col] += min(matrix[prev_row][col], matrix[prev_row][col+1])  
                elif col == edge :
                    matrix[row][col] += min(matrix[prev_row][col], matrix[prev_row][col-1])   
                else :
                    matrix[row][col] += min(matrix[prev_row][col], matrix[prev_row][col-1], matrix[prev_row][col+1])
                    
        return min(matrix[-1])

# given ans 我的比較好
# 我是if邊界情況 given是用for三個位置

s = Solution()
print(s.minFallingPathSum([[2,1,3],[6,5,4],[7,8,9]])) # 13



