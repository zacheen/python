import random

# 固定取最後一個點來當 pivot
def quickSelect(l: int, r: int, k: int):
    pivot = points[r]

    nextSwapped = l
    for i in range(l, r):
        if points[i] <= pivot:
            points[nextSwapped], points[i] = points[i], points[nextSwapped]
            nextSwapped += 1
    points[nextSwapped], points[r] = points[r], points[nextSwapped]

    count = nextSwapped - l + 1  # of points <= pivot
    if count == k:
        return
    if count > k:
        quickSelect(l, nextSwapped - 1, k)
    else:
        quickSelect(nextSwapped + 1, r, k - count)

# k = 5
# points = [random.randint(1, 50) for i in range(20)]
# quickSelect(0, len(points) - 1, k)
# print(points[0:k])
# print(points)


# 取隨機點當 pivot
def quickSelect_rand(l: int, r: int, k: int):
    # 隨機選擇一點 換到最後面
    randIndex = random.randint(l, r)
    points[randIndex], points[r] = points[r], points[randIndex]
    
    pivot = points[r]

    nextSwapped = l
    for i in range(l, r):
        if points[i] <= pivot:
            points[nextSwapped], points[i] = points[i], points[nextSwapped]
            nextSwapped += 1
    points[nextSwapped], points[r] = points[r], points[nextSwapped]

    count = nextSwapped - l + 1  # of points <= pivot
    if count == k:
        return
    if count > k:
        quickSelect(l, nextSwapped - 1, k)
    else:
        quickSelect(nextSwapped + 1, r, k - count)

# k = 5
# points = [random.randint(1, 50) for i in range(20)]
# quickSelect_rand(0, len(points) - 1, k)
# print(points[0:k])
# print(points)

# k = 3
# points = [1,4,7,3,5,6,2,3]
# quickSelect_rand(0, len(points) - 1, k)
# print(points[0:k])
# print(points)


