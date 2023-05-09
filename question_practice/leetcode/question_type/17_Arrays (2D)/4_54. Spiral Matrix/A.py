# my Runtime: 31 ms, faster than 86.52% of Python3
class Solution:
    def spiralOrder(self, matrix):
        ans = []

        now_dir = 0

        while len(matrix) > 0 and len(matrix[0]) > 0 :
            # print(matrix)
            if now_dir == 0 :
                ans += matrix[0]
                del(matrix[0])
            elif now_dir == 1 :
                for i in range(len(matrix)) :
                    ans.append(matrix[i][-1])
                    del(matrix[i][-1])
            elif now_dir == 2 :
                matrix[-1].reverse()
                ans += matrix[-1]
                del(matrix[-1])
            elif now_dir == 3 :
                for i in reversed(range(len(matrix))) :
                    ans.append(matrix[i][0])
                    del(matrix[i][0])

            now_dir += 1
            if now_dir == 4:
                now_dir = 0

        return ans

# given ans Beats 12.57%
# 就真的按照順序存取
class Solution:
    def spiralOrder(self, matrix):
        if not matrix:
            return []

        m = len(matrix)
        n = len(matrix[0])
        ans = []
        r1 = 0
        c1 = 0
        r2 = m - 1
        c2 = n - 1

        # Repeatedly add matrix[r1..r2][c1..c2] to ans
        while len(ans) < m * n:
            j = c1
            while j <= c2 and len(ans) < m * n:
                ans.append(matrix[r1][j])
                j += 1
            i = r1 + 1
            while i <= r2 - 1 and len(ans) < m * n:
                ans.append(matrix[i][c2])
                i += 1
            j = c2
            while j >= c1 and len(ans) < m * n:
                ans.append(matrix[r2][j])
                j -= 1
            i = r2 - 1
            while i >= r1 + 1 and len(ans) < m * n:
                ans.append(matrix[i][c1])
                i -= 1
            r1 += 1
            c1 += 1
            r2 -= 1
            c2 -= 1

        return ans

s = Solution()
print(s.spiralOrder([[1,2 ,3 ,4]
                    ,[5,6 ,7 ,8]
                    ,[9,10,11,12]]))
# print(s.spiralOrder())



