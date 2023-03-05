# https://leetcode.com/problems/find-duplicate-subtrees/description/
# my 做到一半意識到時間複雜度太高 所以放棄使用此方法
# class Solution:
#     def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:

#         ans = []

#         def check_same(root1, root2):
#             if root1 == None :
#                 if root2 == None :
#                     return True
#                 else :
#                     return False
#             else :
#                 if root2 == None :
#                     return False

#             # 確定 root1 跟 root2 都不是 None        
#             if root1.val != root2.val :
#                 return False
#             if (check_same(root1.right, root2.right)) and check_same(root1.left, root2.left) : 
#                 if not (root1 in mem_ans[root1.val]) :
#                     for 
#                     mem_ans[root1.val].append(root1)
#                     ans.append(root1)
#                 return True
#             else :
#                 return False

#         # 規則 : 一定會在左右 list
#         # 如果下面的 sub tree 可以 那我上面只要多比一點就好
#         # 如果下面的 sub tree 不行 那上面也一定不行
#         # -> 我從 root 開始做 只要有 return True 下面就不用再做了，且 return 的過程中所有的點都要加入 ans

#         mem = defaultdict(list)
#         mem_ans = defaultdict(list)
#         stack = [root]
#         while stack :
#             now_root = stack.pop()
#             if now_root != None :
#                 have_same = False
#                 for poss_root in mem[now_root.val] :
#                     is_same = check_same(poss_root, now_root)
#                     if is_same :
#                         have_same = True
#                         break
#                 if not have_same :
#                     mem[now_root.val].append(now_root)
#                     stack.append(now_root.right)
#                     stack.append(now_root.left)
#             # print(stack)
#         return ans
            

# given ans
class Solution:
    def findDuplicateSubtrees(self, root):
        ans = []
        count = collections.Counter()

        def encode(root):
            if not root:
                return ''

            encoded = str(root.val) + '#' + \
                encode(root.left) + '#' + \
                encode(root.right)
            count[encoded] += 1
            # 我原本的想法是要避開重複的比較 不過這裡的方法是想一個較快的比較方法
            # (因為這種方法還是會跟之前的每一個點去做完整的比較 且 subtree 會重複做一次)
            # hash 真的是跟每個項目比較有沒有相同的項目最快的方法
            if count[encoded] == 2:
                ans.append(root)
            return encoded

        encode(root)
        return ans

s = Solution()
print(s.findDuplicateSubtrees())



