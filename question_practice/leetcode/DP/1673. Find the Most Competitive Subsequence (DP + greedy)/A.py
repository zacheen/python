# 1673 https://leetcode.com/problems/find-the-most-competitive-subsequence/description/

# 這一題我想法錯很多次 每次的做法都有漏洞
# 我要如何確保我的想法是對的 ?? 
# 我要如何找到最簡單的做法去做 ?? 

# class Solution(object):
#     def mostCompetitive(self, nums, k):
#         ans = [None] * k
#         n = len(nums)
#         c = 0 # 新數字要塞入的位置
#         for i, x in enumerate(nums):
#             # c 確保不會跳錯
#             # ans[c - 1] > x  如果目前 ans 的最後一位數字 > 新的數字
#             # c + n - i - 1 >= k 我猜是確保 新的數字 長度夠塞入
#             while c and ans[c - 1] > x and c + n - i - 1 >= k:
#                 c -= 1
#                 print("c :",c)
#             # 如果還有空位就要塞入新的數值
#             if c < k: 
#                 ans[c] = x
#                 print(ans)
#                 c += 1
#                 print("c :",c)
#         return ans

# # 2022 05 17 重新練習
# # Time Limit Exceeded
# class Solution:
#     def mostCompetitive(self, nums: List[int], k: int):
#         # 從頭開始掃 如果長度允許就整個替換掉
        
#         i = 1
#         now_list = [nums[0]]
        
#         while i < len(nums) :
#             new_num = nums[i]
#             # print(i, new_num, now_list)
#             have_small = False
#             for ii, this_n in enumerate(now_list) :
#                 # print(this_n , new_num, len(nums)-i, k - ii)
#                 if new_num < this_n and (len(nums)-i) >= (k - ii) :
#                     # len(nums)-i代表nums還有幾個字    k-ii 代表now_list後面所需的長度
#                     now_list = now_list[:ii] + [new_num]
#                     have_small = True
#                     break
#             if not have_small :
#                 now_list.append(new_num)
#             i+=1
#         # print(now_list)
#         return now_list[:k]

# Runtime: 1547 ms, faster than 70.82% of Python3
# 邏輯
# 只要是遞增的數字 就放進 List (反正最後再裁就好)
class Solution:
    def mostCompetitive(self, N, K):
        i, moves = 0, len(N) - K
        # print(moves)
        ans = []
        for x in N:
            # moves 計算 目前ans+N剩下的長度夠不夠
                # moves 也可以說是最多可以移除幾個字母
                # 每移除一個字就減一
            # 跟 2022 05 17 的想法一樣
            # 只是這裡的處理方式更好 (O)
            # 為什麼沒辦法一開始就想到呢?
                # 因為我想到前面是遞增的 list
            while ans and moves and x < ans[-1]:
                ans.pop()
                # print(ans)
                moves -= 1
                # print(moves)
            ans.append(x)
            # print(ans)
        return ans[:K]  # 把多餘的遞增數字移除

# # 方便理解版本 
# class Solution:
#     def mostCompetitive(self, N, K):
#         ans = []
#         for n, remain in zip(N, range(len(N),-1,-1)) :
#             while remain + len(ans) > K and ans and n < ans[-1] :
#                 ans.pop()
#             ans.append(n)
#         return ans[:K]

# 2024 12 06 重新練習
# Time Limit Exceeded
# worst case has the same time complexity, but I estimate average time complexity is lower...
    # I believe the problem is algorithm to complex, so while calculating, many time wasted
    # also the situation optimize is a long increasing number, but maybe it seldom happen
# import bisect
# class Solution:
#     def mostCompetitive(self, N, K):
#         ans = [1000000001]
#         smallest_indx_list = [0,0]
#         for n_indx, n in enumerate(N) :
#             mem_find_place = False
#             for s_indx in range(len(smallest_indx_list)-1) :
#                 sta = smallest_indx_list[s_indx]
#                 en = smallest_indx_list[s_indx+1]
#                 if n < ans[en] :
#                     mem_find_place = True
#                     # 找到可以插入的位置
#                     insert_indx = bisect.bisect_right(ans, n, lo=sta, hi=en+1)
#                     # print("insert :", n, sta, en, insert_indx)
#                     # 如果有位置
#                     after_n = len(N) - n_indx # 包含此項目後面還有幾個項目
#                     # print("after_n :",after_n, insert_indx + after_n, K)
#                     if insert_indx + after_n >= K :
#                         ans = ans[:insert_indx] + [n]
#                         smallest_indx_list = smallest_indx_list[:s_indx+1] + [insert_indx]
#                     else :
#                         # 沒有位置就只能放後面 (就會多一截出來)
#                         insert_indx = K - after_n
#                         ans = ans[:insert_indx] + [n]
#                         smallest_indx_list = smallest_indx_list[:s_indx+1] + [insert_indx-1, insert_indx]
#                     # print("_find :",ans , smallest_indx_list, insert_indx)
#                     break
#             if len(ans)<K and mem_find_place == False :
#                 # 直接加在最後面
#                 smallest_indx_list[-1] += 1
#                 ans.append(n)
#                 # print("_no find :",ans , smallest_indx_list)
#         return ans

# # above version but remove making new list EX: ans = ans[:insert_indx]
# 1881ms Beats5.25%
# import bisect
# class Solution:
#     def mostCompetitive(self, N, K):
#         ans = [1000000001]
#         smallest_indx_list = [0,0]
#         for n_indx, n in enumerate(N) :
#             mem_find_place = False
#             for s_indx in range(len(smallest_indx_list)-1) :
#                 sta = smallest_indx_list[s_indx]
#                 en = smallest_indx_list[s_indx+1]
#                 if n < ans[en] :
#                     mem_find_place = True
#                     # 找到可以插入的位置
#                     insert_indx = bisect.bisect_right(ans, n, lo=sta, hi=en+1)
#                     # print("insert :", n, sta, en, insert_indx)
#                     # 如果有位置
#                     after_n = len(N) - n_indx # 包含此項目後面還有幾個項目
#                     # print("after_n :",after_n, insert_indx + after_n, K)
#                     if insert_indx + after_n >= K :
#                         while len(ans) > insert_indx :
#                             ans.pop()
#                         ans.append(n)
#                         _temp = s_indx+1
#                         while len(smallest_indx_list) > _temp :
#                             smallest_indx_list.pop()
#                         smallest_indx_list.append(insert_indx)
#                         # ans = ans[:insert_indx] + [n]
#                         # smallest_indx_list = smallest_indx_list[:s_indx+1] + [insert_indx]
#                     else :
#                         # 沒有位置就只能放後面 (就會多一截出來)
#                         insert_indx = K - after_n
#                         while len(ans) > insert_indx :
#                             ans.pop()
#                         ans.append(n)
#                         _temp = s_indx+1
#                         while len(smallest_indx_list) > _temp :
#                             smallest_indx_list.pop()
#                         smallest_indx_list.append(insert_indx-1)
#                         smallest_indx_list.append(insert_indx)
#                         # ans = ans[:insert_indx] + [n]
#                         # smallest_indx_list = smallest_indx_list[:s_indx+1] + [insert_indx-1, insert_indx]
                        
#                     # print("_find :",ans , smallest_indx_list, insert_indx)
#                     break
#             if len(ans)<K and mem_find_place == False :
#                 # 直接加在最後面
#                 smallest_indx_list[-1] += 1
#                 ans.append(n)
#                 # print("_no find :",ans , smallest_indx_list)
#         return ans

s = Solution()
print(s.mostCompetitive([2,4,3,3,5,4,9,6], 4))
# print(s.mostCompetitive([3,5,2,6], 2))
# print(s.mostCompetitive([71,18,52,29,55,73,24,42,66,8,80,2], 3))
# print(s.mostCompetitive([71,18,52,29,55,73,24,42,66,8,80,81,82,83,84], 3))
# print(s.mostCompetitive([71,18,52,29,55,73,24,42,66,8,80], 3))