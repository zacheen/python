# my v1
class Solution:
    def miceAndCheese(self, reward1, reward2, k):
        diff_list = []
        for i in range(len(reward1)) :
            diff_list.append((reward1[i] - reward2[i], i))
        diff_list.sort(reverse = True)
        # print(diff_list)
        
        one_eat_indx = set( indx for _,indx in diff_list[:k] )
        # print(one_eat_indx)
        ans = 0
        for i in range(len(reward1)) :
            if i in one_eat_indx :
                ans += reward1[i]
            else :
                ans += reward2[i]
        
        return ans
# my v2
# 考試時有想到 是不是可以用總和然後把差距補回來
class Solution:
    def miceAndCheese(self, reward1, reward2, k):
        diff_list = [(re1 - re2) for re1, re2 in zip(reward1, reward2)]
        diff_list.sort(reverse = True)
        # print(diff_list)
        
        reward2_sum = sum(reward2)
        diff_sum = sum(diff_list[:k])
            # diff = reward1 - reward2 
            # 所以 reward1 = reward2 + diff
        return reward2_sum + diff_sum

# given ans
# 跟 v2 差不多

s = Solution()
print(s.miceAndCheese(reward1 = [1,1,3,4], reward2 = [4,4,1,1], k = 2))
print(s.miceAndCheese(reward1 = [1,1], reward2 = [1,1], k = 2))



