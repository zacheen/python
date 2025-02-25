# checking n1, n2 is in the biggest number
ll = list(range(10,-1,-1))

# # test case
# n1 = 9
# n2 = 10
# # test case
# n1 = 10
# n2 = 9
# # test case
# n1 = 5
# n2 = 10
# # test case
# # 這個 test case 是 0 !! (因為不包含最大的數)
n1 = 5
n2 = 9
# # test case
# # Invalid!! (因為最大的兩個數是 10 跟 9，不可能出現兩個 10)
# n1 = 10
# n2 = 10

indx = 0
if (max(n1, n2) == ll[indx]):
    indx += 1
if (min(n1, n2) == ll[indx]):
    indx += 1

if indx == 0 :
    print("both are not the biggest number")
elif indx == 1 :
    print("one of it is the biggest number")
elif indx == 2 :
    print("both number are the top 2 biggest number")

# classic : 3440. Reschedule Meetings for Maximum Free Time II
# https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-ii/description/


