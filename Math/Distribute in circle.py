# B items are to be delivered in a circle of size A.

# Find the position where the Bth item will be delivered 
# if we start from a given position C.

# A- size of circle
# B- number of items
# C- starting position
def solve(B,A,C):
    z=(C+B-1)%A
    if z==0:
        return A 
    else:
        return z

A=int(input())
B=int(input())
C=int(input())
print(solve(B,A,C))