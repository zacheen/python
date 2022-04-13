class Solution:
    # given ans
    def shortestPathLength(self, graph):
        def dp(node, mask):
            state = (node, mask)
            if state in cache:
                return cache[state]
            if mask & (mask - 1) == 0:
                # Base case - mask only has a single "1", which means
                # that only one node has been visited (the current node)
                return 0

            cache[state] = float("inf") # Avoid infinite loop in recursion
            for neighbor in graph[node]:
                if mask & (1 << neighbor):
                    already_visited = 1 + dp(neighbor, mask)
                    not_visited = 1 + dp(neighbor, mask ^ (1 << node))
                    cache[state] = min(cache[state], already_visited, not_visited)

            return cache[state]

        n = len(graph)
        ending_mask = (1 << n) - 1
        cache = {}

        return min(dp(node, ending_mask) for node in range(n))

    # my Time Limit Exceeded
    # def shortestPathLength(self, graph):
    #     def go_into(graph, now, remain, his, path):
    #         # can go ?
    #         # print(now, remain, his, path, graph[now])
    #         min_len = 10000
    #         min_path = None
    #         for can_go_path in graph[now] :
    #             # print(now, can_go_path, remain, his, path, graph[now])
    #             # print(str(can_go_path)+" in remain : ",can_go_path in remain)
    #             # print("his.get("+str(now)+" "+str(can_go_path)+", False) == False : ",his.get(str(now)+" "+str(can_go_path), False) == False)
    #             if his.get(str(now)+" "+str(can_go_path), False) == False :
    #                 pass_remain = remain.copy()
    #                 if can_go_path in remain :
    #                     # print("before :",pass_remain)
    #                     pass_remain.remove(can_go_path)
    #                     # print("after :",pass_remain)
    #                 if len(pass_remain) == 0 :
    #                     ret = path.copy()
    #                     ret.append(can_go_path)
    #                     return ret
    #                 pass_his = his.copy()
    #                 pass_his[str(now)+" "+str(can_go_path)] = True
    #                 # print("pass_his :",pass_his)
    #                 pass_path = path.copy()
    #                 pass_path.append(can_go_path)
    #                 res = go_into(graph, can_go_path, pass_remain, pass_his, pass_path)
    #                 if res != None :
    #                     resLen = len(res)
    #                     if min_len > resLen :
    #                         # print("有找到最小路徑")
    #                         min_len = resLen
    #                         min_path = res
    #         # print(now, remain, his, path, graph[now], "cant find path return")
    #         if min_path != None :
    #             return min_path
    #         else :
    #             return None
        
    #     minNum = 10000
    #     minPath = []
    #     for startpoint in range(len(graph)) :
    #         remain = list(range(len(graph)))
    #         remain.remove(startpoint)
    #         res = go_into(graph, startpoint, remain, {}, [startpoint])

    #         if res == None :
    #             continue
    #         # 例外結果處理
    #         res_len = len(res)
    #         print("res_len :",res_len)
    #         if res_len == len(graph) :
    #             return res_len - 1

    #         print("minNum : ",minNum,res_len)
    #         if minNum > res_len :
    #             minNum = res_len
    #             minPath = res

    #     if minNum != 10000 :
    #         return minNum - 1
    #     else :
    #         return 0
    
s = Solution()
print(s.shortestPathLength([[2,3,5,7],[2,3,7],[0,1],[0,1],[7],[0],[10],[9,10,0,1,4],[9],[7,8],[7,6]]))