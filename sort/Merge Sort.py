# Merge Sort is a Divide and Conquer algorithm. 
# It divides the input array into two halves, 
# calls itself for the two halves, 
# and then merges the two sorted halves.

# TC- O(nlogn)
# Auxiliary Space: O(n)
# Algorithmic Paradigm: Divide and Conquer
# Sorting In Place: No in a typical implementation
# Stable: Yes

def merge(arr,l,m,r):
    a=arr[:m-l+1]
    b=arr[r-m:]
    i,j=0,0
    k=l
    while i<len(a) or j<len(b):
        if a[i]<=b[j]:
            arr[k]=a[i]
            i+=1
        else:
            arr[k]=b[j]
            j+=1
        k+=1

def mergesort(arr,l,r):
    if(l>=r):
        return
    m=l+(r-l)/2
    mergesort(arr,l,m)
    mergesort(arr,m+1,r)
    merge(arr,l,m,r)


def func():
    ls=list(map(int,input("Enter the list:").split()))
    mergesort(ls,0,len(ls)-1)
    print(ls)


if __name__=="__main__":
    func()

# Merge Sort is useful for sorting linked lists in O(nLogn) time.