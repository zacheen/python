# My Time Limit Exceeded
# class Solution:
#     def digArtifacts(self, n, artifacts, dig):
#         def inside(region, dig):
#             if region[0] <= dig[0] and region[2] >= dig[0] and \
#                 region[1] <= dig[1] and region[3] >= dig[1] :
#                 return True
#             return False

#         # 創建 map 對應 還有幾格沒有挖到
#         # remain = {str(art[0])+"_"+str(art[1]):(art[2]-art[0]+1)*(art[3]-art[1]+1) for art in artifacts}
#         remain = {}
#         for art in artifacts :
#             # 因為List不能當hash值 所以我用 左上角兩個值 組合成字串當key值
#             remain[str(art[0])+"_"+str(art[1])] = (art[2]-art[0]+1)*(art[3]-art[1]+1)
#         print(remain)

#         for each_dig in dig :
#             if len(artifacts) == 0 :
#                 break

#             for each_art in artifacts :
#                 if inside(each_art, each_dig) == True :
#                     remain[str(each_art[0])+"_"+str(each_art[1])] -= 1
#                     break

#         # 統計有幾個格字全部都挖起來的
#         count = 0
#         for key, val in remain.items() :
#             print(key, val)
#             if val == 0:
#                 count = count+1

#         return count

# My v2 創建 2D 表個填值  每個 art 再一格一格掃 (跟目前最好的演算法差不多)
# Runtime: 2610 ms, faster than 82.11% of Python3
class Solution:
    def digArtifacts(self, n, artifacts, dig):
        import numpy as np
        all_place = np.zeros( shape = (n, n) , dtype = bool )

        for each_dig in dig :
            all_place[each_dig[0]][each_dig[1]] = True

        print(all_place)

        ans_count = 0
        for each_art in artifacts :
            all_dig = True
            for i in range(each_art[0], each_art[2]+1) :
                for j in range(each_art[1], each_art[3]+1) :
                    if not all_place[i][j] :
                        all_dig = False
                        break
                if all_dig == False :
                    break
            if all_dig :
                ans_count += 1

        return ans_count        


s = Solution()
# print(s.digArtifacts(n = 2, artifacts = [[0,0,0,0],[0,1,1,1]], dig = [[0,0],[0,1]]))
print(s.digArtifacts(n = 2, artifacts = [[0,0,0,0],[0,1,1,1]], dig = [[0,0],[0,1],[1,1]]))
