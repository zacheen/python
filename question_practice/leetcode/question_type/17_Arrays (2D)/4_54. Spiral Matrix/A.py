# my Runtime: 31 ms, faster than 86.52% of Python3
class Solution:
    def spiralOrder(self, matrix):
        ans = []

        now_dir = 0

        while len(matrix) > 0 and len(matrix[0]) > 0 :
            print(matrix)
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

# given ans

s = Solution()
print(s.spiralOrder([[1,2 ,3 ,4]
                    ,[5,6 ,7 ,8]
                    ,[9,10,11,12]]))
# print(s.spiralOrder())



