# n! means n × (n − 1) × ... × 3 × 2 × 1
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
# Find the sum of the digits in the number 100!

import math

lst = []
ans = 0
tot = math.factorial(100)
lst.append(str(tot))
for i in lst:
    for j in i:
        ans += int(j)

print("Answer is: ",ans)
