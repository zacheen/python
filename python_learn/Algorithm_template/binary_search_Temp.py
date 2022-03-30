# 這幾中template不同在於 "跳出迴圈的條件不同"
    # 1 : left 會越過 right 
        # 如果right會用到 且 不需要回傳找不到的位置(其實是不是就是 right 的位置阿 ??)
    # 2 : left right 會碰到 但不會越過彼此      
        # 最好用在 找 某個東西的時候  "找不到時可以回傳要插入的位置"   
        # 注意 一定要有 left = mid + 1 或 right = mid - 1
    # 3 : left right 不會碰到   
        # 最好用在 r l 有相對關係的時候  要回傳哪一個的判斷就很簡單

# (l+r) // 2 都可以換成 (l+r) >> 1

def binarySearch1(nums, target):
    if len(nums) == 0:
        return -1

    left, right = 0, len(nums) - 1
    # left 會越過 right
    while left <= right:
        mid = (left + right) // 2
        print(left, mid, right, " : ", nums[left], nums[mid], nums[right])
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1 # 這裡是 left 會大於 right 的原因
        else:
            right = mid - 1
    print(left, right)

    # End Condition: left > right
    return -1

# print(binarySearch1([2,4,5,6,7], 4))
# print(binarySearch1([2,4,5,6,7], 3))

def binarySearch2(nums, target):
    # 其實不用
    # if len(nums) == 0:
    #     return -1

# 不懂為什麼是 len(nums) 而不是 len(nums)-1 ?
# 這是因為 0 ~ len() 這樣有 len()+1 個位置  最後結果就算找不到項目 也可以知道要找的項目可以插入的位置
    left, right = 0, len(nums)  
    # left right 會碰到 但不會越過彼此
    while left < right:
        mid = (left + right) // 2 # 曾經看到 mid = l + (r - l) // 2 竟然就不用判斷下面的 nums[left] == target ??
        # print(left, mid, " : ", nums[left], nums[mid])
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid

    # Post-processing:
    # End Condition: left == right
    if left != len(nums) and nums[left] == target:  #而且是真的需要的ㄟ
        return left
    return -1
    # 不懂為什麼要 left != len(nums) ? 
    # 解釋範例  註解上面
    # if left == len(nums) :
    #     return str(target)+"的範圍在 " + str(left) + " 之後"
    # elif nums[left] == target:
    #     return left
    # elif left == 0 :
    #     return str(target)+"的範圍在 " + str(0) + " 之前"
    # else :
    #     return str(target)+"的範圍在 " + str(left-1) + " 到 " + str(left) + " 之間"

# print(binarySearch2([2,4,5,6,7], 4))
# print(binarySearch2([2,4,5,6,7], 3))
for i in range(1,12) :
    print(binarySearch2([2,4,6,8,10], i))

def binarySearch3(nums, target):
    if len(nums) == 0:
        return -1

    left, right = 0, len(nums) - 1
    while left + 1 < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid
        else:
            right = mid

    # Post-processing:
    # End Condition: left + 1 == right
    if nums[left] == target: return left
    if nums[right] == target: return right
    return -1

# print(binarySearch3([2,4,5,6,7], 4))
# print(binarySearch3([2,4,5,6,7], 3))

# 我習慣用這種 因為最簡單
def binarySearch_adv(nums, target):
    left, right = 0, len(nums) - 1
    # left right 不會碰到
    while left + 1 < right:
        mid = (left + right) // 2
        # 這裡我移除 少一次判斷
        # if nums[mid] == target:
        #     return mid
        if nums[mid] < target:
            left = mid
        else:
            right = mid

    # End Condition: left + 1 == right
    if nums[left] == target: return left
    if nums[right] == target: return right
    return -1

# 確認每個位置都不會出問題
# for i in range(1,12) :
#     print(binarySearch_adv([2,4,6,8,10], i))

