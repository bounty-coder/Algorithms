# A Python3 program to sort a
# nearly sorted array.

# 1) Create a Min Heap of size k+1 with first k+1 elements.
#  This will take O(k) time 
# 2) One by one remove min element from heap, put it in result array,
#  and add a new element to heap from remaining elements.
# Removing an element and adding a new element to min heap
#  will take log k time. 
# So overall complexity will be O(k) + O((n-k) * log(k)).


from heapq import heappop, heappush, heapify


# A utility function to print
# array elements
def print_array(arr: list):
	for elem in arr:
		print(elem, end=' ')

# Given an array of size n, where every
# element is k away from its target
# position, sorts the array in O(nLogk) time.


def sort_k(arr: list, n: int, k: int):
	"""
	:param arr: input array
	:param n: length of the array
	:param k: max distance, which every
	element is away from its target position.
	:return: None
	"""
	# List of first k+1 items
	heap = arr[:k + 1]

	# using heapify to convert list
	# into heap(or min heap)
	heapify(heap)

	# "rem_elmnts_index" is index for remaining
	# elements in arr and "target_index" is
	# target index of for current minimum element
	# in Min Heap "heap".
	target_index = 0
	for rem_elmnts_index in range(k + 1, n):
		arr[target_index] = heappop(heap)
		heappush(heap, arr[rem_elmnts_index])
		target_index += 1

	while heap:
		arr[target_index] = heappop(heap)
		target_index += 1


# Driver Code
k = 3
arr = [2, 6, 3, 12, 56, 8]
n = len(arr)
sort_k(arr, n, k)

print('Following is sorted array')
print_array(arr)


