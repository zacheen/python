# my Beats 97.66%
class Solution:
    def sumNumbers(self, root):
        self.total = 0

        def dfs(root, now_num):
            now_num = now_num*10 + root.val
            if root.left == None and root.right == None :
                self.total += now_num
                # print(self.total)
                return 
            
            if root.left :
                dfs(root.left, now_num)

            if root.right :
                dfs(root.right, now_num)

            return 

        dfs(root, 0)
        return self.total

# given ans Beats 87.82% 
class Solution:
    def sumNumbers(self, root):
        total = 0

        def dfs(root, now_num):
            nonlocal total
            # 很特別 還是可以在這邊判斷 root 是不是 None
                # 因為如果是尾端，其實判斷兩邊是不是 None 就已經 加總了
                # 這裡只是用來 return 
            if root == None :
                return 
            
            now_num = now_num*10 + root.val
            if root.left == None and root.right == None :
                total += now_num
                # print(self.total)
                return 

            dfs(root.left, now_num)
            dfs(root.right, now_num)

        dfs(root, 0)
        return total

s = Solution()
# print(s.())



