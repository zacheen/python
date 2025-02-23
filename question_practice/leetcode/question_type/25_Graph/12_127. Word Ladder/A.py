# 127. Word Ladder
# https://leetcode.com/problems/word-ladder

from typing import List
from math import inf

from collections import defaultdict

# my 158ms Beats58.23%
    # O(len(wordList)) because used will be removed
# class Solution:
#     def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
#         word_set = set(wordList)
#         if endWord not in word_set :
#             return 0
#         all_c = [chr(n) for n in range(ord('a'), ord('z')+1)]
#         q = [beginWord]
#         ans_cou = 1
#         s_len = len(beginWord)
#         while q :
#             new_q = []
#             for now_w in q :
#                 for i in range(s_len):
#                     fr_s = now_w[:i]
#                     ba_s = now_w[i+1:]
#                     for cha_c in all_c :
#                         poss_w = fr_s + cha_c + ba_s
#                         if poss_w in word_set :
#                             if poss_w == endWord :
#                                 return ans_cou + 1
#                             new_q.append(poss_w)
#                             word_set.remove(poss_w)
#             q = new_q
#             ans_cou += 1
#         return 0

# optimized by given ans : always do the smaller part : 19ms Beats99.94%
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set :
            return 0
        all_c = [chr(n) for n in range(ord('a'), ord('z')+1)]
        ans_cou = 1
        s_len = len(beginWord)
        q_big = set([endWord])
        q_sma = set([beginWord])
        while q_big and q_sma :
            new_q = set()
            word_set -= q_sma
            for now_w in q_sma :
                if now_w in q_big :
                    return ans_cou
                for i in range(s_len):
                    fr_s = now_w[:i]
                    ba_s = now_w[i+1:]
                    for cha_c in all_c :
                        poss_w = fr_s + cha_c + ba_s
                        if poss_w in word_set :
                            new_q.add(poss_w)
            if len(new_q) < len(q_big):
                q_sma = new_q
            else :
                q_sma, q_big = q_big, new_q
            ans_cou += 1
        return 0

# using method like "433. Minimum Genetic Mutation" would be Time Limit Exceeded 
    # because the links amount might attain 25*10**6
# class Solution:
#     def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
#         li = defaultdict(list)
#         for i, s1 in enumerate(wordList):
#             for s2 in wordList[:i] :
#                 if sum(c1 != c2 for c1,c2 in zip(s1,s2)) == 1 :
#                     li[s1].append(s2)
#                     li[s2].append(s1)

#         q = []
#         seen = set()
#         for b in wordList :
#             if sum(c1 != c2 for c1,c2 in zip(b,beginWord)) == 1 :
#                 q.append(b)
#                 seen.add(b)
        
#         ans_cou = 2
#         while q :
#             new_q = []
#             for now_g in q :
#                 if now_g == endWord :
#                     return ans_cou
#                 seen.add(now_g)
#                 for next_g in li[now_g] :
#                     if next_g not in seen :
#                         new_q.append(next_g)
#             q = new_q
#             ans_cou += 1
#         return 0

s = Solution()
# print("ans :",s.ladderLength(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"])) # 5
# print("ans :",s.ladderLength(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"])) # 0
print("ans :",s.ladderLength(beginWord = "hog", endWord = "cog", wordList = ["cog"])) # 2



