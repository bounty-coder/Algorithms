# Each number in C may only be used once in the combination.

# ip- [10,1,2,7,6,1,5]  target=8
# op- [[1,1,6],[1,2,5],[1,7],[2,6]]

def solve(A,B,temp,ans,index):
    if B==0:
        ans.append(list(temp))
        return
        
    for i in range(index,len(A)):
        # checking if repeated
        if (i>index and A[i]==A[i-1]):
            continue
        # check if sum exceeds
        if A[i]>B:
            break
        # appending 
        temp.append(A[i])
        solve(A,B-A[i],temp,ans,i+1)
        temp.pop()

def combinationSum(A, B):
        ans=[]
        A.sort()
        temp=[]
        n=len(A)
        solve(A,B,temp,ans,0)
        return ans

A=list(map(int,input().split()))
B=int(input())
print(combinationSum(A,B))


# same solution function in function
# def combinationSum(A, B):
    
#     A.sort()
#     res = []

#     def backtrack(idx=0,currSum=0,currList=[]):
#         if currSum>B:
#             return
#         elif currSum==B:
#             res.append(currList)
#             return
#         else:
#             for i in range(idx,len(A)):
#                 if i!=idx and A[i]==A[i-1]:
#                     continue
#                 backtrack(i+1,currSum+A[i],currList+[A[i]])
    
#     backtrack()
#     return sorted(res)