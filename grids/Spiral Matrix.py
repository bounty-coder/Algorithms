# Given a matrix of m * n elements (m rows, n columns), return all 
# elements of the matrix in spiral order.


def spiralOrder(arr):
        n=len(arr)
        m=len(arr[0])
        t,b,l,r=0,n-1,0,m-1
        d=0
        ls=[]
        while t<=b and l<=r:
            if d==0:
                for i in range(l,r+1):
                    ls.append(arr[t][i])
                t+=1
            elif d==1:
                for i in range(t,b+1):
                    ls.append(arr[i][r])
                r-=1
            elif d==2:
                for i in range(r,l-1,-1):
                    ls.append(arr[b][i])
                b-=1
            elif d==3:
                for i in range(b,t-1,-1):
                    ls.append(arr[i][l])
                l+=1
            d=(d+1)%4
        return ls

arr=[
    [ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ]
]
print(spiralOrder(arr))