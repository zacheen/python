# generating all the factors of every nums : O(nlogn)
# this part have to put outside the function become static, preventing recalculate
MAX = 10 ** 5 + 1
fac = [[] for _ in range(MAX)]
for i in range(1, MAX):
    for j in range(i, MAX, i):
        fac[j].append(i)

print(fac[6])
print(fac[100])
print(fac[121])

# classic : 3447. Assign Elements to Groups with Constraints
# https://leetcode.com/problems/assign-elements-to-groups-with-constraints/description/

