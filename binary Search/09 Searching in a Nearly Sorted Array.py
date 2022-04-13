# Searching in a Nearly Sorted Array
# Given an array which is sorted, but after sorting some elements
#  are moved to either of the adjacent positions, i.e., arr[i] may
#  be present at arr[i+1] or arr[i-1]. Write an efficient function
#  to search an element in this array. Basically the element arr[i]
#  can only be swapped with either arr[i+1] or arr[i-1].

# For example consider the array {2, 3, 10, 4, 40}, 4 is moved to
#  next position and 10 is moved to previous position.

# ip= [5,10,30,20,40]
# k= 30
# op= 2

def almostsorted(arr,k):
    n=len(arr)
    start,last=0,n-1
    while start<=last:
        mid=(start+last)//2
        if k==arr[mid]:
            return mid
        if mid>start and arr[mid-1]==k:
            return mid-1
        if mid<last and arr[mid+1]==k:
            return mid+1
        if arr[mid]<k:
            start=mid+2
        if arr[mid]>k:
            last=mid-2
    return -1

arr=[5,10,30,20,40]
k=30
print(almostsorted(arr,k))