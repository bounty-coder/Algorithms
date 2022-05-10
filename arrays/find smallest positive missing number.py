# Given an unsorted integer array, find the first missing positive integer.
# I/p=> [1,2,0] return 3,
# I/p=> [3,4,-1,1] return 2,
# I/p=> [-8, -7, -6] returns 1

#other approach
# 1. sorting 2. Hashing

# Your algorithm should run in O(n) time and use constant space.

def firstMissingPositive(arr, n):
    # Loop to traverse the whole array
    for i in range(n):
        # Loop to check boundary
        # condition and for swapping
        while (arr[i] >= 1 and arr[i] <= n
               and arr[i] != arr[arr[i] - 1]):
            temp = arr[i]
            arr[i] = arr[arr[i] - 1]
            arr[temp - 1] = temp
     
    # Checking any element which
    # is not equal to i+1
    for i in range(n):
        if (arr[i] != i + 1):
            return i + 1
         
    # Nothing is present return last index
    return n + 1
 
# Driver code
arr = [ 2, 3, -7, 6, 8, 1, -10, 15 ];
n = len(arr)
ans = firstMissingPositive(arr, n)
print(ans)
