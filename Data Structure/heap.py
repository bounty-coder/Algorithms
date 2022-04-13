# Heap data structure is mainly used to represent a priority queue
# Heap is a special tree structure in which each parent node is less than or equal to its child node.
# Then it is called a Min Heap.
# If each parent node is greater than or equal to its child node then 
# it is called a max heap

import heapq

ls=[1,2,4,55,23,3,5]
print(ls)
heapq.heapify(ls)
print("After heapifying:", ls)

heapq.heappush(ls,4)
print("After pushing:",ls)

heapq.heappop(ls)
print("After popping:",ls)

# using heappushpop() to push and pop items simultaneously 
print (heapq.heappushpop(ls, 11))
print("After pushing 11 and popping simultaneously:",ls)

# using heapreplace() to push and pop items simultaneously
print (heapq.heapreplace(ls, 13))
print("After replacing 13:",ls)