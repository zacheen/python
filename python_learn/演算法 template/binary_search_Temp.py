# 這幾中template不同在於 "跳出迴圈的條件不同"
    # 1 : left 會越過 right
    # 2 : left right 會碰到 但不會越過彼此
    # 3 : left right 不會碰到 (我習慣用這種)

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
    if len(nums) == 0:
        return -1

    left, right = 0, len(nums)
    # left right 會碰到 但不會越過彼此
    while left < right:
        mid = (left + right) // 2
        print(left, mid, " : ", nums[left], nums[mid])
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid

    # End Condition: left == right
    if left != len(nums) and nums[left] == target:
        return left
    return -1

# print(binarySearch2([2,4,5,6,7], 4))
# print(binarySearch2([2,4,5,6,7], 3))

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
for i in range(1,12) :
    print(binarySearch_adv([2,4,6,8,10], i))

