from typing import List
import functools
# # my v1
# class Solution:
#     def ways(self, pizza, k):
#         # 我覺得應該是 dfs 拉，因為 k 最大只有10
#         @functools.lru_cache(None)
#         # start_x 不包含 end_x
#         def check_have_item(start_x, end_x, start_y, end_y):
#             for x in range(start_x, end_x) :
#                 for y in range(start_y, end_y) :
#                     if pizza[y][x] == "A" :
#                         # print("at check_have_item", start_x, end_x, start_y, end_y, "have result !!")
#                         return True
#             # print("at check_have_item", start_x, end_x, start_y, end_y, "dont have result")
#             return False
        
#         if check_have_item(0, len(pizza[0]), 0, len(pizza)) == 0:
#             return 0

#         # for convenient end_x, end_y does not include line end_x, end_y
#         @functools.lru_cache(None)
#         def dfs(start_x, end_x, start_y, end_y, step):
#             if step == 0:
#                 return 1

#             step -= 1
#             total_count = 0
#             for cut_x in range(start_x+1, end_x) :
#                 if check_have_item(start_x, cut_x, start_y, end_y) and check_have_item(cut_x, end_x, start_y, end_y) :
#                     # 兩邊都還有東西
#                     ret_front = dfs(start_x, cut_x, start_y, end_y, 0)
#                     # print(start_x, cut_x, start_y, end_y, 0 ,"cut comb :", ret_front)
#                     if ret_front != 0 :
#                         ret_back = dfs(cut_x, end_x, start_y, end_y, step)
#                         if ret_back == 0: # if result % 1000000007 == 0, the result will goes wrong, but I think 1000000007 is a prime number
#                             break
#                         total_count += ret_front*ret_back
#                         total_count = total_count % 1000000007                
#             for cut_y in range(start_y+1, end_y) :
#                 if check_have_item(start_x, end_x, start_y, cut_y) and check_have_item(start_x, end_x, cut_y, end_y) :
#                     # 兩邊都還有東西
#                     ret_front = dfs(start_x, end_x, start_y, cut_y, 0)
#                     # print(start_x, end_x, start_y, cut_y, 0 ,"cut comb :", ret_front)
#                     if ret_front != 0 :
#                         ret_back = dfs(start_x, end_x, cut_y, end_y, step)
#                         if ret_back == 0 : 
#                             break
#                         total_count += ret_front*ret_back
#                         total_count = total_count % 1000000007
#             return total_count

#         return dfs(0, len(pizza[0]), 0, len(pizza), k-1) # k-1 是因為總共切 k-1 刀，會變成 k 片

# # my v2 參考 given ans 的 hasApple 方法
# # Beats 7.48% 還是很慢
# class Solution:
#     def ways(self, pizza, k):
#         # 先計算各個位置 從 0,0 ~ i,j 共有幾個 'A'
#         M = len(pizza)
#         N = len(pizza[0])
#         prefix = [[0] * (N+1) for _ in range(M+1)]
#         # prefix[i][j] : (0,0) ~ (i,j) 'A' number (not include i,j )
#         for i in range(M):
#             count_this_line = 0
#             for j, piz in enumerate(pizza[i]):
#                 if piz == 'A' :
#                     count_this_line += 1
#                 if i == 0 :
#                     prefix[i+1][j+1] = count_this_line
#                 else :
#                     prefix[i+1][j+1] = prefix[i][j+1] + count_this_line
#         print(prefix)
                
#         @functools.lru_cache(None)
#         # start_x 不包含 end_x
#         def check_have_item(start_x, end_x, start_y, end_y):
#             print(start_x, end_x, start_y, end_y)
#             num_a = prefix[end_y][end_x] - prefix[end_y][start_x] - prefix[start_y][end_x] + prefix[start_y][start_x]
#             # print(prefix[end_x][end_y], prefix[start_x][end_y], prefix[end_x][start_y], prefix[start_x][start_y], num_a)
#             return num_a > 0
        
#         if prefix[-1][-1] == 0:
#             return 0

#         # for convenient end_x, end_y does not include line end_x, end_y
#         @functools.lru_cache(None)
#         def dfs(start_x, end_x, start_y, end_y, step):
#             if step == 0:
#                 return 1

#             step -= 1
#             total_count = 0
#             for cut_x in range(start_x+1, end_x) :
#                 if check_have_item(start_x, cut_x, start_y, end_y) and check_have_item(cut_x, end_x, start_y, end_y) :
#                     # 兩邊都還有東西
#                     ret_front = dfs(start_x, cut_x, start_y, end_y, 0)
#                     # print(start_x, cut_x, start_y, end_y, 0 ,"cut comb :", ret_front)
#                     if ret_front != 0 :
#                         ret_back = dfs(cut_x, end_x, start_y, end_y, step)
#                         if ret_back == 0: # if result % 1000000007 == 0, the result will goes wrong, but I think 1000000007 is a prime number
#                             break
#                         total_count += ret_front*ret_back
#                         total_count = total_count % 1000000007                
#             for cut_y in range(start_y+1, end_y) :
#                 if check_have_item(start_x, end_x, start_y, cut_y) and check_have_item(start_x, end_x, cut_y, end_y) :
#                     # 兩邊都還有東西
#                     ret_front = dfs(start_x, end_x, start_y, cut_y, 0)
#                     # print(start_x, end_x, start_y, cut_y, 0 ,"cut comb :", ret_front)
#                     if ret_front != 0 :
#                         ret_back = dfs(start_x, end_x, cut_y, end_y, step)
#                         if ret_back == 0 : 
#                             break
#                         total_count += ret_front*ret_back
#                         total_count = total_count % 1000000007
#             return total_count

#         return dfs(0, len(pizza[0]), 0, len(pizza), k-1) # k-1 是因為總共切 k-1 刀，會變成 k 片

# given ans 原本有錯 (我有修改)
    # 他的想法是 dp ，我現在切這刀，左邊就是固定的結果，就看右邊的範圍切 k-1 刀 有幾個切法
    # 我的想法是 左邊有幾種切法 * 右邊有幾種切法
        # 但是最後我發現這樣會重複，所以改成 ret_front = dfs(start_x, cut_x, start_y, end_y, 0) 
        # 但是其實 這個就是判斷 (start_x, cut_x, start_y, end_y) 裡面有沒有結果
    # 所以 given ans 就是我的方法的優化
# Beats 12.10%
# 還是很慢ㄟ
# 優化過後 : Beats 31.80%
class Solution:
    def ways(self, pizza, k):
        M = len(pizza)
        N = len(pizza[0])
        prefix = [[0] * (N + 1) for _ in range(M + 1)]

        # 先計算各個位置 從 0,0 ~ i,j 共有幾個 'A'
        for i in range(M):
            for j in range(N):
                prefix[i + 1][j + 1] = (pizza[i][j] == 'A') + \
                    prefix[i][j + 1] + prefix[i + 1][j] - prefix[i][j]
                
        # ANS 原本沒有例外處理
        if prefix[-1][-1] == 0:
            return 0

        # HasApple of pizza[row1..row2)[col1..col2)
        # 判斷此處有沒有 'A' 的方法就是 : (0,0)~(i2,j2) - (0,0)~(i2,j1) - (0,0)~(i1,j2) + (0,0)~(i1,j1) 
        @functools.lru_cache(None) # 我優化
        def hasApple(row1: int, row2: int, col1: int, col2: int):
            return (prefix[row2][col2] - prefix[row1][col2] -
                prefix[row2][col1] + prefix[row1][col1]) > 0

        # Dp(m, n, k) := # of ways to cut pizza[m:M][n:N] w/ k cuts
        @functools.lru_cache(None)
        def dp(m: int, n: int, k: int):
            if k == 0:
                return 1

            ans = 0
            for i in range(m + 1, M):  # Cut horizontally
                # 左半邊 跟 右半邊 都有剩下的 'A'
                if hasApple(m, i, n, N) and hasApple(i, M, n, N):
                    ans += dp(i, n, k - 1)

            for j in range(n + 1, N):  # Cut vertically
                if hasApple(m, M, n, j) and hasApple(m, M, j, N):
                    ans += dp(m, j, k - 1)

            return ans % (1000000007)

        return dp(0, 0, k - 1) % (1000000007)

s = Solution()
# print("result", s.ways(pizza = ["A..","AAA","..."], k = 3))
# # "A..",
# # "AAA",
# # "..."
# print("result", s.ways(pizza = ["A..","AA.","..."], k = 3))
# print("result", s.ways(pizza = ["A..","A..","..."], k = 1))
#     # "A.."
#     # "A.."
#     # "..."
# print("result", s.ways(pizza = ["...","...","..."], k = 1))
print("result", s.ways(pizza = [".A","AA","A."], k = 3))


