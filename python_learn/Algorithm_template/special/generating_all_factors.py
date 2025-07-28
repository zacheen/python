# all factors, all divisors
# generating all the factors of every nums : O(nlogn)
# this part have to put outside the function become static, preventing recalculate
MAX = 10 ** 5 + 1
fac = [[] for _ in range(MAX)]
for i in range(1, MAX):
    for j in range(i, MAX, i):
        fac[j].append(i)

print("fac :",fac[5])
print("fac :",fac[6])
print("fac :",fac[100])
print("fac :",fac[121])

# only contain prime factor (1 is not a prime)
MAX = 10 ** 5 + 1
prime_fac = [[] for _ in range(MAX)]
for i in range(2, MAX): # 這裡得要是 MAX，因為質數還是有因數那就是自己
    if not prime_fac[i] : # 若沒有任何的因數 代表是質數
        for j in range(i, MAX, i):
            prime_fac[j].append(i)

#但要記得 判斷是不是質數是用
def judge_prime(num):
    return len(prime_fac[num]) == 1
print("judge_prime :",judge_prime(1))
print("judge_prime :",judge_prime(5))

print("prime_fac :",prime_fac[5])
print("prime_fac :",prime_fac[6])
print("prime_fac :",prime_fac[12]) # 因為只包含質數因數，所以並不包含 4
print("prime_fac :",prime_fac[100])
print("prime_fac :",prime_fac[121])


# classic : 3447. Assign Elements to Groups with Constraints
# https://leetcode.com/problems/assign-elements-to-groups-with-constraints/description/

# identify all prime numbers
# MAX = 10 ** 5 + 1
MAX = 100
prime = [True]*MAX
prime[0] = False
prime[1] = False
for i in range(2, int(MAX**(1/2)+1)):
    if prime[i]:
        for j in range(i*i, MAX, i):
            prime[j] = False

print("Prime numbers up to", MAX, ":")
for i in range(MAX):
    if prime[i]:
        print(i, end=' ')
