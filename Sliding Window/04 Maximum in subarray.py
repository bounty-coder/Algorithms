# Given an array and an integer K,
# find the maximum for each and every contiguous subarray of size k.

# Input: arr[] = {1, 2, 3, 1, 4, 5, 2, 3, 6}, K = 3 
# Output: 3 3 4 5 5 5 6

from collections import deque
# A Deque (Double ended queue) based
# method for printing maximum element
# of all subarrays of size k


def slidingMaximum( A, k):
    n=len(A)
    """ Create a Double Ended Queue, q that
will store indexes of array elements.
The queue will store indexes of useful
elements in every window and it will
maintain decreasing order of values from
front to rear in q, i.e., arr[q.front[]]
to arr[q.rear()] are sorted in decreasing
order"""
    q=deque()
    ls=[]
    for i in range(0,n):
            # Remove the elements which are
        # small and out of this window
        if q and q[0]==i-k:
            q.popleft()
        # Remove all elements smaller than
        # the currently being added element
        # (Remove useless elements)
        while q and A[i]>=A[q[-1]]:
            q.pop()
        # Add current element at the rear of Qi
        q.append(i)
        if i>=k-1:
            # append maximum
            ls.append(A[q[0]])
    return ls

ls=list(map(int,input().split()))
k=int(input())
print(slidingMaximum( ls, k))