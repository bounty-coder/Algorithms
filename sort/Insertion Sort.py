# The array is virtually split into a sorted and an unsorted part.
#  Values from the unsorted part are picked and placed at the correct
#  position in the sorted part.


def insertion(arr,n):
    for i in range(1,n):
        for j in range(i):
            if arr[j]>arr[i]:
                temp=arr[j]
                arr[j]=arr[i]
                arr[i]=temp
    return arr

def func():
    arr=list(map(int,input("Enter elements:").split()))
    n=len(arr)
    arr=insertion(arr,n)
    print(arr)

if __name__=='__main__':
    func()