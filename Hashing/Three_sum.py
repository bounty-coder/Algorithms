# Given an array arr of size n and an integer x. Find if there's a triplet in the array which sums up to the given integer x. if not return 0.
# Input:n = 6, x = 13, arr[] = [1,4,45,6,10,8]
# Output: 1
# Explanation: The triplet {1, 4, 8} in the array sums up to 13.


#Method 1 : Hashing
'''Fix the first element, the second will start from the first+1. 
Then sum both first and second element and find the remaining sum.
If remaining number is found in set then the triplet is available.

TC- O(n^2)
SC- O(n)   set is using extra space
'''
def find3Numbers(arr, n, x):
    if n<3:
        return 0
    arr.sort()
    target=0
    for i in range(n-2):
        s=set()
        if arr[i]>x:
            return 0
        for j in range(i+1,n):
            sumij = arr[i]+arr[j]
            remaining=x-sumij
            if remaining in s:
                # print(arr[i],arr[j])
                # print(s)
                return 1
            s.add(arr[j])
    return 0

#Method 2: Two Pointer
'''
First we will sort the array, and fix the first element
Apply two pointer on rest of the array. 
If sum==target then we will return all the three elements
else if sum<target then we will increase the second element
else we will decrease the last element
'''
def find3Numbers(arr, n, x):
    if n<3:
        return 0
    arr.sort()
    # target=0
    for i in range(n-2):
        j,k=i+1,n-1
        while j<k:
            s=arr[i]+arr[j]+arr[k]
            if s==x:
                return 1
            elif s<x:
                j+=1
            else:
                k-=1
    return 0
