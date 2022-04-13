# Find the largest rectangular area possible in a given histogram
# where the largest rectangle can be made of a number of contiguous
#  bars. For simplicity, assume that all bars have the same width
#  and the width is 1 unit, there will be N bars height of each 
# bar will be given by the array arr.

# N = 7
# arr[] = {6,2,5,4,5,1,6}
# Output: 12

def getMaxArea(histogram):
    n=len(histogram)
    stack=[]
    # array to store smaller number left side
    left_small=[]
    i=0
    while i<n:
        if not stack:
            left_small.append(-1)
        elif histogram[stack[-1]]<histogram[i]:
            left_small.append(stack[-1])
        elif histogram[stack[-1]]>=histogram[i]:
            stack.pop()
            continue
        stack.append(i)
        i+=1
    
    # array to store smaller number right side 
    right_small,stack=[],[]
    i=n-1
    while i>=0:
        if not stack:
            right_small.append(n)
        elif histogram[stack[-1]]<histogram[i]:
            right_small.append(stack[-1])
        elif histogram[stack[-1]]>=histogram[i]:
            stack.pop()
            continue
        stack.append(i)
        i-=1
    
    
    maxi=float("-inf")
    for i in range(n):
        k=histogram[i]*(abs(left_small[i]-right_small[n-i-1])-1)
        maxi=max(k,maxi)
    return maxi
            

#{ 
#  Driver Code Starts

n = int(input())
a = list(map(int,input().strip().split()))

print(getMaxArea(a))
# } Driver Code Ends


#optimised code

def getMaxArea(histogram):
        
    #creating an empty stack. The stack holds indexes of histogram[] array.
    #bars stored in stack are always in increasing order of their heights.
    stack = list()

    max_area = 0   

    index = 0
    #traversing the array.
    while index < len(histogram):

        #if current bar is greater than or equal to bar on top 
        #of stack, we push the index into stack.
        if (not stack) or (histogram[stack[-1]] <= histogram[index]):
            stack.append(index)
            index += 1

        #if current bar is lower than bar on top of stack, we calculate
        #area of rectangle with top of stack as the smallest bar.  
        #i is rightindex for top and element before top in stack is leftindex
        else:
            
            #popping the top element of stack.
            top_of_stack = stack.pop()

            #calculating the area with hist[tp] stack as smallest bar.
            area = (histogram[top_of_stack] *
                    ((index - stack[-1] - 1)
                        if stack else index))

            #updating maximum area, if needed.
            max_area = max(max_area, area)

    #now popping the remaining bars from stack and calculating 
    #area with every popped bar as the smallest bar.
    while stack:
        
        top_of_stack = stack.pop()
        area=(histogram[top_of_stack] *
                ((index - stack[-1] - 1)
                    if stack else index))

        #updating maximum area, if needed.
        max_area = max(max_area, area)

    #returning the maximum area.
    return max_area