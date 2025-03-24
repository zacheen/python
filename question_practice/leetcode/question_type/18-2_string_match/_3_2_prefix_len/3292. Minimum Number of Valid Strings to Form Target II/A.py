# 3292. Minimum Number of Valid Strings to Form Target II
# https://leetcode.com/problems/minimum-number-of-valid-strings-to-form-target-ii/description/

from typing import List
from math import inf

def LCP(arr) :
    len_arr = len(arr)
    z = [0]*len_arr
    z_box_l = z_box_r = 0
    for i in range(1, len_arr):
        same_len = 0
        if i <= z_box_r :
            same_len = min(z_box_r-i, z[i-z_box_l])
                # z_box_r-i    : 如果 i~z_box_r 全部都一樣，長度會是多少
                # z[i-z_box_l] :  為了排除情況 "aabab"
            # if same_len > 0 : print("fast forward") # 應該要大於1 才會 fast forward
                       # 如果arr還有位置   and r_p 這個位置與 prefix(same_len) 相同
        while (r_p:=i+same_len) < len_arr and arr[same_len] == arr[r_p]:
            same_len += 1
        z[i] = same_len
        if r_p > z_box_r : # 目前 r_p 到更遠的位置 > 更新box
            z_box_l = i
            z_box_r = r_p
    return z

# 回傳 pattern 在 arr 中各個位置 相同prefix的長度
def prefix_len(arr, pattern) :
    concat = pattern + "$" + arr  # 使用 "$" 避免 pattern 影響 arr
    Z = LCP(concat)
    return Z[len(pattern) + 1:]

# my : 2860ms Beats24.56%
class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        min_pre_l = [0]*len(target)
        for s in words :
            min_pre_l = [max(new_l, pre_l) for new_l, pre_l in zip(prefix_len(target, s), min_pre_l)]
        
        pre_e = 0
        end = 1
        ans = 0
        while end <= len(target) :
            next_end = 0
            for i,l in enumerate(min_pre_l[pre_e:end]) :
                if (add_l := i+l) > next_end :
                    next_end = add_l
            if next_end == 0:
                return -1
            next_end += pre_e+1
            pre_e, end = end, next_end
            ans += 1
        return ans

# my v2 : 2894ms Beats24.56%
class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        min_pre_l = [0]*len(target)
        for s in words :
            min_pre_l = [max(new_l, pre_l) for new_l, pre_l in zip(prefix_len(target, s), min_pre_l)]
        
        max_l = 0
        next_l = 0
        ans = 0
        for i,l in enumerate(min_pre_l) :
            next_l = max(next_l, i+l)
            if i >= max_l :
                if max_l == next_l :
                    return -1
                ans += 1
                max_l = next_l
        return ans
    
from collections import defaultdict, deque
# given ans 
class Trie:
    def __init__(self):
        self.c=defaultdict(Trie)
        self.i=0
        self.prev=None
    def add(self, w):
        cur=self
        for i,ch in enumerate(w):
            cur=cur.c[ch]
            cur.i=i+1
    def next(self, ch):
        if ch in self.c: return self.c[ch]
        if not self.prev: return self
        return self.prev.next(ch)
    def aho_corasick(self):
        dq=deque((self, y) for y in self.c.values())
        while dq:
            x,y = dq.popleft()
            y.prev=x
            for ch in y.c: dq.append((x.next(ch), y.c[ch]))
class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        trie=Trie()
        for w in words: trie.add(w)
        trie.aho_corasick()
        n=len(target)
        pre=[0]*n
        for i,ch in enumerate(target):
            trie=trie.next(ch)
            pre[i]=trie.i
        res,i=0, n-1
        while i>=0:
            if pre[i]==0: return -1
            res,i=res+1, i-pre[i]
        return res
        

s = Solution()
print("ans :",s.minValidStrings(words = ["abc","aaaaa","bcdef"], target = "aabcdabc")) # 3
print("ans :",s.minValidStrings(words = ["abababab","ab"], target = "ababaababa")) # 2
print("ans :",s.minValidStrings(words = ["abcdef"], target = "xyz")) # -1
print("ans :",s.minValidStrings(words = ["a","babc"], target = "aacab")) # -1
print("ans :",s.minValidStrings(words = ["babc"], target = "a")) # -1
print("ans :",s.minValidStrings(words = ["cab","bacbbbbcababca","a"], target = "ccbacbbaaa")) # 6
print("ans :",s.minValidStrings(words = ["caacbbbbbcaccb","baccccb","aacabcca"], target = "aacaacbabb")) # 5 : aac, aac, ba, b, b
