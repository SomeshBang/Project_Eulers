# The following iterative sequence is defined for the set of positive integers:
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?
# Note: Once the chain starts the terms are allowed to go above one million

chain = []
ct = 0
ans=[]
for num in range(1000000,1,-1):

    chain.append(num)
    while num > 1:
        if num % 2 == 0:
            ev = num/2
            chain.append(int(ev))
            num = ev
        else:
            od = 3*num+1
            chain.append(int(od))
            num = od
    count = len(chain)
    # print(chain,count)
    if ct < count:
        ans.clear()
        ct = count
        ans.append(chain)
    chain = []


# print("Longest Chain",ans)
# print("Total count",ct)
for i in ans:
    print("Ans: ",i[0])