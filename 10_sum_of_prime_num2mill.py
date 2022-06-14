# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

x = 2000000
ans = 0

for i in range(2, x+1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            ans = ans+i
print("Ans", ans)



# 142913828922