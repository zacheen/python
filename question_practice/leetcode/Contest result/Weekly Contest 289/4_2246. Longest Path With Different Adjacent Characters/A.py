# my Runtime: 1814 ms, faster than 100.00% of Python3
# 就差一點點就能解出來... 上一題coding很久 要不然就四題 
class Solution:
    def longestPath(self, parent, s):
        connect = defaultdict(list)
        
        for indx, p in enumerate(parent) :
            connect[p].append(indx)
            
        # 這個點後面最長的長度, 上一個點(因為只要跟上一個點不一樣路線就不會重複)
        mem = [0]*len(parent)
        def make_mem(node):
            max_len_1 = 0
            max_len_2 = 0
            for p in connect[node] :
                # print(p)
                # 紀錄最長的兩條 這個點最長的路徑就是 這兩條的長度+1(自己)
                # 回傳給 parent 就是回傳 最長的那一條+自己
                ret = make_mem(p)
                if s[p] != s[node] :
                    max_len_2 = max(max_len_2, ret)
                    if max_len_2 > max_len_1 :
                        max_len_2, max_len_1 = max_len_1, max_len_2
            mem[node] = max_len_1 + max_len_2 + 1
            return max_len_1 + 1
        
        make_mem(0)
        return max(mem)

# given ans 概念是一樣的
# 只是寫的方法不一樣 不過效能差不多
# 因為沒人用python寫 就不優化了 

s = Solution()
print(s.longestPath(parent = [-1,0,0,1,1,2], s = "abacbe"))
print(s.longestPath(parent = [-1,0,0,0], s = "aabc"))



