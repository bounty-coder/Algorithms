# Given an array of N integers, find the sum of xor of 
# all pairs of numbers in the array.

# Input : arr[ ] = {7, 3, 5}
# Output : 12

# At any place value 
# (count_zero + count_one+ 2^placevalue= ans)
# 7 = 111 , 3 = 011 , 5 = 101
# For bit position 0 : 
# count_zero = 0, count_one = 3
# Answer = 0 * 3 * 2 ^ 0 = 0
# Similarly, for bit position 1 :
# count_zero = 1, count_one = 2
# Answer = 1 * 2 * 2 ^ 1 = 4
# Similarly, for bit position 2 :
# count_zero = 1, count_one = 2
# Answer = 1 * 2 * 2 ^ 2 = 8
#  Final answer = 0 + 4 + 8 = 12 

# O(nlogn)
import math
class Solution:
    def sumXOR (self, arr, n) : 
        #Complete the function
        ans=0
        k=int(math.log2(max(arr)))+1
        for i in range(k):
            zc=0
            oc=0
            idsum=0
            for j in range(0,n):
                if (arr[j]%2==0):
                    zc+=1
                else:
                    oc+=1
                arr[j]=int(arr[j]/2)
            idsum=oc*zc*(1<<i)
            ans+=idsum
        return ans

for _ in range(0,int(input())):
    
    n = int(input())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    res = ob.sumXOR(arr, n)
    print(res)
