# TreeAncestor 記錄了各個節點之間的關係

# classic
    # get_kth_ancestor
        # 1483. Kth Ancestor of a Tree Node
        # https://leetcode.com/problems/kth-ancestor-of-a-tree-node
    # get_dist
        # 3559. Number of Ways to Assign Edge Weights II
        # https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-ii
    # upto_dist
        # 3585. Find Weighted Median Node in Tree
        # https://leetcode.com/problems/find-weighted-median-node-in-tree
    # get_lca (Lowest Common Ancestor)
        # 

class TreeAncestor:
    def __init__(self, edges):
        len_n = len(edges)+1
        self.max_bit_len = max_bit_len = len_n.bit_length()
        li = [[] for _ in range(len_n)]
        for x, y, w in edges:
            li[x].append((y, w))
            li[y].append((x, w))

        parent = [-1]*len_n
        depth = [0]*len_n  # 此 node 在第幾層
        dist = [0]*len_n   # 從 root 到 node 的 weight 總和
        root_num = 0
        stack = [root_num]
        while stack:
            u = stack.pop()
            for v,w in li[u]:
                if v == parent[u]: continue
                parent[v] = u
                depth[v] = depth[u]+1
                dist[v]=dist[u]+w
                stack.append(v)

        self.depth = depth
        self.dist = dist
        self.bin_lift = [parent]+[[-1]*len_n for _ in range(max_bit_len)]
        # bin_lift[parent_lv][node]
		# 用來記錄 [父節點, 父節點的父節點, (父節點)**4, (父節點)**8...] 是誰
            # 這樣找 kth_ancestor 就可以在 O(logn) 的時間內做到
                # 例如 k = 13 = 往上1+往上4+往上8
        now_lv = self.bin_lift[0]
        for lv in range(1, max_bit_len+1):
            next_lv = self.bin_lift[lv]
            for node in range(len_n):
                if (par:=now_lv[node]) == -1: continue
                next_lv[node] = now_lv[par]
            now_lv = next_lv

    def get_kth_ancestor(self, node: int, k: int) -> int:
        for shift in range(k.bit_length()):
            if k >> shift & 1:
                node = self.bin_lift[shift][node]
                # if node == -1: # 如果常常超出再開
                #     break
        return node

    # 返回 x和y 的最近公共祖先
    def get_lca(self, x, y):
        if self.depth[x] > self.depth[y]:
            x, y = y, x
        y = self.get_kth_ancestor(y, self.depth[y] - self.depth[x])
        if y == x:
            return x
        for i in range(self.depth[y].bit_length()-1, -1, -1):
            px, py = self.bin_lift[i][x], self.bin_lift[i][y]
            if px != py:
                x, y = px, py  # 同時往上找前 2**i 個父node
        return self.bin_lift[0][x]

    # # 如果已經知道 x和y 在同一條路徑上，不應該呼叫此function，而是直接在程式中計算
    def get_dist(self, x: int, y: int, lca = None) -> int:
        if lca == None: lca = self.get_lca(x, y)
        return self.dist[x] + self.dist[y] - self.dist[lca]*2
    
    def upto_dist_in(self, st, dist): # include
        dist_2_st = self.dist[st]
        for shift in range(self.depth[st].bit_length()-1,-1,-1):
            next_node = self.bin_lift[shift][st]
            if next_node != -1 and (dist_2_st-self.dist[next_node]) <= dist:
                st = next_node
        return st

    def upto_dist_not_in(self, st, dist): # include
        dist_2_st = self.dist[st]
        for shift in range(self.depth[st].bit_length()-1,-1,-1):
            next_node = self.bin_lift[shift][st]
            if next_node != -1 and (dist_2_st-self.dist[next_node]) < dist:
                st = next_node
        return st
    
    def over_dist(self, st, dist): # 要 over 所以當然不包含此點
        return self.bin_lift[0][self.upto_dist_not_in(st, dist)]

# 點跟點之間沒有 weight 或 cost
class TreeAncestor_no_weight:
    def __init__(self, edges):
        root_num = 0
        len_n = len(edges)+root_num
        self.max_bit_len = max_bit_len = len_n.bit_length()
        li = [[] for _ in range(len_n)]
        for x, y in edges:
            li[x].append(y)
            li[y].append(x)

        parent = [-1]*len_n
        depth = [0]*len_n  # 此 node 在第幾層
        
        stack = [root_num]
        while stack:
            u = stack.pop()
            for v in li[u]:
                if v == parent[u]: continue
                parent[v] = u
                depth[v] = depth[u]+1
                stack.append(v)

        self.depth = depth
        self.bin_lift = [parent]+[[-1]*len_n for _ in range(max_bit_len)]
        # bin_lift[parent_lv][node]
		# 用來記錄 [父節點, 父節點的父節點, (父節點)**4, (父節點)**8...] 是誰
            # 這樣找 kth_ancestor 就可以在 O(logn) 的時間內做到
                # 例如 k = 13 = 往上1+往上4+往上8
        now_lv = self.bin_lift[0]
        for lv in range(1, max_bit_len+1):
            next_lv = self.bin_lift[lv]
            for node in range(len_n):
                if (par:=now_lv[node]) == -1: continue
                next_lv[node] = now_lv[par]
            now_lv = next_lv

    # def __init__(self, parent):
    #     len_n = len(parent)
    #     self.max_bit_len = max_bit_len = len_n.bit_length()
    #     li = [[] for _ in range(len_n)]
    #     for x, y in enumerate(parent) :
    #         if y == -1 : continue
    #         li[x].append(y)
    #         li[y].append(x)

    #     depth = [0]*len_n  # 此 node 在第幾層
    #     root_num = 0
    #     stack = [root_num]
    #     while stack:
    #         u = stack.pop()
    #         for v in li[u]:
    #             if v == parent[u]: continue
    #             depth[v] = depth[u]+1
    #             stack.append(v)

    #     self.depth = depth
    #     self.bin_lift = [parent]+[[-1]*len_n for _ in range(max_bit_len)]

    #     now_lv = self.bin_lift[0]
    #     for lv in range(1, max_bit_len+1):
    #         next_lv = self.bin_lift[lv]
    #         for node in range(len_n):
    #             if (par:=now_lv[node]) == -1: continue
    #             next_lv[node] = now_lv[par]
    #         now_lv = next_lv

    def get_kth_ancestor(self, node: int, k: int) -> int:
        for shift in range(k.bit_length()):
            if k >> shift & 1:
                node = self.bin_lift[shift][node]
                if node == -1: # 如果常常超出再開
                    break
        return node

    # 返回 x和y 的最近公共祖先
    def get_lca(self, x, y):
        if self.depth[x] > self.depth[y]:
            x, y = y, x
        y = self.get_kth_ancestor(y, self.depth[y] - self.depth[x])
        if y == x:
            return x
        for i in range(self.depth[y].bit_length()-1, -1, -1):
            px, py = self.bin_lift[i][x], self.bin_lift[i][y]
            if px != py:
                x, y = px, py  # 同時往上找前 2**i 個父node
        return self.bin_lift[0][x]

    # # 如果已經知道 x和y 在同一條路徑上，不應該呼叫此function，而是直接在程式中計算
    def get_dist(self, x: int, y: int, lca = None) -> int:
        if lca == None: lca = self.get_lca(x, y)
        return self.depth[x] + self.depth[y] - self.depth[lca]*2