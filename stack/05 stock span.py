# The span Si of the stocks price on a given day i is defined 
# as the maximum number of consecutive days just before the given
#  day, for which the price of the stock on the current day is 
# less than or equal to its price on the given day.

# N = 7, price[] = [100 80 60 70 60 75 85]
# Output:
# 1 1 1 2 1 4 6

#approach 
# to find the all the smaller elements that means find the previous 
# larger element ie nearest greater to left. Then arrange the 
# output accordingly 
def calculateSpan(a,n):
    stack=[]
    res=[]
    i=0
    while i<n:
        if not stack:
            res.append(-1)
        elif a[stack[-1]]>a[i]:
            res.append(stack[-1])
        elif a[stack[-1]]<=a[i]:
            stack.pop()
            continue
        # save the index of nearest greater to left no
        stack.append(i)
        i+=1
    # modify res to i-res
    for i in range(n):
        res[i]=i-res[i]
    return res


a = list(map(int,input().strip().split()))
n=len(a)
ans = calculateSpan(a, n);
for i in range(n):
    print(ans[i],end=" ")
print()            
