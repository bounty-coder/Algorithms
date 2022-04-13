def knapsack(w,n,p):
    if w==0 or n==0:
        return 0
    if p[n-1][0]<=w:
        return max(p[n-1][1]+knapsack(w-p[n-1][0],n-1,p),knapsack(w,n-1,p))
    elif p[n-1][0]>w:
        return knapsack(w,n-1,p)

#w- weight of knapsack
#no of products
# p[0]-> weight of product
#p[1]-> value of product

if __name__=='__main__':
    t=int(input())
    while t:
        t-=1
        ls=list(map(int,input().split()))
        w=ls[0]
        n=ls[1]
        p=[]
        for i in range(n):
            p.append(list(map(int,input().split())))
        
        max_val=knapsack(w,n,p)
        print(max_val)