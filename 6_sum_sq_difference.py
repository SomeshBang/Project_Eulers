# The sum of the squares of the first ten natural numbers is, 1**2+2**2+3**2+4**2 ....100**2 = 385
# The square of the sum of the first ten natural numbers is,(1+2+3+4....100)**2 = 3025
# Hence the difference between the sum of the squares of the first ten natural
# numbers and the square of the sum is3025-385 = 2640 .Find the difference between the sum of the squares of 
# the first one hundred natural numbers and the square of the sum

sq_all,sq_single = 0,0
for sq in range(1,101):
    sq_single = sq_single + sq**2
    sq_all = sq_all +sq
diff = (sq_all**2)-sq_single
print(diff)
