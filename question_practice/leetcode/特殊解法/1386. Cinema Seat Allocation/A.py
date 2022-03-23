# # My Memory Limit Exceeded
# class Solution(object):
#     def maxNumberOfFamilies(self, n, reservedSeats):
#         reservedSeats.sort(key = lambda x : x[0])
#         # print(reservedSeats)

#         ans = 0
#         reserve_indx = 0
#         for i in range(1,n+1) :
#             reserve = []
#             while reserve_indx < len(reservedSeats) and reservedSeats[reserve_indx][0] == i : 
#                 reserve.append(reservedSeats[reserve_indx][1])
#                 reserve_indx += 1
#             print(i, reserve)
#             if len({4,5} & set(reserve)) == 0 :
#                 # 45 沒人坐
#                 if len({2,3} & set(reserve)) == 0 :
#                     ans += 1
#                     if len({6,7,8,9} & set(reserve)) == 0 :
#                         ans += 1
#                 else :
#                     if len({6,7} & set(reserve)) == 0 :
#                         ans += 1
#             else :
#                 if len({6,7,8,9} & set(reserve)) == 0 :
#                     ans += 1

#         return ans

# My v2 還是 Memory Limit Exceeded
# 應該是垃圾回收機制有問題
# class Solution(object):
#     def maxNumberOfFamilies(self, n, reservedSeats):
#         from collections import defaultdict
#         hash_table = defaultdict(set)
#         for each_seat in reservedSeats :
#             hash_table[each_seat[0]].add(each_seat[1])

#         ans = 0
#         reserve_indx = 0
#         for i in range(1,n+1) :
#             reserve = hash_table[i]
#             if len({4,5} & reserve) == 0 :
#                 # 45 沒人坐
#                 if len({2,3} & reserve) == 0 :
#                     ans += 1
#                     if len({6,7,8,9} & reserve) == 0 :
#                         ans += 1
#                 else :
#                     if len({6,7} & reserve) == 0 :
#                         ans += 1
#             else :
#                 if len({6,7,8,9} & reserve) == 0 :
#                     ans += 1

#         return ans

# My v3 判斷空位換寫法
# 還是 Memory Limit Exceeded ... 不是跟下面的寫法相同嗎?
# 這個是關鍵
# ans = (n - len(hash_table))*2
# for i in hash_table:
# Runtime: 629 ms, faster than 62.28% of Python
class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        from collections import defaultdict
        hash_table = defaultdict(set)
        for each_seat in reservedSeats :
            hash_table[each_seat[0]].add(each_seat[1])

        ans = (n - len(hash_table))*2
        for i in hash_table:
            left = True
            middle = True
            right = True
            for each_reserve in hash_table[i] :
                if each_reserve in [2,3,4,5] :
                    left = False
                elif each_reserve in [6,7,8,9] :
                    right = False
                if each_reserve in [4,5,6,7] :
                    middle = False

            if left and right :
                ans += 2
            elif left or right or middle :
                ans += 1
        return ans

# given ans 
# class Solution:
#     def maxNumberOfFamilies(self, n, reservedSeats):
#         dic = collections.defaultdict(list)
#         for row, column in reservedSeats:
#             dic[row].append(column)
#         # 這裡有優化一下 就不用range全部的排數
#         res = (n - len(dic))*2
#         for row in dic:
#             left = 1 # the four seats from 2 to 5
#             middle = 1# the four seats from 4 to 7
#             right = 1## the four seats from 6 to 9
#             for i in dic[row]:
#                 if i in [2,3,4,5]:
#                     left = 0
#                 if i in [4,5,6,7]:
#                     middle = 0
#                 if i in [6,7,8,9]:
#                     right = 0
#             if left == 1 and middle == 1 and right == 1:
#                 res += 2
#             elif left == 1 or middle == 1 or right == 1:
#                 res += 1
#         return res

# given ans 
# class Solution:
#     def maxNumberOfFamilies(self, n, reservedSeats):
#         left, right, mid = set(), set(), set()
#         count = 0
        
#         # 統計被預約的位置
#         for r, c in reservedSeats:
#             if r in left and r in right and r in mid:
#                 continue
#             if c < 6 and c > 1:
#                 left.add(r)
#             if c < 10 and c > 5:
#                 right.add(r)
#             if c < 8 and c > 3:
#                 mid.add(r)
#         for i in (left|right|mid):
#             # 預約位置在兩邊：1 or 10
#             if i not in left and i not in right:
#                 count += 2
#             # 預約位置在左邊/右邊：2 or 3 or 8 or 9
#             elif i not in mid:
#                 count += 1
#             # 預約位置在中間：4 or 5 or 6 or 7
#             elif i not in left or i not in right:
#                 count += 1
#         # 反向篩選一下，沒有被預約的行最多可以坐兩家人
#         count += 2*(n - len(left|right|mid))
#         return count

s = Solution()
print(s.maxNumberOfFamilies(4,[[4,3],[1,4],[4,6],[1,7]]))
# print(s.maxNumberOfFamilies(3,[[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]))
