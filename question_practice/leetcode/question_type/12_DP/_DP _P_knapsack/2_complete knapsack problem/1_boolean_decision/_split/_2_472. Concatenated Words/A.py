# 472. Concatenated Words
# https://leetcode.com/problems/concatenated-words
    
# my, using template Trie and C_Knap_reach : 255ms Beats36.48%
class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word):
        now_n = self.root
        for c in word :
            if c not in now_n :
                now_n[c] = {}
            now_n = now_n[c]
        now_n[None] = None
    
    def find_all_len(self, prefix) :
        ret = []
        now_n = self.root
        for l, c in enumerate(prefix, 1) :
            if c not in now_n :
                return ret
            now_n = now_n[c]
            if None in now_n :
                ret.append(l)
        return ret
class Solution:
    def findAllConcatenatedWordsInADict(self, words):
        trie = Trie()
        words.sort(key = len)
        ans = []
        for w in words :
            dp=[True] + [False]*len(w)
            for i in range(len(dp)-1) :
                if dp[i] :
                    for n in trie.find_all_len(w[i:]) :
                        dp[i+n] = True
                if dp[-1] :
                    ans.append(w)
                    break
            trie.insert(w)
        return ans

s = Solution()
print(s.findAllConcatenatedWordsInADict(["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]))
print(s.findAllConcatenatedWordsInADict(["rfkqyuqfjkx","vnrtysfrzrmzl"]))
print(s.findAllConcatenatedWordsInADict(["a","b","c","d","af","abc","acb","aca","afd","adbc"]))


