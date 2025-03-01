# pseudotree 基環樹
    # 由於每個大小為 k 的連通塊都有 k 個點和 k 條邊，所以每個連通塊必定有且僅有一個環
    # 若每個點的出度均為 1，這樣的有向圖又叫做內向基環樹
    # 若每個點的入度均為 1，這樣的有向圖又叫做外向基環樹
    # 由基環樹組成的森林叫基環樹森林 (pseudoforest)。

# edges [n1,n2,n3] 0可以到n1, 1可以到n2, 2可以到n3 ... 以此類推

##### out pseudotree ########################################
# out pseudotree 因為"出度均為 1", 所以只有一條路徑，不用怕有岔路
    # 此特性 - classic : 2359. Find Closest Node to Given Two Nodes
    # https://leetcode.com/problems/find-closest-node-to-given-two-nodes/description/

# return [len, intersect(cycle include node)]
def find_all_cycle(edges):
    len_n = len(edges)
    ret = []
    time = 1
    timeVisited = [0] * len_n
    for now_n in range(len_n):
        if timeVisited[now_n] :
            continue
        startTime = time
        while now_n != -1 and not timeVisited[now_n]:
            timeVisited[now_n] = time
            time += 1
            now_n = edges[now_n]  # Move to next node
        # if now_n == -1 : go to an dead end (this line is a straight line)
        # if timeVisited[now_n] < startTime : meet a point that seen before
        if now_n != -1 and timeVisited[now_n] >= startTime:
            ret.append((time - timeVisited[now_n], now_n))
    return ret

# print(find_all_cycle([3,3,4,2,3]))
# print(find_all_cycle([1,0,4,2,3]))
# print(find_all_cycle([1,0,1,0,1]))

# classic : 2360. Longest Cycle in a Graph
# https://leetcode.com/problems/longest-cycle-in-a-graph/description/

##### out pseudotree end ########################################