# returning the index of the floor number
def findFloor(arr,n,k):
    start,last=0,n-1
    res=-1
    while start<=last:
        mid=start+(last-start)//2
        if arr[mid]==k:
            return mid
            
        elif arr[mid]<k:
            res=mid  # a valid candidate
            start=mid+1
        elif arr[mid]>k:
            last=mid-1
    return res


arr=list(map(int,input("Enter a sorted array").split()))
n=len(arr)
k=int(input())
print(findFloor(arr,n,k))