# my Beats 16.17%
# 雖然速度比較慢 但是打出來比較快
class Solution(object):
    def addToArrayForm(self, num, k):
        front_num = 0
        for n in num :
            front_num = front_num*10 + n
        
        result_num = front_num + k

        result_list = []
        while(result_num != 0):
            result_list.insert(0,result_num%10)
            result_num = result_num//10

        return result_list

# 練習直接在原本的 list 中處理 (進位很麻煩 但應該比較快)

# given ans

s = Solution()
print(s.addToArrayForm(num = [1,2,0,0], k = 34))
print(s.addToArrayForm(num = [2,7,4], k = 181))
print(s.addToArrayForm(num = [2,1,5], k = 806))
# print(s.addToArrayForm())



