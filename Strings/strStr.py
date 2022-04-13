# Expectation is that you will ask for correct clarification
#  or you will state your assumptions before you start coding.

def strStr( A, B):
    n=len(A)
    m=len(B)
    if m==0:
        return 0
    if n==0 and m==0:
        return 0
    if n==m and A==B:
        return 0
    i=0
    while i+m<n:
        if B==A[i:i+m]:
            return i
        i+=1
    return -1

A=input()
B=input()
print(strStr(A,B))