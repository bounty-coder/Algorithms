# Given two sorted arrays nums1 and nums2 of size m and n respectively, 
# return the median of the two sorted arrays.

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.

# "if we cut the sorted array to two halves of EQUAL LENGTHS, then
# median is the AVERAGE OF Max(lower_half) and Min(upper_half), i.e. the
# two numbers immediately next to the cut".
# Now, we do partition of array A and accordingly array B will be partitioned
# as,total element in leftside partition(left_A+left_B)=(right_A+right_B)
#check if max_left_A < min_right_B and max_left_B < min_right_A
# if yes then find the median else go accordingly
# max_left_A > min_right_B => right_A = partition_A - 1
# max_left_B > min_right_A => left_A = partition_A + 1

# binary search, divide the array and find median
#TC- O(min(log(m),log(n))), SC- O(1) 
import math
class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a double
    def findMedianSortedArrays(self, A, B):

        m = len(A)
        n = len(B)

        if m > n:
            A, B, m, n = B, A, n, m
        
        left_A = 0
        right_A = m

        while left_A <= right_A:
            partition_A = (left_A + right_A) // 2
            partition_B = (m + n + 1) // 2 - partition_A

            max_left_A = A[partition_A - 1] if partition_A >= 0 else -float('inf')
            min_right_A = A[partition_A] if partition_A <= m else float('inf')

            max_left_B = B[partition_B - 1] if partition_B != 0 else -float('inf')
            min_right_B = B[partition_B] if partition_B != n else float('inf')

            if max_left_A > min_right_B:
                right_A = partition_A - 1
            elif max_left_B > min_right_A:
                left_A = partition_A + 1
            else:
                if (m + n) % 2:
                    return max(max_left_A, max_left_B)
                else:
                    return (max(max_left_A, max_left_B) + min(min_right_A, min_right_B)) / 2.0