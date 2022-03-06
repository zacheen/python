# My
class Solution:
    def rob(self, nums):
        
        # 從最後一個位置到現在位置 最多的可能拿多少錢
        cache = {}
        houseNum = len(nums)
        cache[houseNum-1] = nums[houseNum-1]
        if houseNum > 1 :
            cache[houseNum-2] = nums[houseNum-2]
        else :
            return nums[0]
        

        def search(pos): 
            # print(cache)
            his = cache.get(pos, None)
            if his != None :
                # print("有找到紀錄")
                return his
            

            maxCanRob = 0
            for i in range(pos+2,houseNum) :
                # print("search(i) i :",i)
                canrob = nums[pos] + search(i)
                if canrob > maxCanRob :
                    maxCanRob = canrob

            # print("寫紀錄 pos,maxCanRob",pos,maxCanRob)
            cache[pos] = maxCanRob
            return maxCanRob
            
        # 這個不能再和進去嗎?
        from_first = search(0)
        from_second = search(1)
        return max(from_first, from_second)


s = Solution()
# print(s.rob([1,2,3]))
# print(s.rob([1,1,1,2,7,9,3,1]))
# print(s.rob([0,0,0,0,0,0,0,0,0]))
print(s.rob([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]))