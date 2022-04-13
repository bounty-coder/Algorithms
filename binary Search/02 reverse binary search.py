# reverse binary search
# [10,8,5,3,1]

def findk(arr,l,r,k):
    if l<=r:
        mid=l+(r-l)//2
        if k==arr[mid]:
            return mid
        elif k<arr[mid]:
            return findk(arr,mid+1,r,k)
        else:
            return findk(arr,l,mid-1,k)
    else:
        return -1

arr=list(map(int,input().split()))
n=len(arr)
k=int(input())
print(findk(arr,0,n-1,k))