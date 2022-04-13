def selection(arr):
    l=len(arr)
    for i in range(l):
        k=i
        m=arr[i]
        for j in range(i+1,l):
            if m>arr[j]:
                m=arr[j]
                k=j
        temp=arr[i]
        arr[i]=arr[k]
        arr[k]=temp
    return arr

def func():
    ls=list(map(int,input("Enter elements:").split()))
    ls=selection(ls)
    print(ls)

if __name__=='__main__':
    func()