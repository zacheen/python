# 2444. Count Subarrays With Fixed Bounds
# https://leetcode.com/problems/count-subarrays-with-fixed-bounds/

# my 
# class Solution:
#     def countSubarrays(self, nums, minK, maxK):
        # 先判斷 斷點(小於minK 大於maxK) -> 有可能的解答一定在這個區間 
        # 三種情況
        # 1 只有 minK, maxK 其中一個數字
        # 2 minK, maxK 兩個數字不同 且 都存在
            # 這個想不到要怎麼處理
                # 不能左邊的組合*右邊的組合
                # minK1, maxK , minK2
                # 會有 左minK1 * maxK右 跟 左maxK+minK2右 的情況 且 還要扣除重複的項目
        # 3 minK, maxK 兩個數字相同 且 存在
            # 看有幾個連續 (n+1)*n/2

# given ans
# 這個我不懂叫什麼演算法 (我先叫 find substring)
class Solution:
    def countSubarrays(self, nums, minK, maxK):
        ans = 0
        r = -1
        # 紀錄上一個 minK 跟 maxK
        prevMinKIndex = -1
        prevMaxKIndex = -1

        # r 是紀錄最前面可以當開頭的位置
        # l 是紀錄現在的位置
        for now_pos, num in enumerate(nums):
            if num < minK or num > maxK:
                r = now_pos
            if num == minK:
                prevMinKIndex = now_pos
            if num == maxK:
                prevMaxKIndex = now_pos
            # any index k in [j + 1, min(prevMinKIndex, prevMaxKIndex)] can be the
            # start of the subarray s.t. nums[k..i] satisfies the conditions
            ans += max(0, min(prevMinKIndex, prevMaxKIndex) - r)
            # min(prevMinKIndex, prevMaxKIndex) : 代表最後面開頭的位置
            # min(prevMinKIndex, prevMaxKIndex) - r : 代表 最後面可以當開頭的位置 - 最前面可以當開頭的位置 = 在尾端為 now_pos 不同開頭位置有幾種組合
            print(num, now_pos, r, prevMinKIndex,prevMaxKIndex, max(0, min(prevMinKIndex, prevMaxKIndex) - r), ans)

        return ans

s = Solution()
# print(s.countSubarrays(nums = [2,1,3,5,2,7,5], minK = 1, maxK = 5))
print(s.countSubarrays(nums = [2,1,3,5,1,2,7,5], minK = 1, maxK = 5))
# print(s.countSubarrays(nums = [1,1,1,1], minK = 1, maxK = 1))



