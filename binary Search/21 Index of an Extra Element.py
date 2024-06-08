# You have given two sorted arrays arr1[] & arr2[] of distinct elements. The first array has one element extra added in between. Return the index of the extra element.
# Note: 0-based indexing is followed.

'''
  Input: n = 7, arr1[] = {2,4,6,8,9,10,12}, arr2[] = {2,4,6,8,10,12}
  Output: 4
  Explanation: In the first array, 9 is extra added and it's index is 4.
'''


# TC- O(n)
def findExtra(n,a,b):
    i,j=0,0
    while i<n and j<n:
        if j==n-1:
            return i
        if a[i]!=b[j]:
            return i
        i+=1
        j+=1




# TC- O(logn)
def findExtra(n,a,b):
    first=0
    last =n-2
    while first<=last:
      mid=first+(last-first)//2
      if a[mid]==b[mid]:
          first=mid+1
      else:
          last=mid-1
    return first
