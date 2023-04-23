# my Beats 87.18%
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        ans = 0
        def dp(node):
            nonlocal ans
            left_len = 0
            right_len = 0

            if node.left :
                ret_left_len, ret_right_len = dp(node.left)
                left_len = ret_right_len + 1
                ans = max(ans, left_len)
            
            if node.right :
                ret_left_len, ret_right_len = dp(node.right)
                right_len = ret_left_len + 1
                ans = max(ans, right_len)

            return left_len, right_len
        
        dp(root)
        return ans

# my v2 較快且節省空間 但易讀性較差
# Beats 97.7%
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        ans = 0
        def dp(node):
            nonlocal ans
            left_len = 0
            right_len = 0

            if node.left :
                left_len = dp(node.left)[1] + 1
                ans = max(ans, left_len)
            if node.right :
                right_len = dp(node.right)[0] + 1
                ans = max(ans, right_len)

            return left_len, right_len
        
        dp(root)
        return ans
    
# given ans
# 差不多 只是用 class 回傳 
    # 我的寫法應該比較快

# s = Solution()
# print(s.())



