# Bubble Sort is the simplest sorting algorithm that 
# works by repeatedly swapping the adjacent elements
# if they are in wrong order.

def bubble(arr,n):
    if n==1:
        return 
    
    for i in range(n-1):
        if arr[i]>arr[i+1]:
            arr[i],arr[i+1]=arr[i+1],arr[i]
        
    bubble(arr,n-1)

    return arr


arr=list(map(int,input().split()))
n=len(arr)
arr=bubble(arr,n)
print(arr)