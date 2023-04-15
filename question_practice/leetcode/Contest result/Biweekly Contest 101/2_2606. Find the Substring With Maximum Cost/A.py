# my Time Limit Exceeded (不知道 subarray 區域最佳解的演算法)
class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        cost = {}
        for i in range(ord('a'), ord('a')+26):
            cost[chr(i)] = i - ord('a') + 1
        for c, val in zip(chars, vals) :
            cost[c] = val
            
        cost_list = []
        total_cost = 0
        front_to_i_cost = [0] # front_to_i_cost[i] not inlcude i
        for c in s:
            total_cost += cost[c]
            front_to_i_cost.append(total_cost)
        
        total_cost = front_to_i_cost[-1]
        i_to_back_cost = [total_cost] # i_to_back_cost[i] include i
        for c in s:
            total_cost -= cost[c]
            i_to_back_cost.append(total_cost)
            
        # i~j(not include j) = all - front~(i-1) - j~end
        min_out_side = 0
        for i,f in enumerate(front_to_i_cost[:-1]):
            l = min(i_to_back_cost[i+1:])
            min_out_side = min(min_out_side, (f + l))
        return max(0, front_to_i_cost[-1], front_to_i_cost[-1] - min_out_side)

# 參考 given ans 改寫
# 其實有點像 sliding window + greedy
    # 固定 sliding window 的 l，找出 r 最佳解位置
class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        cost = {}
        for i in range(ord('a'), ord('a')+26):
            cost[chr(i)] = i - ord('a') + 1
        for c, val in zip(chars, vals) :
            cost[c] = val
            
        total_cost = 0
        front_min_cost = 0
        max_ans = 0
        for c in s:
            total_cost += cost[c]
            front_min_cost = min(front_min_cost, total_cost)
            max_ans = max(max_ans, total_cost-front_min_cost)
        return max_ans

# s = Solution()
# print(s.())



