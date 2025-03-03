# my Runtime: 65 ms, faster than 94.07% of Python3
class Solution:
    def minimumTotal(self, triangle):

        min_list = triangle[-1]

        # i 現在在做第幾行
        for i in range(len(triangle)-2,-1,-1) :
            for j in range(i+1): # j 現在在做第幾個項目
                min_list[j] = min(min_list[j], min_list[j+1]) + triangle[i][j]
        return min_list[0]

# given ans
# 直接在原本的 triangle 紀錄

s = Solution()
print(s.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))
print(s.minimumTotal([[-10]]))


