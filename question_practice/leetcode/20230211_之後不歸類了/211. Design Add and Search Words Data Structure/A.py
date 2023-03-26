# my Beats 14.53%
class WordDictionary:
    def __init__(self):
        self.mem = defaultdict(bool)

    def addWord(self, word):
        # if word == "" :
        #     mem[""] = True
        #     return 
        
        go_into = self.mem

        for c in word :
            if go_into[c] == False :
                go_into[c] = defaultdict(bool)
            go_into = go_into[c]
        
        go_into["End"] = True

    def search(self, word):
        # if word == "" :
        #     return mem[""]
        
        stack = [self.mem]
        for c in word :
            # print("c : ",c)
            new_stack = []
            for go_into in stack :
                if c == "." :
                    ret_val = list(go_into.values())
                    # print("ret_val :",ret_val)
                    ret_val = [x for x in ret_val if type(x) is defaultdict]
                    new_stack = new_stack + ret_val
                else :
                    ret = go_into[c]
                    # print(ret)
                    if ret :
                        new_stack.append(ret)
            stack = new_stack
            # print(stack)

        # print(word, stack)
        for go_into in stack : 
            if go_into['End'] :
                return True
        return False

# given ans 
# 看起來想法跟我一樣
    # 不過改成使用 DFS (我的現在是 BFS)
# 果然 : Beats 21.70%
    # 雖然有點慢，但我看網路上的方法都是這樣
    # 就先這樣八
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root
        for c in word:
            node = node.children.setdefault(c, TrieNode())
        node.isWord = True

    def search(self, word):
        return self._dfs(word, 0, self.root)

    def _dfs(self, word, s, node):
        if s == len(word):
            return node.isWord
        if word[s] != '.':
            child = node.children.get(word[s], None)
            return self._dfs(word, s + 1, child) if child else False
        return any(self._dfs(word, s + 1, child) for child in node.children.values())

s = Solution()
# print(s.())



