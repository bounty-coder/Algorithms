# Given an array arr of size n and an integer x. Find if there's a triplet in the array which sums up to the given integer x. if not return 0.
# Input:n = 6, x = 13, arr[] = [1,4,45,6,10,8]
# Output: 1
# Explanation: The triplet {1, 4, 8} in the array sums up to 13.


#Method 1 : Hashing
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
