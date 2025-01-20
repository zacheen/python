# 3430. Maximum and Minimum Sums of at Most Size K Subarrays
# https://leetcode.com/problems/maximum-and-minimum-sums-of-at-most-size-k-subarrays/description/

from typing import List
import functools

from math import inf
# my fail : Time Limit Exceeded
# my 5538ms
class SegTree:
    def __init__(self, nums, comp, init):
        self.n = len(nums)
        self.comp = comp
        self.init = init
        # init
        self.tree = [0] * 2 * self.n
        for i,real_i,n in zip(range(self.n, 2 * self.n), range(self.n) , nums):
            self.tree[i] = (n, real_i)
        for i in range(self.n-1, 0, -1):
            # execute def
            if comp(self.tree[2*i][0], self.tree[2*i+1][0]) :
                self.tree[i] = self.tree[2*i]
            else :
                self.tree[i] = self.tree[2*i+1]

    def query(self, left, right):
        # include
        left += self.n
        right += self.n-1
        res = [self.init, -1]
        while left <= right:
            if left & 1 :
                # combine result
                if self.comp(self.tree[left][0], res[0]) :
                    res = self.tree[left]
                left += 1
            if not (right & 1) :
                # combine result
                if self.comp(self.tree[right][0], res[0]) :
                    res = self.tree[right]
                right -= 1
            left >>= 1
            right>>= 1
        return res

class Solution:
    def minMaxSubarraySum(self, nums: List[int], k: int) -> int:
        @functools.lru_cache
        def add_to_1(n):
            return (n+1)*n//2
        @functools.lru_cache
        def cal_comb(l, mid , r):
            if l != 0 :
                return cal_comb(0, mid-l, r-l)
            # # ori
            # ret_ori = 0
            # for i in range(min(mid+1,k)) :
            #     ret_ori += min(k-i-1, r-mid-1)+1 # +1 是為了包含0
            # # opt
            ret = add_to_1(k)
            min_r = (k-1)-(r-mid-1)
            if min_r > 0 : # right length not enought
                ret -= add_to_1(min_r)
            min_l = k-(mid+1)
            if min_l > 0 : # left length not enought
                ret -= add_to_1(min_l)
            min_overlap = (min_r + min_l) - k
            if min_overlap > 0:
                ret += add_to_1(min_overlap)
            return ret

        ans = 0
        segtree = SegTree(nums, lambda x, y : x <= y, inf)
        def min_dp(l, r): # r not include
            nonlocal ans
            if l >= r or l < 0 or r > len(nums):
                return
            min_n, min_n_i = segtree.query(l,r)
            ans += min_n*cal_comb(l, min_n_i, r)
            min_dp(l,min_n_i)
            min_dp(min_n_i+1,r)
        min_dp(0, len(nums))

        segtree = SegTree(nums, lambda x, y : x >= y, -inf)
        def max_dp(l, r): # r not include
            nonlocal ans
            if l >= r or l < 0 or r > len(nums):
                return
            max_n, max_n_i = segtree.query(l,r)
            ans += max_n*cal_comb(l, max_n_i, r)
            max_dp(l,max_n_i)
            max_dp(max_n_i+1,r)
        max_dp(0, len(nums))

        return ans

# given ans No1. : 1940ms
class Solution(object):
    def minMaxSubarraySum(self, nums, k):
        # same as my cal_comb, add_to_1
        def f(x):
            return 0 if x < 0 else (x+1)*(x+2)//2
        def count_subwindows(L, R, M):
            return f(M) - f(M-(L+1)) - f(M-(R+1)) + f(M-(L+1)-(R+1))
        
        def sum_of_min_subarrays_at_most_k(arr, k):
            n = len(arr)
            # left and right 各自存了 這個數字在這個範圍裏面是最大或最小的
            left = [0]*n
            right = [0]*n
            stack = []
            for i in range(n):
                while stack and arr[stack[-1]] > arr[i]:
                    stack.pop()
                left[i] = i - (stack[-1] if stack else -1) - 1
                stack.append(i)
            stack = []
            for i in range(n-1, -1, -1):
                while stack and arr[stack[-1]] >= arr[i]:
                    stack.pop()
                right[i] = (stack[-1] if stack else n) - i - 1
                stack.append(i)
            s = 0
            M = k-1
            for i in range(n):
                c = count_subwindows(left[i], right[i], M)
                s += arr[i]*c
            return s
        
        def sum_of_max_subarrays_at_most_k(arr, k):
            n = len(arr)
            left = [0]*n
            right = [0]*n
            stack = []
            for i in range(n):
                while stack and arr[stack[-1]] < arr[i]:
                    stack.pop()
                left[i] = i - (stack[-1] if stack else -1) - 1
                stack.append(i)
            stack = []
            for i in range(n-1, -1, -1):
                while stack and arr[stack[-1]] <= arr[i]:
                    stack.pop()
                right[i] = (stack[-1] if stack else n) - i - 1
                stack.append(i)
            s = 0
            M = k-1
            for i in range(n):
                c = count_subwindows(left[i], right[i], M)
                s += arr[i]*c
            return s
        
        return sum_of_min_subarrays_at_most_k(nums, k) + sum_of_max_subarrays_at_most_k(nums, k)

s = Solution()
# print("ans :",s.minMaxSubarraySum(nums = [1,2,3], k = 2)) # 9 +  = 20
# print("ans :",s.minMaxSubarraySum(nums = [1,2,3,4,2,1], k = 3))
# print("ans :",s.minMaxSubarraySum(nums = [1,4,2,3,5,0], k = 3))
print("ans :",s.minMaxSubarraySum(nums = [1,0,0,2,0,0,0], k = 2))
# print("ans :",s.minMaxSubarraySum(nums = [1,-3,1], k = 2)) # -7 +  = -6
# print("ans :",s.minMaxSubarraySum(nums = [-4,-17,17], k = 1)) # -8
# print("ans :",s.minMaxSubarraySum(nums = [15,-3,-11], k = 3)) 

