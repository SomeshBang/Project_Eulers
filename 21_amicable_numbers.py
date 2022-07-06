# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
# Evaluate the sum of all the amicable numbers under 10000.

lst = []

for i in range(2,10000):
    divisior = i // 2 + 2
    f_num = 0
    s_num = 0
    for j in range(1,divisior):
        if i%j == 0:
            f_num += j
    divisior_sec = f_num //2 + 2
    for k in range(1,divisior_sec):
        if f_num % k == 0:
            s_num += k
    if i == s_num and i != f_num:
        lst.append(i)
print(sum(lst))
