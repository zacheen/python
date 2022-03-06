class Solution:
    def isPalindrome(self, s):
        regular = ""
        s = s.lower()
        for eachChar in s :
            if eachChar.isalpha() or eachChar.isnumeric():
                regular = regular + eachChar

        print(regular)

        totalLen = len(regular)
        mid = totalLen // 2
        print("mid:",mid)
        #################################
        # MaxIdx = totalLen - 1
        # for i in range(mid):
        #     if regular[i] != regular[MaxIdx-i] :
        #         return False
        ################################
        if totalLen % 2 == 0:
            back = regular[: mid-1 : -1]
        else :
            back = regular[: mid : -1]
        print("優 : ", regular[:mid], "|" ,back)
        return regular[:mid] == back
        ###################################
        return True

        
s = Solution()
print(s.isPalindrome("ab"))