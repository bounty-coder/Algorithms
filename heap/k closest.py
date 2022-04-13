# Python3 program to find k closest elements

# 1) Make a max heap of differences with first k elements. 
# 2) For every element starting from (k+1)-th element, do following. 
# …..a) Find difference of current element with x. 
# …..b) If difference is more than root of heap, ignore current element. 
# …..c) Else insert the current element to the heap after removing the root. 
# 3) Finally the heap has k closest elements. 

# TC: O(n Log k)
import math
import sys
from queue import PriorityQueue
def printKclosest(arr,n,x,k):

	# Make a max heap of difference with
	# first k elements.
	pq = PriorityQueue()
	for i in range(k):
		pq.put((-abs(arr[i]-x),i))

	# Now process remaining elements
	for i in range(k,n):
		diff = abs(arr[i]-x)
		p,pi = pq.get()
		curr = -p

		# If difference with current
		# element is more than root,
		# then put it back.
		if diff>curr:
			pq.put((-curr,pi))
			continue
		else:

			# Else remove root and insert
			pq.put((-diff,i))
			
	# Print contents of heap.
	while(not pq.empty()):
		p,q = pq.get()
		print("{} ".format(arr[q]),end = "")

# Driver program to test above functions
if __name__=='__main__':
	arr = [-10,-50,20,17,80]
	x,k = 20,2
	n = len(arr)
	printKclosest(arr, n, x, k)