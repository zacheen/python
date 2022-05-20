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

# 2022 05 17 重新練習
# Time Limit Exceeded
class Solution:
    def mostCompetitive(self, nums: List[int], k: int):
        # 從頭開始掃 如果長度允許就整個替換掉
        
        i = 1
        now_list = [nums[0]]
        
        while i < len(nums) :
            new_num = nums[i]
            # print(i, new_num, now_list)
            have_small = False
            for ii, this_n in enumerate(now_list) :
                # print(this_n , new_num, len(nums)-i, k - ii)
                if new_num < this_n and (len(nums)-i) >= (k - ii) :
                    # len(nums)-i代表nums還有幾個字    k-ii 代表now_list後面所需的長度
                    now_list = now_list[:ii] + [new_num]
                    have_small = True
                    break
            if not have_small :
                now_list.append(new_num)
            i+=1
        # print(now_list)
        return now_list[:k]

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

s = Solution()
# print(s.mostCompetitive([2,4,3,3,5,4,9,6], 4))
# print(s.mostCompetitive([3,5,2,6], 2))
# print(s.mostCompetitive([71,18,52,29,55,73,24,42,66,8,80,2], 3))
# print(s.mostCompetitive([71,18,52,29,55,73,24,42,66,8,80,81,82,83,84], 3))
print(s.mostCompetitive([71,18,52,29,55,73,24,42,66,8,80], 3))