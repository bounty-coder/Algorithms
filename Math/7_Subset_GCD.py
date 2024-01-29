#  https://www.codechef.com/problems/GCDPERM?tab=statement

# Given integers N and K. Find a k-sized subset of {1,2,3..N} with maximum GCD. If multiple such subsets exist, you may print any.

'''
Input
3
3 2
3 3
4 2
Output
2 3
1 2 3
2 4

'''

#Logic is, from observation
''' if N=8, and k=1 => 8
       N=8, and k=2 => 4,8
       N=8, and k=3 => 2,4,6
       N=8, and k=4 => 2,4,6,8
    so, N/k is always the minimum number, then find its k multiples
'''

t=int(input())
while t:
    n,k=map(int,input().split())
    ls=[]
    x=n//k
    i=1
    while i<=k:
        ls.append(x*i)
        i+=1
    print(" ".join(map(str,ls)))
    t-=1
