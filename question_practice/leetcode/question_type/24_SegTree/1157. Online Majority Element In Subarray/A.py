# 1157. Online Majority Element In Subarray
# https://leetcode.com/problems/online-majority-element-in-subarray/description/

from typing import List
from math import inf

# given ans
from collections import defaultdict
from bisect import bisect_left, bisect_right

class Node:
    """
    區段樹節點的結構。
    x: 候選多數元素的值。
    y: 候選元素的計數。
    """
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        """
        模擬 C++ 中的 operator+，用於合併兩個區段樹節點。
        這實作了 Boyer-Moore 多數投票演算法的合併邏輯。
        """
        t = Node()
        if self.x == other.x:
            # 如果兩個節點的候選值相同，則計數相加
            t.x = self.x
            t.y = self.y + other.y
        elif self.y < other.y:
            # 如果第一個節點的計數較少，則取第二個節點的候選值，並減去第一個節點的計數
            t.x = other.x
            t.y = other.y - self.y
        else:
            # 如果第二個節點的計數較少，則取第一個節點的候選值，並減去第二個節點的計數
            t.x = self.x
            t.y = self.y - other.y
        return t

class MajorityChecker:
    """
    MajorityChecker 類別，用於查詢給定範圍內是否存在多數元素。
    它使用區段樹來快速找到候選元素，並使用預儲存的索引來驗證計數。
    """
    def __init__(self, arr: list[int]):
        self.n = len(arr)
        self.arr = arr
        # self.pos_map 儲存每個值在原始陣列中出現的所有索引，按升序排列
        # 例如: {value: [index1, index2, ...]}
        self.pos_map = defaultdict(list)
        for i, num in enumerate(arr):
            self.pos_map[num].append(i)

        # 區段樹陣列，大小約為 4 * n
        # 初始化所有節點為預設的 Node(0, 0)
        self.tree = [Node() for _ in range(4 * self.n)]
        
        # 建構區段樹
        self._build(1, 0, self.n - 1)

    def _build(self, r_idx: int, l: int, r: int):
        """
        遞迴建構區段樹。
        r_idx: 當前節點在 self.tree 陣列中的索引。
        l, r: 當前節點所代表的範圍 [l, r]。
        """
        if l == r:
            # 葉子節點：其候選值為陣列中的實際元素，計數為 1
            self.tree[r_idx] = Node(self.arr[l], 1)
            return

        mid = (l + r) // 2
        # 遞迴建構左子樹
        self._build(2 * r_idx, l, mid)
        # 遞迴建構右子樹
        self._build(2 * r_idx + 1, mid + 1, r)
        
        # 合併左右子節點的結果到當前節點
        self.tree[r_idx] = self.tree[2 * r_idx] + self.tree[2 * r_idx + 1]

    def _ask(self, r_idx: int, l: int, r: int, query_l: int, query_r: int) -> Node:
        """
        遞迴查詢區段樹以找出給定範圍 [query_l, query_r] 的多數候選元素。
        r_idx: 當前節點在 self.tree 陣列中的索引。
        l, r: 當前節點所代表的範圍 [l, r]。
        query_l, query_r: 查詢的目標範圍。
        """
        # 如果當前節點的範圍完全包含在查詢範圍內，直接返回當前節點的結果
        if query_l == l and r == query_r:
            return self.tree[r_idx]

        mid = (l + r) // 2
        # 如果查詢範圍完全位於左子樹
        if query_r <= mid:
            return self._ask(2 * r_idx, l, mid, query_l, query_r)
        # 如果查詢範圍完全位於右子樹
        if query_l > mid:
            return self._ask(2 * r_idx + 1, mid + 1, r, query_l, query_r)
        
        # 如果查詢範圍跨越左右子樹，則分別查詢左右子樹並合併結果
        left_result = self._ask(2 * r_idx, l, mid, query_l, mid)
        right_result = self._ask(2 * r_idx + 1, mid + 1, r, mid + 1, query_r)
        return left_result + right_result

    def query(self, left: int, right: int, threshold: int) -> int:
        """
        查詢在 [left, right] 範圍內是否存在一個元素，其出現次數大於或等於 threshold。
        如果存在，返回該元素；否則返回 -1。
        """
        # 使用區段樹查詢範圍 [left, right] 的候選多數元素
        candidate_node = self._ask(1, 0, self.n - 1, left, right)
        ans = candidate_node.x

        # 檢查候選元素是否存在於 pos_map 中，以及其在 pos_map 中的索引列表是否為空
        # (因為 Node 預設值為 0，如果 ans 為 0 但原始陣列中沒有 0，可能會導致錯誤)
        if ans not in self.pos_map or not self.pos_map[ans]:
            return -1

        # 使用 bisect_left 和 bisect_right 在預儲存的索引列表中計算候選元素在 [left, right] 範圍內的出現次數
        # bisect_left 找到第一個大於或等於 left 的索引
        start_idx = bisect_left(self.pos_map[ans], left)
        # bisect_right 找到第一個大於 right 的索引
        end_idx = bisect_right(self.pos_map[ans], right)
        
        # 計算出現次數
        count = end_idx - start_idx

        # 如果出現次數達到或超過閾值，返回候選元素，否則返回 -1
        if count >= threshold:
            return ans
        else:
            return -1




