# 2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2**1000?
num = int(input("Enter number : "))
power = int(input("Enter power : "))
lst = []
x = 0
z = num**power
lst.append(str(z))
for i in lst:
    for j in i:
        x += int(j) 

print(x)
