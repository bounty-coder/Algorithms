# Given an array A containing N integers.
# You need to find the maximum sum of triplet ( Ai + Aj + Ak )
#  such that 0 <= i < j < k < N and Ai < Aj < Ak.
# If no such triplet exist return 0.



from bisect import bisect_left
def BinarySearch(a, x):
    i = bisect_left(a, x)
    if i:
        return i - 1
    else:
        return -1


class Solution:

    # @param A : list of integers
    # @return an integer

    def solve(self, A):
        n = len(A)
        dp = [0] * n
        dp[n - 1] = A[n - 1]
        for i in range(n - 2, -1, -1):
            dp[i] = max(dp[i + 1], A[i])
        lst = []
        maxe = 0
        lst.append(A[0])
        for i in range(1, n - 1):
            res = BinarySearch(lst, A[i])
            if res != -1 and A[i]<dp[i+1]:
                ans = lst[res] + A[i] + dp[i + 1]
                maxe = max(maxe, ans)
            lst.insert(res + 1, A[i])
        return maxe
        return 0