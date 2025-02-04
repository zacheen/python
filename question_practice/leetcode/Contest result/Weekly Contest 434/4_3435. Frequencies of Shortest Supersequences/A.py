# 3435. Frequencies of Shortest Supersequences
# https://leetcode.com/problems/frequencies-of-shortest-supersequences/description/

from typing import List
import functools
from math import inf

from collections import defaultdict
# given ans
class Solution:
    def supersequences(self, words: List[str]) -> List[List[int]]:
        # 收集有哪些字母，同時建立圖
        all_mask = 0
        g = defaultdict(list)
        for x, y in words:
            x, y = ord(x) - ord('a'), ord(y) - ord('a')
            all_mask |= 1 << x | 1 << y
            g[x].append(y)

        # 判斷是否有環 # sub 是項目為兩個的字母
        def has_cycle(sub: int) -> bool:
            color = [0] * 26
            def dfs(x: int) -> bool:
                color[x] = 1
                for y in g[x]:
                    # 只遍歷不在 sub 中的字母
                    if sub >> y & 1:
                        continue
                    if color[y] == 1 or (color[y] == 0 and dfs(y)):
                        return True
                color[x] = 2
                return False

            for i, c in enumerate(color):
                # 只遍歷不在 sub 中的字母
                if c == 0 and (sub >> i & 1) == 0 and dfs(i):
                    return True
            return False

        st = set()
        min_size = inf
        # 枚舉 all_mask 的所有子集 sub
        sub = all_mask # subset
        while True:
            size = sub.bit_count()
            # 剪枝：如果 size > min_size 就不需要判斷了
            if size <= min_size and not has_cycle(sub):
                if size < min_size:
                    min_size = size
                    st.clear()
                st.add(sub)
            sub = (sub - 1) & all_mask
            if sub == all_mask:
                break

        # print([bin(sub) for sub in st])
        return [[(all_mask >> i & 1) + (sub >> i & 1) for i in range(26)] for sub in st]


s = Solution()
# print("ans :",s.supersequences(["ab","ba"])) # "aba" and "bab"
# print("ans :",s.supersequences(["aa","ac"])) # "aac" and "aca", but are the same
# print("ans :",s.supersequences(["aa","bb","cc"])) # "aabbcc"
# print("ans :",s.supersequences(["ab","bc","ca","ae","ef","fa"])) #"a bcef a"
# print("ans :",s.supersequences(["ab","bc","ca","be","ea"])) #"a bce a","c abe c"
print("ans :",s.supersequences(["ab","bc","cd","da","be","ef","fa"])) #"a bcdef a","c dabef c"



