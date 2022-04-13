n = int(input())

def uglynum(n):
    ugly=[0]*n
    ugly[0]=1
    i2,i3,i5=0,0,0
    n2,n3,n5=2,3,5
    print(f"i2={i2} i3={i3} i5={i5} n2={n2} n3={n3} n5={n5}")
    for i in range(1,n):
        ugly[i]=min(n2,n3,n5)
        if ugly[i]==n2:
            i2+=1 
            n2=ugly[i2]*2
            print(f"i2={i2} ({n2},{n3},{n5})",end=' ')
        if ugly[i]==n3:
            i3+=1
            n3=ugly[i3]*3
            print(f"i3={i3} ({n2},{n3},{n5})",end=" ")
        if ugly[i]==n5:
            i5+=1
            n5=ugly[i5]*5
            print(f"i5={i5} ({n2},{n3},{n5})",end=" ")
        print('')
    return ugly


print(uglynum(n))