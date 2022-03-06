
# 可以優化看看 v2 
# v1 每次加減 Runtime: 393 ms, faster than 83.56% of Python3
class Solution:
    def maxConsecutiveAnswers(self, answerKey, k):
        listLen = len(answerKey)
        if listLen == 0 :
            return 0
        
        memWord = answerKey[0]
        firstMemPlace = 0
        diffList = []
        
        from collections import Counter
        count = Counter()

        l = 0
        maxLen = -1
        for r, word in enumerate(answerKey) :
            count[word] = count[word] + 1

            if count["T"] > k and count["F"] > k :
                print("out : ",word, r, count["T"], count["F"])
                beforeOutLen = r - l - 1
                if beforeOutLen > maxLen :
                    maxLen = beforeOutLen

                # 優化 這裡可以改成計數的 因為一開始已經計算過了
                while count["T"] > k and count["F"] > k :
                    count[answerKey[l]] = count[answerKey[l]] - 1
                    l = l + 1

                print("safe :",answerKey[l], l, count["T"], count["F"])
                if r - l > maxLen :
                    maxLen = r - l

        lastLen = (len(answerKey) - l -1)
        if lastLen > maxLen :
                maxLen = lastLen
        
        return maxLen + 1
            

                    

            


s = Solution()
# print(s.maxConsecutiveAnswers("TFFT", 1))
# print(s.maxConsecutiveAnswers("TTFF", 2))
print(s.maxConsecutiveAnswers("TTFTTTTTFT", 1))