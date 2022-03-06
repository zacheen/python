# Runtime: 28 ms, faster than 95.99% of Python3
class Solution:
    def reformatNumber(self, number):
        number = number.replace(" ","").replace("-","")
        # print("number :",number)
        
        stop = len(number) % 3
        stoPoint = len(number)-stop
        if stop < 2 :
            stoPoint = stoPoint - 3

        count = 0
        ans = ""
        while count < stoPoint :
            ans = ans + number[count:count+3] + "-"
            count = count + 3
            
        # print(stop,stoPoint,count)
        # print("ans :",ans)
        
        if stop == 1 :
            ans = ans + number[count:count+2] + "-" + number[count+2:count+4]
        else :
            ans = ans + number[count:]
            
        return ans

s = Solution()
print(s.reformatNumber("1-23-45 678"))