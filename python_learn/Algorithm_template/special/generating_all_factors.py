# all factors, all divisors
# generating all the factors of every nums : O(nlogn)
# this part have to put outside the function become static, preventing recalculate
MAX = 10 ** 5 + 1
fac = [[] for _ in range(MAX)]
for i in range(1, MAX):
    for j in range(i, MAX, i):
        fac[j].append(i)

print("fac :",fac[6])
print("fac :",fac[100])
print("fac :",fac[121])

# classic : 3447. Assign Elements to Groups with Constraints
# https://leetcode.com/problems/assign-elements-to-groups-with-constraints/description/

# identify all prime numbers
# MAX = 10 ** 5 + 1
MAX = 100
prime = [True]*MAX
prime[0] = False
prime[1] = False
for i in range(2, int(MAX**(1/2)+1)):
    if not prime[i]:
        continue
    for j in range(i*i, MAX, i):
        prime[j] = False

print("Prime numbers up to", MAX, ":")
for i in range(MAX):
    if prime[i]:
        print(i, end=' ')
