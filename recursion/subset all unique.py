# Given an array arr[] of integers of size N that might contain duplicates,
#  the task is to find all possible unique subsets.
# Input: N = 4, arr[] = {1,2,3,3}
# Output: (),(1),(1 2),(1 2 3),(1 2 3 3),(1 3),(1 3 3),(2),(2 3)
# (2 3 3),(3),(3 3)

#Backtracking
#take a set for saving unique subsets

def solve(s,ou,res):
    if len(s)==0:
        res.add(tuple(ou))
        return
    ou1 = ou[:]
    ou2 = ou[:]
    ou2.append(s[0])
    s = s[1:]
    # not pick
    solve(s,ou1,res)
    # pick
    solve(s,ou2,res)

def recursion(s,n):
    ou = []
    res = set()
    s.sort()
    solve(s,ou,res)
    res = list(res)
    res.sort()
    return res

ip=list(map(int,input().split()))
n=len(ip)
print(recursion(ip,n))