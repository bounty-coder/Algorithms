def getpostorder(pre,n):
    pivotpoint=0

    for i in range(1,n):
        if (pre[0]<=pre[i]):
            pivotpoint=i
            break

        for i in range(pivotpoint-1,0,-1):
            print(pre[i],end=" ")

        for i in range(n-1,pivotpoint-1,-1):
            print(pre[i],end=" ")
        print(pre[0])
        

pre=[40,30,32,35,80,90,100,120]
n=8

getpostorder(pre,n)