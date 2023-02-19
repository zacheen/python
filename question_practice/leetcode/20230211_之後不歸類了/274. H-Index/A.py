# my Beats 83.76%
class Solution(object):
    def hIndex(self, citations):
        citations.sort(reverse = True)
        for indx, num in enumerate(citations):
            if (indx + 1) > num :
                return int(indx)
        return len(citations)

# given ans 
class Solution:
    def hIndex(self, citations):
        n = len(citations)
        accumulate = 0
        count = [0] * (n + 1)

        # 統計各個數字 總共的數量 (且把大於最大可能的數字歸類成一類)
        for citation in citations:
            count[min(citation, n)] += 1

        # print(count)

        # To find the largeset h-index, loop from back to front
        # I is the candidate h-index
        for i, c in reversed(list(enumerate(count))):
            accumulate += c
            if accumulate >= i:
                return i

s = Solution()
print(s.hIndex([3,0,6,1,5]))
print(s.hIndex([1]))
print(s.hIndex([0]))
print(s.hIndex([]))



