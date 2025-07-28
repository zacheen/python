# 3629. Minimum Jumps to Reach End via Prime Teleportation
# https://leetcode.com/problems/minimum-jumps-to-reach-end-via-prime-teleportation

from typing import List
from math import inf
from collections import defaultdict
from functools import cache

# inspire by given ans (new template) : 667ms Beats100.00%
MAX = 10**6 + 1
prime_fac = [[] for _ in range(MAX)]
for i in range(2, MAX):
    if not prime_fac[i] : # 若沒有任何的因數 代表是質數
        for j in range(i, MAX, i):
            prime_fac[j].append(i)

class Solution:
    def minJumps(self, nums: List[int]) -> int:
        # bfs 向外擴張
        not_seen = [True]*len(nums)

        # 把每個數字的 "質數因數" 對應到 其位置
            # 所以並不是 list 一定比較快
        n2i = defaultdict(list) # 874ms Beats100.00%
        # n2i = [[] for _ in range(now_Max)] # 8835ms Beats33.33%
        for i, n in enumerate(nums) :
            for p_f in prime_fac[n] :
                n2i[p_f].append(i)

        q = [0]
        ans_cnt = 0
        end_i = len(nums)-1
        while q :
            # if end_i in q :
            #     return ans_cnt
            new_q = []
            for now_i in q :
                if now_i == end_i :
                    return ans_cnt
                
                now_num = nums[now_i]
                # prime
                # 因為就只有質數 才會有路徑，所以也不需要判斷是不是質數
                for next_i in n2i[now_num] : 
                    if not_seen[next_i] :
                        new_q.append(next_i)
                        not_seen[next_i] = False
                del(n2i[now_num])
                        
                # right
                if not_seen[(r := now_i+1)] :
                    new_q.append(r)
                    not_seen[r] = False

                # left
                if not_seen[(l := now_i-1)] :
                    if now_i != 0 :
                        new_q.append(l)
                        not_seen[l] = False

            ans_cnt += 1
            q = new_q
        return ans_cnt

# my 1673ms Beats66.67%
MAX = 10 ** 6 + 1
prime = [True]*MAX
prime[0] = False
prime[1] = False
for i in range(2, int(MAX**(1/2)+1)):
    if not prime[i]:
        continue
    for j in range(i*i, MAX, i):
        prime[j] = False

class Solution:
    def minJumps(self, nums: List[int]) -> int:
        if len(nums) == 1 : return 0

        now_Max = max(nums)+2
        
        # bfs 向外擴張
        seen_node = set()
        seen_prime = set()

        n2i = defaultdict(list) # 1673ms Beats66.67%
        # n2i = [[] for _ in range(now_Max)] # 4939ms Beats33.33%
        for i, n in enumerate(nums) :
            n2i[n].append(i)

        q = [0]
        ans_cnt = 0
        end_i = len(nums)-1
        while q :
            new_q = []
            for now_i in q :
                now_num = nums[now_i]
                # prime
                if prime[now_num] :
                    if now_num not in seen_prime :
                        seen_prime.add(now_num)
                        if nums[-1] % now_num == 0 :
                            return ans_cnt + 1
                        for m in range(now_num, now_Max, now_num) :
                            for next_i in n2i[m] :
                                if next_i not in seen_node :
                                    new_q.append(next_i)
                                    seen_node.add(next_i)
                        
                # right
                if (r := now_i+1) not in seen_node :
                    if r == end_i :
                        return ans_cnt + 1
                    new_q.append(r)
                    seen_node.add(r)

                # left
                if (l := now_i-1) not in seen_node :
                    if now_i != 0 :
                        new_q.append(l)
                        seen_node.add(l)

            ans_cnt += 1
            q = new_q
        return ans_cnt

s = Solution()
print("ans :",s.minJumps([1,2,4,6])) # 2
print("ans :",s.minJumps([2,3,4,7,9])) # 2
print("ans :",s.minJumps([4,6,5,8])) # 3
print("ans :",s.minJumps([1])) # 0
print("ans :",s.minJumps([5,7,9,5,1])) # 2
print("ans :",s.minJumps([7, 4, 5, 6, 7])) # 1
print("ans :",s.minJumps([383, 4, 5, 6, 383])) # 1
