# 可隨意調換陣列順序，找出相差總和的最小值
def min_diff(arr1, arr2) :
    arr1.sort()
    arr2.sort()
    return sum(abs(n1-n2) for n1,n2 in zip(arr1, arr2))

arr1 = [-7,9,5]
arr2 = [7,-2,-5]
print( min_diff(arr1,arr2) )

print( min_diff([1,2,3],[3,1,2]) )