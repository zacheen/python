#!/bin/python3

import math
import os
import random
import re
import sys
import bisect

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    # Write your code here
    rank_pos = [(ranked[0],1)]
    pos = 2
    for rank in ranked :
        if rank != rank_pos[-1][0] :
            rank_pos.append((rank, pos))
            pos += 1
    rank_pos.append((-1, pos))
    rank_pos.reverse()
    print(rank_pos)
    ret = []
    for p in player :
        if p >= rank_pos[-1][0] :
            ret.append(1)
            continue
        
        indx = bisect.bisect_left(rank_pos, (p,math.inf))
        print(p, indx)
        if rank_pos[indx][0] == p :
            ret.append(rank_pos[indx][1])
        else :
            ret.append(rank_pos[indx][1] + 1 )
    return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
