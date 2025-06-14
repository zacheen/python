# 3213. Construct String with Minimum Cost
# https://leetcode.com/problems/construct-string-with-minimum-cost/description/

from typing import List
from math import inf
from collections import defaultdict
from random import randint

# Double Hashing (雙模哈希)
    # 較安全也更通用
    # 但由於乘法超過 64 位整數範圍，需要用到 bigint，所以效率不如 Single Hashing (單模哈希)
class Solution:
    def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:
        n = len(target)

        # 多項式字串雜湊（方便計算子字串雜湊值）
        # 雜湊函數 hash(s) = s[0] * BASE^(n-1) + s[1] * BASE^(n-2) + ... + s[n-2] * BASE + s[n-1]
        MOD = 10 ** 18 + 3
        BASE = randint(8 * 10 ** 17, 9 * 10 ** 17)  # 隨機 BASE，防止 hack
        pow_base = [1] + [0] * n  # pow_base[i] = BASE^i
        pre_hash = [0] * (n + 1)  # 前綴雜湊值 pre_hash[i] = hash(s[:i])
        for i, b in enumerate(target):
            pow_base[i + 1] = pow_base[i] * BASE % MOD
            pre_hash[i + 1] = (pre_hash[i] * BASE + ord(b)) % MOD  # 秦九韶演算法計算多項式雜湊

        # 每個 words[i] 的雜湊值 -> 最小成本
        min_cost = defaultdict(lambda: inf)
        for w, c in zip(words, costs):
            h = 0
            for b in w:
                h = (h * BASE + ord(b)) % MOD
            min_cost[h] = min(min_cost[h], c)

        # 有 O(√L) 個不同的長度
        sorted_lens = sorted(set(map(len, words)))

        f = [0] + [inf] * n
        for i in range(1, n + 1):
            for sz in sorted_lens:
                if sz > i:
                    break
                # 計算子字串 target[i-sz:i] 的雜湊值（計算方法類似前綴和）
                sub_hash = (pre_hash[i] - pre_hash[i - sz] * pow_base[sz]) % MOD
                # 手寫 min，避免超時
                tmp = f[i - sz] + min_cost[sub_hash]
                if tmp < f[i]:
                    f[i] = tmp
        return -1 if f[n] == inf else f[n]


# Single Hashing (單模哈希)
class Solution:
    def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:
        n = len(target)

        # 多項式字串雜湊(方便計算子字串雜湊值)
        # 雜湊函數 hash(s) = s[0] * BASE^(n-1) + s[1] * BASE^(n-2) + ... + s[n-2] * BASE + s[n-1]
        MOD = 1_070_777_777
        BASE = randint(8 * 10**8, 9 * 10**8)  # 隨機 BASE，防止 hack
        pow_base = [1] + [0] * n  # pow_base[i] = BASE^i
        pre_hash = [0] * (n + 1)  # 前綴雜湊值 pre_hash[i] = hash(s[:i])
        for i, b in enumerate(target):
            pow_base[i + 1] = pow_base[i] * BASE % MOD
            pre_hash[i + 1] = (pre_hash[i] * BASE + ord(b)) % MOD  # 秦九韶演算法計算多項式雜湊

        # 每個 words[i] 的雜湊值 -> 最小成本
        min_cost = defaultdict(lambda: inf)
        for w, c in zip(words, costs):
            h = 0
            for b in w:
                h = (h * BASE + ord(b)) % MOD
            min_cost[h] = min(min_cost[h], c)

        # 有 O(√L) 個不同的長度
        sorted_lens = sorted(set(map(len, words)))

        f = [0] + [inf] * n
        for i in range(1, n + 1):
            for sz in sorted_lens:
                if sz > i:
                    break
                # 計算子字串 target[i-sz:i] 的雜湊值（計算方法類似前綴和）
                sub_hash = (pre_hash[i] - pre_hash[i - sz] * pow_base[sz]) % MOD
                # 手寫 min，避免超時
                tmp = f[i - sz] + min_cost[sub_hash]
                if tmp < f[i]:
                    f[i] = tmp
        return -1 if f[n] == inf else f[n]



s = Solution()
print("ans :",s.minimumCost(target = "abcdef", 
    words = ["abdef","abc","d","def","ef"], 
    costs = [100,1,1,10,5])) # 
print("ans :",s.minimumCost( target = "aaaa", 
    words = ["z","zz","zzz"], costs = [1,10,100])) # 



