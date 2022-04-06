from collections import Counter
# my 
class Solution:
    def findWinners(self, matches):
        all_player = set()
        
        count_lose = Counter()
        
        for win_p, lose_p in matches :
            all_player.add(win_p)
            all_player.add(lose_p)
            count_lose[lose_p] += 1
         
        ans = [[],[]]
        for player in all_player :
            if count_lose[player] == 0 :
                ans[0].append(player)
            elif count_lose[player] == 1 :
                ans[1].append(player)
        # 一開始不知道要排序...
        # 各自sort 應該比sort all_player 還要快 (因為數量比較少)
        ans[0].sort()
        ans[1].sort()
        return ans

# given ans
# 大家想法差不多

s = Solution()
print(s.findWinners([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]))
print(s.findWinners([[2,3],[1,3],[5,4],[6,4]]))


