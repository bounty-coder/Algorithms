# Input: arr = [1,1,2,3,3,4,4,8,8]
# Output: 2

def singleNonDuplicate(arr):
    n=len(arr)
    if n==1:
        return arr[0]
    if arr[0]!=arr[1]:
        return arr[0]
    start,last=0,n-1
    while start<last:
        mid=start+(last-start)//2
        even=(last-mid)%2
        
        if arr[mid]==arr[mid-1]:
            if even==0:
                last=mid-2
            else:
                start=mid+1
                
        elif arr[mid]==arr[mid+1]:
            if even==0:
                start=mid+2
            else:
                last=mid-1
        else:
            return arr[mid]
    return arr[start]

arr=[1,1,2,3,3,4,4,8,8]
print(singleNonDuplicate(arr))