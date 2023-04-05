# my Beats 59.16%
class Solution:
    def numRescueBoats(self, people, limit):
        people.sort()
        l = 0
        r = len(people)-1

        ans = 0
        while l<=r :
            if people[l] + people[r] <= limit :
                # 如果很常不進入這個判斷式 可以用 bisect 去判斷下一個位置
                l += 1
            ans += 1
            r -= 1
        return ans

# given ans Beats 59.16%
    # 看起來運算次數會少一點 不知道為什麼沒比較快
# 優化不用每次都 + 再比較
# 直接計算下一個數字應該要小於哪個數字
class Solution:
    def numRescueBoats(self, people, limit):
        people.sort()
        l = 0
        r = len(people)-1

        ans = 0
        while l <= r :
            big_limit = limit-people[l]
            while people[r] > big_limit :
                ans += 1
                r -= 1
                if l > r :
                    return ans
            ans += 1
            r -= 1
            l += 1
        return ans
    
s = Solution()
print(s.numRescueBoats(people = [1,2], limit = 3))
print(s.numRescueBoats(people = [3,2,2,1], limit = 3))
print(s.numRescueBoats(people = [3,5,3,4], limit = 5))



