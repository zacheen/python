# calculate all result / permutation amount
# this mostly fit counting items has the same result, with one for loop
    # like how many pairs, has the same result after % target

from collections import Counter

l = [4,6,5,5,3,7,2,8,1,13]
# like how many pairs, has the same result after % target 
def cou_pairs(l, target) :
    cou = Counter(n%target for n in l)
    print("cou :", cou)
    return sum(cou_num*(cou_num-1) for cou_num in cou.values() if cou_num > 1) // 2

print(cou_pairs(l, 5))
# (6,1), (5,5), (7,2), (3,8), (8,13), (3,13)

# classic : # 2364. Count Number of Bad Pairs
# https://leetcode.com/problems/count-number-of-bad-pairs/description