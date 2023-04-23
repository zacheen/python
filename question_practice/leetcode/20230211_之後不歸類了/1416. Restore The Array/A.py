from typing import List
import functools

# my v1 Time Limit Exceeded
# 原本以為要印出全部組合
class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        @functools.lru_cache(None)
        def dp(i) : # this will return the all combination from s[i:]
            if s[i] == '0':
                return []
            
            ret = []
            if int(s[i:]) <= k :
                ret.append([s[i:]])
            now_front = ""
            for cut_indx in range(i, len(s)-1) :
                now_front += s[cut_indx]
                if int(now_front) > k :
                    break
                ret_dp = dp(cut_indx+1) 
                for can_end in ret_dp :
                    ret.append([now_front] + can_end)
            return ret

        ans = dp(0)
        print(ans)
        return len(ans)

# # my v2 改成回傳結果個數還是 Time Limit Exceeded
# class Solution:
#     def numberOfArrays(self, s: str, k: int) -> int:
#         @functools.lru_cache(None)
#         def dp(i) : # this will return the all combination from s[i:]
#             if s[i] == '0':
#                 return 0
            
#             ret = 0
#             if int(s[i:]) <= k :
#                 ret += 1
#             now_front = ""
#             for cut_indx in range(i, len(s)-1) :
#                 now_front += s[cut_indx]
#                 if int(now_front) > k :
#                     break
#                 ret += dp(cut_indx+1) 
#             return ret % 1000000007

#         ans = dp(0)
#         return ans

# # my v3 我看 given ans 的架構跟我完全相同 不知道哪裡出問題
# # 竟然是出在 int(s[i:])
# # 這下面是 Time Limit Exceeded 的版本
# class Solution:
#     def numberOfArrays(self, s: str, k: int) -> int:
#         @functools.lru_cache(None)
#         def dp(i) : # this will return the all combination from s[i:]
#             if i == len(s) :
#                 return 1
#             if s[i] == '0':
#                 return 0
            
#             ret = 0
#             if int(s[i:]) <= k :
#                 ret += 1
#             now_front = 0
#             for cut_indx in range(i, len(s)-1) :
#                 now_front = now_front * 10 + int(s[cut_indx])
#                 if now_front > k :
#                     break
#                 ret = (ret+dp(cut_indx+1)) 
#             return ret % 1000000007

#         ans = dp(0)
#         return ans

# 通過的版本 : Beats 86.30%
# 只差在 if int(s[i:]) <= k : 的優化
    # 但是 int(s[i:]) 應該只會做 10^5 次 竟然就 time out 了
class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        @functools.lru_cache(None)
        def dp(i) : # this will return the all combination from s[i:]
            if i == len(s) :
                return 1
            if s[i] == '0':
                return 0
            
            ret = 0
            now_front = 0
            for cut_indx in range(i, len(s)) :
                now_front = now_front * 10 + int(s[cut_indx])
                if now_front > k :
                    break
                ret = ret+dp(cut_indx+1)
            return ret % 1000000007

        ans = dp(0)
        return ans
    
# 所以看起來是字串太長造成的
# # 測試 1 Time Limit Exceeded
# class Solution:
#     def numberOfArrays(self, s: str, k: int) -> int:
#         for i in range(len(s)) :
#             r = int(s[i:])

#         # 正確回傳 code
# # 測試 2 通過
# class Solution:
#     def numberOfArrays(self, s: str, k: int) -> int:
#         for i in range(len(s)) :
#             r = int(s[i])

#         # 正確回傳 code

s = Solution()
print(s.numberOfArrays(s = "1000", k = 10000))
print(s.numberOfArrays(s = "1000", k = 10))
print(s.numberOfArrays(s = "1317", k = 2000))



