# my 
# class Solution:
#     def minBitFlips(self, start: int, goal: int):
#         st = bin(start)[2:]
#         go = bin(goal)[2:]
        
        
#         while len(st) > len(go) :
#             go = "0"+go
#         while len(st) < len(go) :
#             st = "0"+st
            
#         # print(st, go)
        
#         ans = 0
#         for i in range(len(st)) :
#             if st[i] != go[i]:
#                 ans += 1
#         return ans

# given ans 1
class Solution:
    def minBitFlips(self, s: int, t: int):
        # 對ㄟ 有XOR 這個東西
        return bin(s ^ t).count('1')

# given ans 2
# class Solution {
# public:
#     int minBitFlips(int start, int goal) {
#         int ans = 0;
#         while(start != 0 || goal != 0){
#             ans += (start & 1) != (goal & 1); 
#             start >>= 1;
#             goal >>= 1;
#         }
#         return ans;
#     }
# };

s = Solution()
print(s.minBitFlips(10, 7))



