# my Runtime: 78 ms, faster than 73.99% of Python3
class Solution:
    def duplicateZeros(self, arr):
        for i in reversed(range(len(arr))) :
            if arr[i] == 0 :
                arr.insert(i, 0)
                del(arr[-1])

# given ans

s = Solution()
ll = [1,0,2,3,0,4,5,0]
print(s.duplicateZeros(ll))
print(ll)



