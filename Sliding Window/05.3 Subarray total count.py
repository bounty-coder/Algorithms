# Given an unsorted array of integers, find the number of continuous
#  subarrays having sum exactly equal to a given number k.    
# N = 5
# Arr = {10 , 2, -2, -20, 10}
# k = -10
# Output: 3
# Subarrays: arr[0...3], arr[1...4], arr[3..4]
# have sum exactly equal to -10.
#   
# Here, we will be using a dictionary which if a key not 
# present in it. Instead of raising the error, it will 
# automatically creates the key and raises its value to 0.
# Defaultdict is a module in collections library with same features

from collections import defaultdict
class Solution:
    def findSubArraySum(self, Arr, N, k):

        dic=defaultdict(lambda:0)
        l,i,s=0,0,0  #l= count, s=sum
        while i<N:
            s+=Arr[i]
            if s==k:
                l+=1
                
            if s-k in dic:
                l+=dic[s-k]
                
            dic[s]+=1
            i+=1
        return l

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N = int(input())
        Arr = input().split()
        for itr in range(N):
            Arr[itr] = int(Arr[itr])
        k = int(input())
        ob = Solution()
        print(ob.findSubArraySum(Arr, N, k))


# Why Do we Have to use HashTable:
# Let us Consider a subarray within the array whose sum is let say ‘x’
#  and a subarray starting just after this subarray sums up to k , 
# a[i,j]=x & a[j+1,l]=k (l be any positive number ≥ j+1 and less than
#  the size of array) so a[i,l]=x+k.
# # Main observation to take from here is if take the sum form the 
# starting index and store in a hashmap for every index i and also 
# check for every index if ‘sum-k’ is already present in the subarray or
# not (x+k-k→x) ,sum-k would have been present in the map if and 
# only if my current value is x+k hence we'll be able to consider 
# all the subarrays , the last point which we have to to take care is 
# that there can be more than 1 ‘x’ in the array while taking the sum 
# as our array contains negative values so we have to count all those 
# x's in our answer , that's why we use a map instead of a set to also 
# keep the count of x's we have previously encountered and 
# then add it to the answer.