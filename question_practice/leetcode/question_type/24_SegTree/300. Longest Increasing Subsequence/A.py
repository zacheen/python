# 300. Longest Increasing Subsequence (有更多解法)
# https://leetcode.com/problems/longest-increasing-subsequence/

# segment tree version 95ms Beats72.55%
class SegTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] * 2 * self.n

    # 更新這個位置最大長度
    def update(self, index, val):
        index += self.n
        self.tree[index] = val
        while index > 1:
            # update node
            self.tree[index>>1] = max(self.tree[index], self.tree[index^1])
            index >>= 1

    # 查詢這個數字以前最大長度
    def query(self, left, right):
        # include
        left += self.n
        right += self.n
        res = 0
        while left <= right:
            if left & 1 :
                # combine result
                res = max(res, self.tree[left])
                left += 1
            if not (right & 1) :
                # combine result
                res = max(res, self.tree[right])
                right -= 1
            left >>= 1
            right>>= 1
        return res

class Solution:
    def lengthOfLIS(self, nums):
        # discrete > dense
        rank = { x : i for i, x in enumerate(sorted(list(set(nums)))) } # 各個數字的大小排行

        sg = SegTree(rank)
        for num in nums:
            prev = sg.query(0, rank[num] - 1) # 判斷在這個數字之前(0~(rank[num] - 1)) 各自數字"最長"(max)的結果
            sg.update(rank[num], prev + 1) 
        return sg.query(0, len(rank) - 1) # 查找最大的數字 回傳就是最長的組合
    
# # 其實觀念很像下面這個
# # 只不過這直接用數字去紀錄
# from bisect import bisect_left
# class Solution:
#     def lengthOfLIS(self, nums):
#         # tail[i] := the minimum tail of all increasing subseqs having length i + 1
#         # it's easy to see that tail must be an increasing array
#         tail = []
#         for num in nums:
#             if not tail or num > tail[-1]:
#                 tail.append(num)
#             else:
#                 tail[bisect_left(tail, num)] = num
#         return len(tail)

s = Solution()
print(s.lengthOfLIS([1,2,3]))
# print(s.lengthOfLIS([3,2,1]))
# print(s.lengthOfLIS([10,9,2,5,6,3,7,101,18]))
# print(s.lengthOfLIS([0,1,0,3,2,3]))
# print(s.lengthOfLIS([7,7,7,7,7,7,7]))
# print(s.lengthOfLIS([1,3,6,7,9,4,10,5,6,8,9]))
# print(s.lengthOfLIS([1,3,6,7,9,2,10,5,6,8,9]))
# print(s.lengthOfLIS([1,3,5,7,3,5,]))
# print(s.lengthOfLIS([2,2]))

