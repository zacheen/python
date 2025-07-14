# 2410. Maximum Matching of Players With Trainers
# https://leetcode.com/problems/maximum-matching-of-players-with-trainers

from typing import List
from math import inf

# my 67ms Beats92.52%
class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()

        t_i = 0
        t_end = len(trainers)
        for cnt, p in enumerate(players) :
            while p > trainers[t_i] : 
                t_i += 1
                if t_i == t_end :
                    return cnt
            t_i += 1
            if t_i == t_end :
                return cnt + 1
        return len(players)

s = Solution()
print("ans :",s.matchPlayersAndTrainers(players = [4,7,9], trainers = [8,2,5,8])) # 2
print("ans :",s.matchPlayersAndTrainers(players = [1,1,1], trainers = [10])) # 1
# print("ans :",s.matchPlayersAndTrainers()) # 



