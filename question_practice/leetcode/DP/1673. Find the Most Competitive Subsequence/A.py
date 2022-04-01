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


# 邏輯
# 只要是遞增的數字 就放進 List (反正最後再裁就好)
# 只是我不懂最後 
class Solution:
    def mostCompetitive(self, N, K):
        i, moves = 0, len(N) - K
        print(moves)
        ans = []
        for x in N:
            # moves 計算 目前ans+N剩下的長度夠不夠
            while ans and moves and x < ans[-1]:
                ans.pop()
                print(ans)
                moves -= 1
                print(moves)
            ans.append(x)
            print(ans)
        return ans[:K]  # 這個是因為

s = Solution()
# print(s.mostCompetitive([2,4,3,3,5,4,9,6], 4))
# print(s.mostCompetitive([3,5,2,6], 2))
# print(s.mostCompetitive([71,18,52,29,55,73,24,42,66,8,80,2], 3))
# print(s.mostCompetitive([71,18,52,29,55,73,24,42,66,8,80,81,82,83,84], 3))
print(s.mostCompetitive([71,18,52,29,55,73,24,42,66,8,80], 3))