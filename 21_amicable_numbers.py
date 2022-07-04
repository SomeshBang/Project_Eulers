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
