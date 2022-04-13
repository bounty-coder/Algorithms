# The array is virtually split into a sorted and an unsorted part.
#  Values from the unsorted part are picked and placed at the correct
#  position in the sorted part.

# To sort an array of size n in ascending order: 
# 1: Iterate from arr[1] to arr[n] over the array. 
# 2: Compare the current element (key) to its predecessor. 
# 3: If the key element is smaller than its predecessor, compare
# it to the elements before. Move the greater elements one position
# up to make space for the swapped element.

def insertion(arr,n):
    if n<=1:
        return
    insertion(arr,n-1)
    for i in range(0,n):
        if arr[n-1]<arr[i]:
            arr[n-1],arr[i]=arr[i],arr[n-1]
    return arr

arr=list(map(int,input().split()))
n=len(arr)
arr=insertion(arr,n)
print(arr)