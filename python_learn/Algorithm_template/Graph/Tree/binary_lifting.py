# binary lifting (倍增算法)
    # 記錄 [父節點, 父節點的父節點, (父節點)**4, (父節點)**8...] 是誰
    # 這樣找 kth_ancestor 就可以在 O(logn) 的時間內做到
        # 例如 k = 13 = 往上1+往上4+往上8

class binary_lifting :
    def __init__(self, edges):
        self.len_n = len_n = len(edges) +1

        # 建構 parents (一個 child 只能有一個 father)
        parents = [-1]*len_n
        TODO

        # 把回到自己的路徑設成-1 (binary lifting 才不會出錯)
        for st, end in enumerate(parents):
            if st == end :
                parents[st] = -1

        # 建構 倍增演算法(binary lifting)
        self.max_bit_len = max_bit_len = len_n.bit_length()
        bin_lift = [parents]+[[-1]*len_n for _ in range(max_bit_len)]
        # bin_lift[parent_lv][node]
        now_lv = bin_lift[0]
        for lv in range(1, max_bit_len+1):
            next_lv = bin_lift[lv]
            for node in range(len_n):
                if (par:=now_lv[node]) == -1: continue
                next_lv[node] = now_lv[par]
            now_lv = next_lv
        self.bin_lift = bin_lift
    
    def upto(self, st, limit):
        dis_cou = 0
        for shift in range(self.max_bit_len-1,-1,-1):
            next_node = self.bin_lift[shift][st]
            if next_node != -1 and COND < limit:
                st = next_node
                dis_cou += 1 << shift
        return dis_cou, st
        # st : 最後符合的node, dis_cou : 最後符合的node 與 st 的距離

    def get_kth_ancestor(self, node, k):
        for shift in range(k.bit_length()):
            if k >> shift & 1:
                node = self.bin_lift[shift][node]
                # if node == -1: # 如果常常超出再開
                #     break
        return node
    
# 還有一種是把 -1 改成 len_n
# 參考
    # 3464. Maximize the Distance Between Points on a Square
    # https://leetcode.com/problems/maximize-the-distance-between-points-on-a-square/description/
