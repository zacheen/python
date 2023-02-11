# my 
from collections import defaultdict
class Solution(object):
    def create_dir_map(self, dir_list):
        dir_map = defaultdict(list)
        for i,j in dir_list:
            if i in dir_map.keys():
                dir_map[i].append(j);
            else :
                dir_map[i] = [j]

        return dir_map

        
    def shortestAlternatingPaths(self, n, redEdges, blueEdges):
        # only one way

        red_dir_map = self.create_dir_map(redEdges)
        blue_dir_map = self.create_dir_map(blueEdges)

        max_len_plus_one = 2*n+1
        red_min_step = [max_len_plus_one]*n
        blue_min_step = [max_len_plus_one]*n

        red_next_possible = [0]
        blue_next_possible = [0]

        i = 0
        while True: # n*2 每個點可能走兩次 因為不同顏色
            new_red_next_possible = []
            new_blue_next_possible = []
            for p in red_next_possible :
                if (red_min_step[p] < i):
                    continue
                red_min_step[p] = i
                new_blue_next_possible += red_dir_map[p]
            for p in blue_next_possible :
                if (blue_min_step[p] < i):
                    continue
                blue_min_step[p] = i
                new_red_next_possible += blue_dir_map[p]
            
            if not new_red_next_possible and not new_blue_next_possible :
                break

            red_next_possible = new_red_next_possible
            blue_next_possible = new_blue_next_possible
            i+=1

            # print(red_min_step)
            # print(blue_min_step)

        ans = [0]*n
        for i in range(n):
            ans[i] = min(red_min_step[i], blue_min_step[i])
            if ans[i] == max_len_plus_one :
                ans[i] = -1
        return ans

# given ans

s = Solution()
print(s.shortestAlternatingPaths(n = 3, redEdges = [[0,1],[1,2]], blueEdges = []))
print(s.shortestAlternatingPaths(n = 3, redEdges = [[0,1]], blueEdges = [[1,2]]))
print(s.shortestAlternatingPaths(n = 3, redEdges = [[0,1]], blueEdges = [[2,1]]))
print(s.shortestAlternatingPaths(n = 5, redEdges = [[0,1],[1,2],[2,3],[3,4]], blueEdges = [[1,2],[2,3],[3,1]]))



