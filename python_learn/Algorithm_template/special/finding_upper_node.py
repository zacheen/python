# direct links, but don't have cycles 
# find the relation between two node, whether upper or lower

# classic question
# 1462. Course Schedule IV
# https://leetcode.com/problems/course-schedule-iv/description

# because of "if seen[next_lower]:", 
    # each dfs(i, lower_rela[i]) will pass each point only once
    # in conclusion, it turn it into a tree, so every dfs(i, lower_rela[i]) at most O(n)

#                     upper[X] = (up, low) means node up is higher than node low                                                             
def find_lower(len_n, upper):
    links = [[] for _ in range(len_n)]
    for up, low in upper:
        links[up].append(low)

    lower_rela = [[False]*len_n for _ in range(len_n)]
    # means lower_rela[n1][n2] n1 is upper than n2
    def dfs(now_n, seen):
        for next_lower in links[now_n]:
            if seen[next_lower]: 
                continue
            seen[next_lower] = True
            dfs(next_lower, seen)
    for i in range(len_n):
        dfs(i, lower_rela[i])
    return lower_rela

lower_rela = find_lower(3, [[1,0],[2,1]])
print(lower_rela[2][0])
