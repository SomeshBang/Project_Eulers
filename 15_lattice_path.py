'''
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, 
there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?
'''


import math
grid1 = int(input("Enter grid size (Height) = "))
grid2 = int(input("Enter grid size (Width) = "))

# Lattice path Formula (a+b  a)
nu = grid1 + grid2
de = grid1

# Solving using binomial coefficent
# (n   k) = n!/k!(n-k)!

sub = nu - de
n = math.factorial(nu)
k = math.factorial(de)
sub_fact = math.factorial(sub)

x = k*sub_fact
print("Total is : ",int(n/x))














# # Just based on calculations

# z = nu - de
# n = 1
# k = 1
# o = 1

# for i in range(1,nu+1):
#     n *= i

# for j in range(1,de+1):
#     k *= j

# for l in range(1,z+1):
#     o *= l

# deno = k*o
# print("Total is : ",int(n/deno))