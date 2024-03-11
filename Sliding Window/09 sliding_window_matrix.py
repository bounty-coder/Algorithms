# https://www.geeksforgeeks.org/problems/count-pairs-sum-in-matrices4332/1
"""Given two sorted matrices mat1 and mat2 of size n x n of elements. Each matrix contains numbers arranged
in strictly ascending order, with each row sorted from left to right, and the last element of a row being
smaller than the first element of the next row. You're given a target value, x, your task is to find and 
count all pairs {a, b} such that a is from mat1 and b is from mat2 where sum of a and b is equal to x."""

"""Input: 
n = 3, x = 21
mat1 = {{1, 5, 6},
        {8, 10, 11},
        {15, 16, 18}}
mat2 = {{2, 4, 7},
        {9, 10, 12},
        {13, 16, 20}}
OUTPUT: 4
Explanation: The pairs whose sum is found to be 21 are (1, 20), (5, 16), (8, 13), (11, 10)."""


#1 Recursion(good)
class Solution:
    def countPairs(self, mat1, mat2, n, x):
        # code here
        ls1 = []
        ls2 = []
        for i in range(n):
            for j in range(n):
                ls1.append(mat1[i][j])
                ls2.append(mat2[n-i-1][n-j-1])
        
        def findpairs(ls1,ls2,i,j,x,count):
            if i>len(ls1)-1 or j>len(ls2)-1:
                return count
            s = ls1[i]+ls2[j]
            if s==x:
                count+=1
                count = findpairs(ls1,ls2,i+1,j+1,x,count)
            elif s<x:
                count = findpairs(ls1,ls2,i+1,j,x,count)
            else:
                count = findpairs(ls1,ls2,i,j+1,x,count)
            return count
        
        return findpairs(ls1,ls2,0,0,x,0)



#2 Iterative(better)
#User function Template for python3
class Solution:
    def countPairs(self, mat1, mat2, n, x):
        # code here
        ls1 = []
        ls2 = []
        for i in range(n):
            for j in range(n):
                ls1.append(mat1[i][j])
                ls2.append(mat2[n-i-1][n-j-1])
        
        count,i,j = 0,0,0
        while (i<len(ls1) and j<len(ls2)):
            s = ls1[i]+ls2[j]
            if s==x:
                count+=1
                i+=1
                j+=1
            elif s<x:
                i+=1
            else:
                j+=1
        return count



#3 Hashing(best)
class Solution:
    def countPairs(self, mat1, mat2, n, x):
        h=set()
        for i in range(n):
            for j in range(n):
                h.add(mat1[i][j])
       
        count=0
        for i in range(n):
           for j in range(n):
               if x-mat2[i][j] in h:
                   count+=1
        return count
