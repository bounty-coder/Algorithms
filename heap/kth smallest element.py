# for smallest element use max heap and vice versa


import heapq

arr=list(map(int,input("Enter array:").split()))
k=int(input("Enter k:"))

# O(nlogk)
for i in range(k-1):
    heapq.heapify(arr)
    heapq.heappop(arr)
heapq.heapify(arr)
print(heapq.heappop(arr))
print(arr)