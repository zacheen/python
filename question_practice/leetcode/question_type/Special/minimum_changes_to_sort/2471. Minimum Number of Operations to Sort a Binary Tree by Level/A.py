# 2471. Minimum Number of Operations to Sort a Binary Tree by Level
# https://leetcode.com/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/description

from typing import List
import functools

# my opt 124ms Beats99.35%
class Solution:
    def minimumOperations(self, root) -> int:
        total_swaps = 0
        # Process tree level by level using BFS
        last_level = [root]
        while last_level :
            next_level = []
            level_values = []
            for p in last_level :
                level_values.append(p.val)
                if p.left != None :
                    next_level.append(p.left)
                if p.right != None :
                    next_level.append(p.right)
            last_level = next_level
            
            # Add minimum swaps needed for current level
            target = sorted(level_values)
            # Map to track current positions of values
            pos = {val: idx for idx, val in enumerate(level_values)}
            # For each position, swap until correct value is placed
            for i, target_n in enumerate(target):
                if level_values[i] != target_n:
                    total_swaps += 1
                    # Update position of swapped values
                    # 只改後面的 因為前面已經搞定
                    pos[level_values[i]] = pos[target_n]
                    level_values[pos[target_n]] = level_values[i]
        return total_swaps

# my 151ms Beats65.36%
class Solution:
    def minimumOperations(self, root) -> int:
        ans_cou = 0
        last_level = [root]
        while last_level :
            next_level = []
            level_list = []
            for i, p in enumerate(last_level) :
                level_list.append([p.val, i])
                if p.left != None :
                    next_level.append(p.left)
                if p.right != None :
                    next_level.append(p.right)
            level_list.sort(key=lambda x : x[0])
            level_list = [ i for _,i in level_list ]
            # print("level_list :", level_list)
            for i, c in enumerate(level_list):
                while i != c :
                    level_list[i], level_list[c] = level_list[c], level_list[i]
                    ans_cou += 1
                    c = level_list[i]
            last_level = next_level
        return ans_cou

# given ans
# same concept, but _get_min_swaps much faster than mine
from collections import deque
class Solution:
    def minimumOperations(self, root) -> int:
        queue = deque([root])
        total_swaps = 0
        # Process tree level by level using BFS
        while queue:
            level_size = len(queue)
            level_values = []
            # Store level values and add children to queue
            for _ in range(level_size):
                node = queue.popleft()
                level_values.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # Add minimum swaps needed for current level
            total_swaps += self._get_min_swaps(level_values)
        return total_swaps

    # Calculate minimum swaps needed to sort an array
    def _get_min_swaps(self, original: list) -> int:
        swaps = 0
        target = sorted(original)
        # Map to track current positions of values
        pos = {val: idx for idx, val in enumerate(original)}
        # For each position, swap until correct value is placed
        for i in range(len(original)):
            if original[i] != target[i]:
                swaps += 1
                # Update position of swapped values
                cur_pos = pos[target[i]]
                pos[original[i]] = cur_pos
                original[cur_pos] = original[i]
        return swaps



s = Solution()
print("ans :",s.minimumOperations()) # 



