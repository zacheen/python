# my Runtime: 31 ms, faster than 82.89% of Python3
class Solution:
    def generateMatrix(self, n):
        ans = [[0]*n for i in range(n)]

        bound = n-1
        now_x = 0
        now_y = 0
        now_dir = 0
        for i in range(1,n**2+1) :
            ans[now_x][now_y] = i

            if now_dir == 0: # 右
                if now_y == bound or ans[now_x][now_y+1] != 0 :
                    now_dir = 1
                else :
                    now_y += 1
            if now_dir == 1: # 下
                if now_x == bound or ans[now_x+1][now_y] != 0  :
                    now_dir = 2
                else :
                    now_x += 1
            if now_dir == 2: # 左
                if now_y == 0 or ans[now_x][now_y-1] != 0  :
                    now_dir = 3
                else :
                    now_y -= 1
            if now_dir == 3: # 左
                if now_x == 0 or ans[now_x-1][now_y] != 0  :
                    now_dir = 0
                    now_y += 1 # 因為沒有下一個方向
                else :
                    now_x -= 1

        return ans

# given ans 有很多種方法

s = Solution()
# print(s.generateMatrix(2))
# print(s.generateMatrix(1))
print(s.generateMatrix(3))



