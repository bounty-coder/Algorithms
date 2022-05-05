# Ugly numbers are numbers whose only prime factors are 2, 3 or 5.

def divide(a,b):
    while a%b==0:
        a=a/b
    return a

def isugly(i):
    j=i
    i= divide(i,2)
    i= divide(i,3)
    i= divide(i,5)
    if i==1:
        print(j,end=' ')
    return 1 if i==1 else 0

def uglynum(n):
    i=1
    count=1
    while count<n:
        i+=1
        if isugly(i):
            count+=1

    return i

t=int(input())
while t:
    t-=1
    n=int(input())   #input the N-th value to find nth ugly number
    ug=uglynum(n)
    print(ug)