# Given a positive integer N, the task is to find all the
# N bit binary numbers having more than or equal 1’s than 
# 0’s for any prefix of the number.

# Input:  N = 3
# Output: 111 110 101

def solve(n,curr,ones,zeroes,s):
    if zeroes<=ones and n==ones+zeroes:
        s.append(curr)
        return 
    else:
        if ones+zeroes<n:
            solve(n,curr+"1",ones+1,zeroes,s)
        if ones>zeroes:
            solve(n,curr+"0",ones,zeroes+1,s)
    
def NBitBinary(N):
    # code here
    ones=0
    zeroes=0
    S=[]
    solve(N,"",ones,zeroes,S)
    return S

N=int(input())
print(NBitBinary(N))