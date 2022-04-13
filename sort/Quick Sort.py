def swap(a,b):
    temp=a
    a=b
    b=temp

def quicksort(arr,low,high):
    if low<high:
        pivot=arr[high]
        i=low-1
        for j in range(low,high):
            if arr[j]<pivot:
                i=i+1
                swap(arr[i],arr[j])
        swap(arr[i+1],arr[high])
        quicksort(arr,low,i)
        quicksort(arr,i+2,high)
    return arr

def func():
    ls=list(map(int,input("Enter elements:").split()))
    ls=quicksort(ls,0,len(ls)-1)
    print(ls)

if __name__=='__main__':
    func()