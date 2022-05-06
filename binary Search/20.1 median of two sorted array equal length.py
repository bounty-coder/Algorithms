# There are 2 sorted arrays A and B of size n each. 
# Write an algorithm to find the median of the array 
# obtained after merging the above 2 arrays

#  ar1[] = {1, 12, 15, 26, 38}
#  ar2[] = {2, 13, 17, 30, 45}

# o/p- 16

# 1) Calculate the medians m1 and m2 of the input arrays ar1[] 
#    and ar2[] respectively.
# 2) If m1 and m2 both are equal then we are done.
#      return m1 (or m2)
# 3) If m1 is greater than m2, then median is present in one 
#    of the below two subarrays.
#     a)  From first element of ar1 to m1 (ar1[0...|_n/2_|])
#     b)  From m2 to last element of ar2  (ar2[|_n/2_|...n-1])
# 4) If m2 is greater than m1, then median is present in one    
#    of the below two subarrays.
#    a)  From m1 to last element of ar1  (ar1[|_n/2_|...n-1])
#    b)  From first element of ar2 to m2 (ar2[0...|_n/2_|])
# 5) Repeat the above process until size of both the subarrays 
#    becomes 2.
# 6) If size of the two arrays is 2 then use below formula to get 
#   the median.
#     Median = (max(ar1[0], ar2[0]) + min(ar1[1], ar2[1]))/2

# TC-O(log(n)) and SC-O(1)
def getMedian(arr1,arr2,n):
    if n==0:
        return -1
    elif n==1:
        return (arr1[0]+arr2[0])/2
    elif n==2:
        return (max(arr1[0],arr2[0])+min(arr1[1],arr2[1]))/2
    else:
        m1=median(arr1,n)
        m2=median(arr2,n)
        
        if m1>m2:
            if n%2==0:
                return getMedian(arr1[:n//2+1],arr2[n//2-1:],n//2+1)
            else:
                return getMedian(arr1[:n//2+1],arr2[n//2:],n//2+1)
        
        else:
            if n%2==0:
                return getMedian(arr1[n//2-1:],arr2[:n//2+1],n//2+1)
            else:
                return getMedian(arr1[n//2:],arr2[:n//2+1],n//2+1)

def median(arr,n):
    if n%2==1:
        return arr[n//2]
    else:
        return (arr[n//2]+arr[n//2-1])/2

arr1=[1,3,6,8]
arr2=[2,4,5,7]
n=len(arr1)
print(getMedian(arr1,arr2,n))