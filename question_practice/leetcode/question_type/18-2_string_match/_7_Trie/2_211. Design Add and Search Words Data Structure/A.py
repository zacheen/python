# 211. Design Add and Search Words Data Structure
# https://leetcode.com/problems/design-add-and-search-words-data-structure/description/

# my, using template v1 : 658ms Beats98.72%
class WordDictionary:
    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        now_n = self.root
        for c in word :
            if c not in now_n :
                now_n[c] = {}
            now_n = now_n[c]
        now_n[None] = None

    def search(self, word: str) -> bool:
        len_w = len(word)
        def dfs(now_i, now_n):
            if now_i == len_w :
                return None in now_n
            c = word[now_i]
            if c == "." :
                # print(now_n.values())
                for next_n in now_n.values():
                    if next_n != None and dfs(now_i+1, next_n) :
                        return True
                return False
            else :
                if c not in now_n :
                    return False
                return dfs(now_i+1, now_n[c])
        return dfs(0, self.root)
