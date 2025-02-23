# 841. Keys and Rooms
# https://leetcode.com/problems/keys-and-rooms

from typing import List
from math import inf

# my 
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        seen = [False]*len(rooms)
        dfs_stack = [0]
        while dfs_stack :
            next_n = dfs_stack.pop()
            if not seen[next_n] :
                seen[next_n] = True
                dfs_stack += rooms[next_n]
        # print(seen)
        return all(seen)

s = Solution()
print("ans :",s.canVisitAllRooms(rooms = [[1,3],[3,0,1],[2],[0]])) # F



