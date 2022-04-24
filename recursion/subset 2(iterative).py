def combine(a,data,k,strt,endd,idx):
    if idx==k:
        for j in data:
            print(j,end=' ')
        print()
        return

    i=strt
    while i<=endd :
        data[idx]=a[i]
        combine(a,data,k,i+1,endd,idx+1)
        i+=1


def printseq(a,n,k):
    data=[0]*k
    combine(a,data,k,0,n-1,0)

a=[1,2,3,4,5]
k=3
printseq(a,len(a),k)