# Given a binary matrix, find the maximum size rectangle 
# binary-sub-matrix with all 1’s. 

#    Input:
#    0 1 1 0
#    1 1 1 1
#    1 1 1 1
#    1 1 0 0
# Output : 8

# approach
# See through the previous problem, try to make histograms.
# starting from 0th row, add previous row height to current row 
# for each column. If height is 0 somewhere, make the height of 
# building 0(hawe p to rhegi nhi building)
# modified array will be for above example:

# 0 1 1 0
# 1 2 2 1
# 2 3 3 2
# 3 4 0 0
        
def maxArea(M, n, m):
    ls=[[0 for i in range(m)] for j in range(n)]
    for i in range(n):
        for j in range(m):
            if i==0:
                ls[i][j]=M[i][j]
            elif M[i][j]==0:
                ls[i][j]=0
            else:
                ls[i][j]=ls[i-1][j]+M[i][j]
                
    arr=[]
    for i in range(n):
        arr.append(getMaxArea(ls[i]))
    
    return max(arr)

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
            
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

R,C = map(int, input().strip().split())
A = []
for i in range(R):
    line = [int(x) for x in input().strip().split()]
    A.append(line)
print(maxArea(A, R, C)) 

# } Driver Code Ends