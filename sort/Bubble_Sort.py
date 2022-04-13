def bubble(arr):
    l=len(arr)
    for i in range(l):
        for j in range(i-1):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
    return arr

def func():
    ls=list(map(int,input("Enter elements:").split()))
    ls=bubble(ls)
    print(ls)

if __name__=='__main__':
    func()