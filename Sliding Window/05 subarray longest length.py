#Given an array arr[] of size n containing integers. 
# The problem is to find the length of the 
# longest sub-array having sum equal to the given value k.

# Input : arr[] = { 10, 5, 2, 7, 1, 9 }, 
#             k = 15
# Output : 4

# sliding window concept will apply only on positive numbers
# Below code is only for positive numbered array

def findLongestLength(arr,k):
    s,l=0,0
    i,j=0,0
    n=len(arr)
    while j<n:
        s+=arr[j]
        if s<k:
            j+=1
        elif s==k:
            l=max(l,j-i+1)
            j+=1
        else:
            while s>k:
                s-=arr[i]
                i+=1
            if s==k:
                l=max(l,j-i+1)
            j+=1
        
    return l


arr=list(map(int,input().split()))
k=int(input())
print(findLongestLength(arr,k))