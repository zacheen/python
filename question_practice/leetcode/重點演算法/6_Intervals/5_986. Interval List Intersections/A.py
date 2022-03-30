# my Runtime: 156 ms, faster than 89.52% of Python3 
class Solution:
    def intervalIntersection(self, firstList, secondList):
        fir_indx = 0
        sec_indx = 0
        
        ans = []
        while fir_indx < len(firstList) and sec_indx < len(secondList) :
            max_fir = max(firstList[fir_indx][0], secondList[sec_indx][0])
            min_sec = min(firstList[fir_indx][1], secondList[sec_indx][1])
            
            if max_fir <= min_sec :
                ans.append([max_fir , min_sec])
            
            # end 比較後面的留下
            if firstList[fir_indx][1] > secondList[sec_indx][1] :
                sec_indx += 1
            else :
                fir_indx += 1
                
        return ans

# given ans 一樣

s = Solution()
print(s.intervalIntersection(firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]))
