# Given an array arr[ ] of size N having distinct elements, 
# the task is to find the next greater element for each 
# element of the array in order of their appearance in the array.

# Input: 
# N = 4, arr[] = [1 3 2 4]
# Output:
# 3 4 4 -1

# Approach
# Use a stack to save next larger numbers and while traversing 
# from right to left.


def previousLargerElement(arr,n):
    stack = [ ]                
    res = [ ]                   
    i = 0
    while i<n:
        #when no element in stack
        if not stack:
                res.append(-1)    
        # when top is larger(as we wanted)             
        elif stack[ -1 ]>arr[ i ]:
                res.append(stack[-1])      
        # if top is smaller(pop top until larger element is got)
        elif stack[ -1 ]<=arr[ i ]:
                stack.pop()
                continue  
        stack.append( arr[ i ] )
        i += 1
    return (res)
            

a = list(map(int,input().strip().split()))
n=len(a)
res = previousLargerElement(a,n)
for i in range (len (res)):
    print (res[i], end = " ")
print ()
