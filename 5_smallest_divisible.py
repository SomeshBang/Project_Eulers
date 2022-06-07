# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20


num = 1
count=0

while num >= 1:
    if num%2==0:
        for i in range(1,21):
            ans=num%i
            if ans == 0:
                count+=1
            else:
                break
            if count == 20:
                print(num)
            i+=1
        count=0
    num+=1