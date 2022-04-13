# Given an array a of integers of length n, find the nearest
#  smaller number for every element such that the smaller 
# element is on left side.
# If no small element present on the left print -1.

# Input: n = 3
# a = {1, 6, 2}
# Output: -1 1 1

def leftSmaller(n, a):
    # code here
    stack=[]
    res=[]
    i=0
    while i<n:
        if not stack:
            res.append(-1)
        elif stack[-1]<a[i]:
            res.append(stack[-1])
        elif stack[-1]>=a[i]:
            stack.pop()
            continue
        stack.append(a[i])
        i+=1
    return res

        
a = input().split()
n = len(a)
for i in range(n):
    a[i] = int(a[i])
ans = leftSmaller(n, a)
for u in(ans):
    print(u,end = " ")
print()
