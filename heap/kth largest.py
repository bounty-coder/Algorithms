
# 1) Build a Max Heap tree in O(n) 
# 2) Use Extract Max k times to get k maximum 
# elements from the Max Heap O(k*log(n))



# TC- O(n + (n-k)*log(k)) 
import heapq
# 1
# @param A : list of integers
# @param B : integer
# @return a list of integers
def solve(A, B):
    heapq.heapify(A)
    for i in range(len(A)-B):
        heapq.heappop(A)
    return A

#2  TC- O(n + (n-k)*log(k))
#creating a min heap by making neg of each number.
def kthLargest(arr, size, k):
    pq = []
    for i in range(size):
        heapq.heappush(pq, -1 * arr[i])

    l = k - 1
    while l > 0:
        heapq.heappop(pq)
        l = l - 1 
    return -1 * pq[0]