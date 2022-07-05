# 練 index
# 

# my 
# Runtime: 2212 ms, faster than 93.06% of Python3
# Runtime: 2030 ms, faster than 95.71% of Python3
class Solution:
    def findMaxForm(self, strs, m, n):
        count = defaultdict(list)
        
        for s in strs :
            c  = Counter(s)
            count[c["0"]].append(c["1"])
            
        for key, items in count.items() :
            items.sort()
            
        mem = [[0]*(n+1) for _ in range(m+1)]
        # mem[M][N] 選 M個0 N個1 最多可以有幾個 subset 
        # O(m*n*strs.length)
        max_ans = 0
        for count0 in range(101) :
            for count1 in count[count0] :
                have_better_result = False
                new_mem = copy.deepcopy(mem)
                for bi, i in zip(range(0,m-count0+1),range(count0,m+1)):
                    for bii, ii in zip(range(0,n-count1+1),range(count1,n+1)):
                        # print(bi, i, bii, ii )
                        new_res = mem[bi][bii]+1
                        if new_res > new_mem[i][ii] :
                            max_ans = max(new_res, max_ans)
                            new_mem[i][ii] = new_res
                            have_better_result = True
                mem = new_mem
                # print(count0, count1)
                if have_better_result == False :
                    # print(count0, count1)
                    break
                
        # print(mem)
        return max_ans

# given ans
# 跟我未優化前的想法一樣
# 但從後面開始覆寫 因此不用創建new_mem (O)
# 結果一定在 dp[m][n] 因此不用 max_ans
# class Solution:
#     def findMaxForm(self, strs, m, n):
#         # dp[i][j] := max size of the subset given i 0's and j 1's are available
#         dp = [[0] * (n + 1) for _ in range(m + 1)]

#         for s in strs:
#             count0 = s.count('0')
#             count1 = len(s) - count0
#             for i in range(m, count0 - 1, -1):
#                 for j in range(n, count1 - 1, -1):
#                     dp[i][j] = max(dp[i][j], dp[i - count0][j - count1] + 1)

#         return dp[m][n]

s = Solution()
print(s.findMaxForm())



