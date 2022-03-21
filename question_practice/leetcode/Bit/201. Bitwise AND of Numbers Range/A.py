class Solution:
    def rangeBitwiseAnd(self, left, right):
        # print(left, bin(left))
        # print(right, bin(right))

        # My v2 Runtime: 105 ms, faster than 27.43% of Python3
        # 應該是2分法
        # 轉字串 從頭 開始比 第一個位數不同的後面都要 shift
        # count_shift_time = 0
        # while left > 0 and left != right:
        #     left = left >> 1
        #     right = right >> 1
        #     count_shift_time = count_shift_time + 1
        # return left << count_shift_time

        # v3 優化 Runtime: 48 ms, faster than 98.04% of Python3
        count_shift_time = 0
        while left > 0:
            if left == right :
                break
            left = left >> 1
            right = right >> 1
            count_shift_time = count_shift_time + 1
        return left << count_shift_time

        # My v1 最直覺的 Time Limit Exceeded
        # ans = right
        # for i in range(left, right) :
        #     ans = ans & i
        # # return ans 
        # print(ans, bin(ans))


s = Solution()
print(s.rangeBitwiseAnd(left = 5, right = 5))
print(s.rangeBitwiseAnd(left = 3, right = 4))
print(s.rangeBitwiseAnd(left = 9, right = 15))
print(s.rangeBitwiseAnd(left = 0, right = 0))
print(s.rangeBitwiseAnd(left = 1, right = 2147483647))