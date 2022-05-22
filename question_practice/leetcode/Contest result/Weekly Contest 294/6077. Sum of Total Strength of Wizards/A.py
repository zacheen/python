# my 
class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        
        # 從頭到此index的累計
        sum_acc = [0]
        now_sum = 0
        for n in strength :
            now_sum += n
            now_sum = now_sum % 1000000007
            sum_acc.append(now_sum)
        # print(sum_acc)
        
        def get_sum(l,r) :
            sub = sum_acc[l] - sum_acc[r]
            if sub < 0 :
                return sub + 1000000007
            else :
                return sub
        
        # min_lr[l][r] 從 index l 到 index r(包含) 的最小值
        min_lr = [[0]*(len(strength)+1) for _ in range(len(strength)+1)]
        for i in range(len(strength)) :
            min_lr[i][i] = strength[i]
            
        # 原因應該是因為我不知道 找各段區間 min 的演算法
        for l in range(0, len(strength)-1) :
            for i in range(0, len(strength)-l-1) :
                # print(i, i+l+1, " || ", i, i+l, " || ", i+l)
                index1 = i+l
                index2 = index1+1 
                min_lr[i][index2] = min(min_lr[i][index1],strength[index2])
            # print("-----")
        
        # print(min_lr)
        # min_lr[i][i+1] = min(min_lr[i][i],strength[i])
        # min_lr[i][i+2] = min(min_lr[i][i+1],strength[i+1])
        # min_lr[i][i+l+1] = min(min_lr[i][i+l],strength[i+l]) 
        
        ans = 0
        for i in range(len(strength)) :
            for ii in range(i+1,len(strength)+1) :  # ii 位置不包含
                ans += get_sum(ii,i) * min_lr[i][ii-1]
                ans = ans % 1000000007
        return ans

# given ans

s = Solution()
print(s.())



