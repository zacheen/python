# 優化 given ans Beats 86.74%
class Solution(object):
    def nthUglyNumber(self, n):
        nums = [1]
        i2 = 0
        i3 = 0
        i5 = 0

        # 對每個數字來說
            # 當我現在這個數字 *(2或3或5)
            # 那下一個 *(2或3或5) 之後最小的數字一定是 "現在這個數字的下一個數字*(2或3或5)"
        # 對 List 來說就是找出上面的 3 個候選數字最小的那一個 一定就是下一個最小的數字
        next2 = 2
        next3 = 3
        next5 = 5

        while len(nums) < n:
            next = min(next2, next3, next5)
            # print(i2, i3, i5)
            # print(nums[i2], nums[i3], nums[i5])
            # print(next2, next3, next5)
            # print(nums)
            # print("-------------------")
            nums.append(next)
            if next == next2:
                i2 += 1
                next2 = nums[i2] * 2
            if next == next3:
                i3 += 1
                next3 = nums[i3] * 3
            if next == next5:
                i5 += 1
                next5 = nums[i5] * 5
        return nums[-1]

# me 20230305 重新練習
# class Solution:
#     def nthUglyNumber(self, n):
#         last_small_2_indx = 0
#         last_small_3_indx = 0
#         last_small_5_indx = 0

#         mem = [1]
#         mul_2 = mem[last_small_2_indx] * 2
#         mul_3 = mem[last_small_3_indx] * 3
#         mul_5 = mem[last_small_5_indx] * 5

#         for _ in range(n-1):
#             next_small_mul = min(mul_2, mul_3, mul_5)
#             mem.append(next_small_mul)
#             if next_small_mul == mul_2 :
#                 last_small_2_indx += 1
#                 mul_2 = mem[last_small_2_indx] * 2
#             if next_small_mul == mul_3 :
#                 last_small_3_indx += 1
#                 mul_3 = mem[last_small_3_indx] * 3
#             if next_small_mul == mul_5 :
#                 last_small_5_indx += 1
#                 mul_5 = mem[last_small_5_indx] * 5
#         return mem[-1]

s = Solution()
print(s.nthUglyNumber(20))



