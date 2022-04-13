# find next smaller 

# Input: N = 5, arr[] = {3, 8, 5, 2, 25}
# Output: 2 5 2 -1 -1
def help_classmate(arr, n):
    stack=[]
    res=[]
    i=n-1
    while i>=0:
        if not stack:
            res.append(-1)
        elif stack[-1]<arr[i]:
            res.append(stack[-1])
        elif stack[-1]>=arr[i]:
            stack.pop()
            continue
        stack.append(arr[i])
        i-=1
    return res[::-1]


arr = [ int(x) for x in input().split() ]
n=len(arr)
result = help_classmate(arr,n)
for i in result:
    print(i,end=' ')
print()