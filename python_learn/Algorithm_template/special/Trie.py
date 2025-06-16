# Trie

# v1 : easier to read
class Trie_node:
    def __init__(self):
        self.next = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = Trie_node()

    def insert(self, word):
        now_n = self.root
        for c in word :
            if c not in now_n.next :
                now_n.next[c] = Trie_node()
            now_n = now_n.next[c]
        now_n.end = True
        # now_n.next[last_c].end = True

    # None : return at the middle
    # else : return the end node
    def find_end(self, prefix) :
        now_n = self.root
        for c in prefix :
            if c not in now_n.next :
                return None
            now_n = now_n.next[c]
        return now_n

    def search(self, word: str) -> bool:
        ret = self.find_end(word)
        return ret!=None and ret.end

    def startsWith(self, prefix: str) -> bool:
        return self.find_end(prefix) != None

# v2 (faster)
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

    # None : return at the middle
    # else : return the end node
    def find_end(self, prefix) :
        now_n = self.root
        for c in prefix :
            if c not in now_n :
                return None
            now_n = now_n[c]
        return now_n
    
    def find_end_dfs(self, prefix) :
        def dfs(now_n, now_i, STATUS):
            if now_i == len(prefix) :
                return (STATUS and None in now_n)
        
            now_c = prefix[now_i]
            # not same 
            if STATUS :
                for c, next_n in now_n.items() :
                    if c == now_c : continue
                    if next_n != None and dfs(next_n, now_i+1, STATUS):
                        return True
            # same
            if now_c in now_n :
                return dfs(now_n[now_c], now_i+1, STATUS)
            return False
    
    ## not necessary ####################################
    def search(self, word: str) -> bool:
        ret = self.find_end(word)
        return None != ret and None in ret

    def startsWith(self, prefix: str) -> bool:
        return self.find_end(prefix) != None
    
    # def dfs_2_end(self):
    #     STATUS
    #     def dfs(now_n) :
    #         if len(now_n) == 0 :
    #             # Reach end
    #             # do something
    #             STATUS
    #         for next_n in now_n.values() :
    #             dfs(next_n)
    #     dfs(self.root)
    #     return STATUS

    

# classic 208. Implement Trie (Prefix Tree)
# https://leetcode.com/problems/implement-trie-prefix-tree/description/
