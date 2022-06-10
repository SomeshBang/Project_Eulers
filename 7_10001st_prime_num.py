# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

a = 1
b = 2
c = []

for a in range(2, 200000):
    if a % 2 != 0:
        for b in range(3, a):
            if a % b == 0:
                break
        else:
            c.append(a)
print(c[9999])
