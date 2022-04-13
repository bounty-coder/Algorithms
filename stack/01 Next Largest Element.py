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

class Solution:
    def nextLargerElement(self,arr,n):
        stack = [ ]                
        res = [ ]                   
        i = n - 1
        while i>=0:
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
            i -= 1
        return (res[::-1])
                
                

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())

        a = list(map(int,input().strip().split()))
        obj = Solution()
        res = obj.nextLargerElement(a,n)
        for i in range (len (res)):
            print (res[i], end = " ")
        print ()
# } Driver Code Ends