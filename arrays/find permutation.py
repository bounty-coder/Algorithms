# Given a positive integer n and a string s consisting only 
# of letters D or I, you have to find any permutation of 
# first n positive integer that satisfy the given input string.

# D means the next number is smaller,
#  while I means the next number is greater.

# Length of given string s will always equal to n - 1
# Your solution should run in linear time and space.

# B=3, A="ID"  Return: [1, 3, 2]
# B=5, A="DIDI"  return: [5,1,4,3,2]

# for i start from 1 and go up
# or else start from B and go down
 
def findPerm(A, B):
    s=1
    l=B
    res=[]
    for i in range(0,len(A)):
        if A[i]=="I":
            res.append(s)
            s+=1
        else:
            res.append(l)
            l-=1
        print(res)
    res.append(l)
    return res