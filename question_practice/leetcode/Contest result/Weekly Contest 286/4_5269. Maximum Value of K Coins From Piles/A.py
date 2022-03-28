# 當時的測驗結果
# 想法是對的 只是時間不夠
# class Solution:
#     def maxValueOfCoins(self, piles, k):
#         # 目前取N個最好的結果
#         mem = [0]*(k+1)
        
#         for each_pile in piles :
#             now_coin_sum = 0
#             for indx , coins in enumerate(each_pile):
#                 now_coin_sum += coins
#                 # indx+1 代表此pile取幾個 
#                 # for : ??
#                     # mem[k-indx] = max(mem[k-indx], mem[k-(indx+1)]+now_coin_sum)
                
#             print(mem)
        
#         return max(mem)

# My 繼續完成  有參考 given ans 想法錯在哪裡
# mem 是紀錄到目前為止 取N個的最佳結果
# 新加入的一排就是跟mem湊 做出新的mem
class Solution:
    def maxValueOfCoins(self, piles, k):
        # 目前取N個最好的結果 0~k
        mem = [0]*(k+1)
        for each_pile in piles :
            now_coin_sum = 0
            # 因為 mem[2]+從新pile的取1個 的這個組合  會複寫 mem[2+1] 這個位置
            # 在同一個pile中 mem[3]+從新pile的取1個  pile的取1個 會重複計算
            # 因此需要用 temp_mem
            temp_mem = mem.copy()
            for indx , coins in enumerate(each_pile):
                now_coin_sum += coins
                # indx+1 代表此pile取幾個 
                for mem_i in range(len(mem)): # i 是 0 index
                    temp_indx = indx+1+mem_i
                    if temp_indx > k : # 不用 = 因為共有k+1個空間
                        break
                    # max 第一個是用 temp_mem 而不是 mem 是因為
                    # 組合 0+3 1+2 2+1 3+0 還是要取目前最大的  如果是使用temp_mem只會跟3+0比較(也就是舊的紀錄)
                    temp_mem[temp_indx] = max(temp_mem[temp_indx], mem[mem_i]+now_coin_sum)
            mem = temp_mem
            print(mem)
        return mem[-1]

# 跟我想法一樣的 given ans 
# 只是更精簡  使用的變數更少
# class Solution:
#     def maxValueOfCoins(self, p: List[List[int]], k: int) -> int:
#         f = [0] * (k + 1)
#         for a in p:
#             g = f[:]
#             s = 0
#             for i in range(len(a)):
#                 s += a[i]
#                 for j in range(i + 1, k + 1):
#                     g[j] = max(g[j], f[j - (i + 1)] + s)
#             f = g
#         return f[-1]

# given ans recursive 解法
# 這個 recursive 怎麼這麼奇怪  自己寫一個試試看
# from math import inf
# class Solution:
#     def maxValueOfCoins(self, piles, k):
#         # @cache
#         def ans(pile, rem):
#             # print(pile, rem)
#             # 代表使用的數量 超過k
#             if rem < 0:
#                 return -inf  # return -inf 其實就只是不希望選這個選項而已
#             # 代表pile已經超過piles的數量了
#             if pile < 0:
#                 # 如果剛剛好沒有要取更多的coin
#                 if rem == 0:
#                     return 0  # return 0 就是從0開始計算
#                 return -inf
#             res = ans(pile-1, rem)
#             cur = 0
#             for i in range(len(piles[pile])):
#                 cur += piles[pile][i]
#                 res = max(res, cur+ans(pile-1, rem-i-1))
#             return res
#         return ans(len(piles)-1, k)

# 自己試試看
# Accepted
# class Solution:
#     def maxValueOfCoins(self, piles, k):
#         def recursive(pile_num, remain):
#             if pile_num == len(piles) :
#                 # 到底了
#                 return 0

#             now_total_coin = 0
#             max_ret = 0
#             for indx, coins in enumerate(piles[pile_num]):
#                 # indx+1 代表此pile取幾個 
#                 now_total_coin += coins
#                 pass_remain = remain-(indx+1)
#                 if pass_remain < 0 :
#                     break
#                 max_ret = max(max_ret, recursive(pile_num+1, pass_remain) + now_total_coin)

#             # 也有可能取0個
#             max_ret = max(max_ret, recursive(pile_num+1, remain) + 0)

#             return max_ret

#         return recursive(0, k)

s = Solution()
print(s.maxValueOfCoins(piles = [[1,100,3],[7,8,9]], k = 2))
print(s.maxValueOfCoins(piles = [[100],[100],[100],[100],[100],[100],[1,1,1,1,1,1,700]], k = 7))
print(s.maxValueOfCoins(piles = [[1,1,1,1,1,1,700],[100],[100],[100],[100],[100],[100]], k = 7))
print(s.maxValueOfCoins(piles = [[100],[1,1,1,1,1,700],[100],[100],[100],[100],[100]], k = 7))
print(s.maxValueOfCoins([[37,88],[51,64,65,20,95,30,26],[9,62,20],[44]],9))
print(s.maxValueOfCoins([[1,2,3],[1,2,3],[1,2,3]],3))

