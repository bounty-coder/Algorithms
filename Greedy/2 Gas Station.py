# Given two integer arrays A and B of size N. There are N gas stations
#  along a circular route, where the amount of gas at station i is A[i].

# You have a car with an unlimited gas tank and it costs B[i] of gas to
#  travel from station i to its next station (i+1). You begin the journey
#  with an empty tank at one of the gas stations.

# Return the minimum starting gas station's index if you can travel around
#  the circuit once, otherwise return -1.

#ip- A[1,2,3,4,5] gas
#    B[3,4,5,1,2] cost
#op- 3 (YES from third index car can start )
# O(n)
def canCompleteCircuit(A, B):
    n=len(A)
    tank,total=0,0
    index=0
    for i in range(n):
        consume=A[i]-B[i]
        tank+=consume
        if tank<0:
            index=i+1
            tank=0
        total+=consume
    
    if total<0:
        return -1
    else:
        return index

# O(n^2 bruteforce)
# def canCompleteCircuit(A, B):
#         cost=0
#         n=len(A)
#         for i in range(n):
#             total,stopcount=0,0
#             j=i
#             while stopcount<n:
#                 total+=A[j%n]-B[j%n]
#                 if total<0:
#                     break
#                 stopcount+=1
#                 j+=1
            
#             if stopcount==n and total>=0:
#                 return i
#         return -1