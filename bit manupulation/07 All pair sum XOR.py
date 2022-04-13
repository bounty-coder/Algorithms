# Given an array, calculate
# (A1+A1)^(A1+A2)^....(A1+An)^
# (A2+A1)..........
# ..
# ..
# (An+A1)^............(An+An)

# ip- arr=[4,3,9,1]
# op- 30

# Approch1: Bruteforce O(n^2) by two for loop
# Approach2: By observing the bruteforce matrix, we see that
#  Only diagonal elements will left for calculation and rest 
# element are duplicate in matrix so they will be 0.

arr=list(map(int,input().split()))
ans=(arr[0]+arr[0])   
for i in range(1,len(arr)):
    ans=ans^(arr[i]+arr[i])
print(ans)