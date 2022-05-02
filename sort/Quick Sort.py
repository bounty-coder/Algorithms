# QuickSort is a Divide and Conquer algorithm. It picks an
# element as pivot and partitions the given array around the picked pivot.

# Always pick first element as pivot.
# Always pick last element as pivot (implemented below)
# Pick a random element as pivot.
# Pick median as pivot.

# The logic is simple, we start from the leftmost element and keep track
# of index of smaller (or equal to) elements as i. While traversing,
# if we find a smaller element, we swap current element with 
# arr[i]. Otherwise we ignore current element. 

# Not stable, Inplace(as it uses recursive space)
# The worst case occurs when the partition process always picks
#  greatest or smallest element as pivot. (if already sorted , O(n^2)) 

#TC- O(nlogn)
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