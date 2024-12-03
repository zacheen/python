# 1105. Filling Bookcase Shelves
# https://leetcode.com/problems/filling-bookcase-shelves

from typing import List
import functools
import math

# my 49ms Beats74.58%
class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        
        dp_height = [0]+[0]*len(books)
        # 到 這本書 最好的結果會存在 dp_height 裡面
            # indx+1 是包含第 books[indx] 最好的組合是
        for indx,(th,h) in enumerate(books) :
            # 如果放入上一行 (找出所有上一行最佳解)
            can_fit_sum = 0
            max_comb_th = 0
            comb_h_min = math.inf
            for can_fit_indx in range(indx,-1,-1):
                past_th, past_h = books[can_fit_indx]
                can_fit_sum += past_th
                if can_fit_sum > shelfWidth :
                    break
                max_comb_th = max(max_comb_th, past_h)
                comb_h_min = min(comb_h_min, max_comb_th+dp_height[can_fit_indx])
            # 其實這個部分已經包含在上面了
            # # 如果我在這本書這裡分層
            # sep_h = dp_height[indx] + h
            # # print(comb_h_min, sep_h)
            # dp_height[indx+1] = min(comb_h_min, sep_h)
            dp_height[indx+1] = comb_h_min
        # print(dp_height)
        return dp_height[-1]

# given ans
# similar concept : directly save comb_h_min into dp_height
class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        # dp[i] := the minimum height to place the first i books
        dp = [0] + [math.inf] * len(books)

        for i in range(len(books)):
            sumThickness = 0
            maxHeight = 0
            # Place books[j..i] on a new shelf.
            for j in range(i, -1, -1):
                thickness, height = books[j]
                sumThickness += thickness
                if sumThickness > shelfWidth:
                    break
                maxHeight = max(maxHeight, height)
                dp[i + 1] = min(dp[i + 1], dp[j] + maxHeight)

        return dp[-1]
s = Solution()
# print(s.minHeightShelves(books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], shelfWidth = 4))
# print(s.minHeightShelves(books = [[1,3],[2,4],[3,2]], shelfWidth = 6))
print(s.minHeightShelves([[11,83],[170,4],[93,80],[155,163],[134,118],[75,14],[122,192],[123,154],[187,29],[160,64],[170,152],[113,179],[60,102],[28,187],[59,95],[187,97],[49,193],[67,126],[75,45],[130,160],[4,102],[116,171],[43,170],[96,188],[54,15],[167,183],[58,158],[59,55],[148,183],[89,95],[90,113],[51,49],[91,28],[172,103],[173,3],[131,78],[11,199],[77,200],[58,65],[77,30],[157,58],[18,194],[101,148],[22,197],[76,181],[21,176],[50,45],[80,174],[116,198],[138,9],[58,125],[163,102],[133,175],[21,39],[141,156],[34,185],[14,113],[11,34],[35,184],[16,132],[78,147],[85,170],[32,149],[46,94],[196,3],[155,90],[9,114],[117,119],[17,157],[94,178],[53,55],[103,142],[70,121],[9,141],[16,170],[92,137],[157,30],[94,82],[144,149],[128,160],[8,147],[153,198],[12,22],[140,68],[64,172],[86,63],[66,158],[23,15],[120,99],[27,165],[79,174],[46,19],[60,98],[160,172],[128,184],[63,172],[135,54],[40,4],[102,171],[29,125],[81,9],[111,197],[16,90],[22,150],[168,126],[187,61],[47,190],[54,110],[106,102],[55,47],[117,134],[33,107],[2,10],[18,62],[109,188],[113,37],[59,159],[120,175],[17,147],[112,195],[177,53],[148,173],[29,105],[196,32],[123,51],[29,19],[161,178],[148,2],[70,124],[126,9],[105,87],[41,121],[147,10],[78,167],[91,197],[22,98],[73,33],[148,194],[166,64],[33,138],[139,158],[160,19],[140,27],[103,109],[88,16],[99,181],[2,140],[50,188],[200,77],[73,84],[159,130],[115,199],[152,79],[1,172],[124,136],[117,138],[158,86],[193,150],[56,57],[150,133],[52,186],[21,145],[127,97],[108,110],[174,44],[199,169],[139,200],[66,48],[52,190],[27,86],[142,191],[191,79],[126,114],[125,100],[176,95],[104,79],[146,189],[144,78],[52,106],[74,74],[163,128],[34,181],[20,178],[15,107],[105,8],[66,142],[39,126],[95,59],[164,69],[138,18],[110,145],[128,200],[149,150],[149,93],[145,140],[90,170],[81,127],[57,151],[167,127],[95,89]],200))



