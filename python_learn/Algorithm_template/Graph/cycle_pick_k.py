# check limitation of pick k node

from bisect import bisect_left

# checking whether picking "pick_k" nodes, these nodes distance is larger than "dis_thresh"
def check_cycle_valid(points, cycle_len, dis_thresh, pick_k):
    len_n = len(points)

    poss_p_i = [0]
    now_n = points[0]
    for j in range(1, pick_k):
        i = bisect_left(points, now_n + dis_thresh)
        if i == len_n:
            return False
        poss_p_i.append(i)
        now_n = points[i]
    # print(poss_p_i, now_n)

    if cycle_len - (now_n - points[0]) >= dis_thresh:
        return True
    
    for poss_p_i[0] in range(poss_p_i[0]+1, poss_p_i[1]):
        for j in range(1, pick_k):
            while points[poss_p_i[j]] - points[poss_p_i[j - 1]] < dis_thresh:
                poss_p_i[j] += 1
                if poss_p_i[j] == len_n:
                    return False
        if cycle_len - (points[poss_p_i[-1]] - points[poss_p_i[0]]) >= dis_thresh:
            return True
    return False

print(check_cycle_valid(points = [9, 36, 50, 112, 162, 175, 259], cycle_len = 264,
    dis_thresh = 51, pick_k = 4))
print(check_cycle_valid(points = [9, 36, 50, 112, 162, 175, 259], cycle_len = 264,
    dis_thresh = 55, pick_k = 4))
print(check_cycle_valid(points = [9, 36, 50, 112, 162, 175, 259], cycle_len = 264,
    dis_thresh = 56, pick_k = 4))
# print(check_cycle_valid(points, 
#     dis_thresh, pick_k, cycle_len))

def check_cycle_valid_explain(points, dis_thresh, pick_k, cycle_len):
    len_n = len(points)
    
    # 為什麼只需要計算 從第一個點開始 就可以知道是否會 return False ??
        # 這裡只有判斷 第一個點 到 最後一個點 是否有在限制之內
            # 這裡沒有判斷最後一個點到第一個點的距離是否合規則
        # 如果光是少一個點都不行了，那其他開頭的循環距離一定也不行
    # method 1 : 適合 points 多 pick_k 少 O(pick_k * log"points")
    poss_p_i = [0]
    now_n = points[0]
    for j in range(1, pick_k):
        i = bisect_left(points, now_n + dis_thresh)
        if i == len_n: # 到底了
            return False
        poss_p_i.append(i)
        now_n = points[i]
    # print(poss_p_i, now_n)

    # 現在 now_n 是最後一個點
    # 判斷以第一個點開始 是否可以合乎規則 
    if cycle_len - (now_n - points[0]) >= dis_thresh:
        return True
    
    # # method 2 : pick_k 接近 points 的數量 O(points)
    # # 或 如果需要找每個點的下一個點是誰
    # next_node = []
    # r = 1
    # for p in points :
    #     while r < len(points) and points[r] - p < dis_thresh : # actually total time complexity is O(n)
    #         r += 1
    #     if r == len(points) :
    #         break
    #     next_node.append(r)
    
    # poss_p_i = [0]
    # now_n = 0
    # for _ in range(pick_k-1):
    #     now_n = next_node[now_n]
    #     poss_p_i.append(now_n)
    # # print(poss_p_i, now_n)
    
    # 判斷其他點開頭是否可行
    # 其他可能的開頭只有第一個點到第二個點之間
    for poss_p_i[0] in range(poss_p_i[0]+1, poss_p_i[1]):
        for j in range(1, pick_k):
            while points[poss_p_i[j]] - points[poss_p_i[j - 1]] < dis_thresh:
                poss_p_i[j] += 1
                if poss_p_i[j] == len_n: # 到底了
                    return False
        if cycle_len - (points[poss_p_i[-1]] - points[poss_p_i[0]]) >= dis_thresh:
            return True
    return False