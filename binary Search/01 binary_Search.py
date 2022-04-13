def binary(lst,f,l,n):
    while f<=l:
        mid = f + (l -f) // 2
        if n == lst[mid]:
            return mid
        elif n < lst[mid]:
            l=mid-1
        elif n > lst[mid]:
            f=mid+1
    return -1

def value():
    lst=[]
    lst=list(map(int,input("Enter List:").split()))
    lst.sort()
    l=len(lst)
    n=int(input("Enter element to search:"))
    r=binary(lst,0,l,n)
    if r==-1:
        print("Element not present in array")
    else:
        print(f"Element present at {r}th index")

if __name__ == '__main__':
    value()