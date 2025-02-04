# affect_range

arr = [4,1,3,2,5,0,7]
print(arr)

len_arr = len(arr)
left = [0]*len_arr
right = [0]*len_arr
stack = []
for i, now_n in enumerate(arr):
    while stack and arr[stack[-1]] > now_n:
        stack.pop()
    left[i] = i - (stack[-1] if stack else -1) - 1
    stack.append(i)
stack = []
for i, now_n in zip(range(len_arr-1, -1, -1), arr[::-1]):
    while stack and arr[stack[-1]] >= now_n:
        stack.pop()
    right[i] = (stack[-1] if stack else len_arr) - i - 1
    stack.append(i)

print(left)
print(right)
i = 3
print("index",i,"是範圍左邊",left[i],"個與右邊",right[i],"個之間的最小值")
print("也就是 index", i-left[i], "~", i+right[i], "之間的最小值")