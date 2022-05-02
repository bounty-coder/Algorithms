# for smallest element use min heap and vice versa

# O(n + k*log(n)) 

import heapq

arr=list(map(int,input("Enter array:").split()))
k=int(input("Enter k:"))

# O(n)
heapq.heapify(arr)

#O(klogn)
for i in range(k-1):
    heapq.heappop(arr)
print(arr[0])