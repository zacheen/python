# my 一開始以為要回傳 list
# class Solution(object):
#     def mergeKLists(self, lists):
#         each_smallest = [(lists[x][0],0,x) for x in range(len(lists))]
#         each_smallest.sort(reverse=True)
#         # print(each_smallest)

#         ans_list = []
#         while each_smallest :
#             smallest_info = each_smallest.pop()
#             ans_list.append(smallest_info[0])

#             if (smallest_info[1]+1) < len(lists[smallest_info[2]]) :
#                 new_num = lists[smallest_info[2]][smallest_info[1]+1]

#                 # 找插入位置
#                 left, right = 0, len(each_smallest)
#                 while left < right:
#                     mid = (left + right) // 2
#                     if each_smallest[mid][0] > new_num :
#                         # 沒通過
#                         left = mid + 1
#                     else:
#                         # 通過(包含 == target 的情況)
#                         right = mid 

#                 each_smallest.insert(left, (new_num, smallest_info[1]+1, smallest_info[2]))
#             # print(each_smallest)

#         return ans_list

# my 修改成正確格式 Beats 97.40%
class Solution(object):
    def mergeKLists(self, lists):
        each_smallest = [ll for ll in lists if ll is not None]
        each_smallest.sort(reverse = True, key = lambda x: x.val)

        ans_list = None
        root = None
        while each_smallest :
            smallest_info = each_smallest.pop()
            if ans_list :
                ans_list.next = smallest_info
                ans_list = ans_list.next
            else :
                ans_list = smallest_info
                root = smallest_info

            if smallest_info.next != None :
                new_node = smallest_info.next

                # 找插入位置
                left, right = 0, len(each_smallest)
                while left < right:
                    mid = (left + right) // 2
                    if each_smallest[mid].val > new_node.val :
                        # 沒通過
                        left = mid + 1
                    else:
                        # 通過(包含 == target 的情況)
                        right = mid 

                each_smallest.insert(left, new_node)
            # print(each_smallest)
        return root

# given ans

s = Solution()
print(s.mergeKLists([[1,4,5],[1,3,4],[2,6]]))



