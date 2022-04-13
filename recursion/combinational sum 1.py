
# A = [2, 3, 6, 7]
# B = 7
#target: [ [2, 2, 3] , [7] ]


def solve(ip,op,B,ans,index):
    if B==0:
        ans.append(list(op))
        return
    for i in range(index,len(ip)):
        if B-ip[i]>=0:
            op.append(ip[i])
            solve(ip,op,B-ip[i],ans,i)
            op.remove(ip[i])
        if B-ip[i]<0:
            break

def combinationSum(A, B):
    A=list(set(A))
    A.sort()
    ans=[]
    op=[]        #temporary output array
    solve(A,op,B,ans,0)
    return ans

A=list(map(int,input().split()))
B=int(input())
print(combinationSum(A,B))