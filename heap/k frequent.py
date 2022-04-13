# Python3 implementation to find k
# numbers with most occurrences in
# the given array

# Create a Hashmap hm, to store key-value pair,
#  i.e. element-frequency pair.
# Traverse the array from start to end.
# For every element in the array update hm[array[i]]++
# Store the element-frequency pair in a Priority Queue 
# and create the Priority Queue, this takes O(n) time.
# Run a loop k times, and in each iteration remove the 
# top of the priority queue and print the element.

# Time Complexity: O(k log d + d), where d is the
#  count of distinct elements in the array. 
# To remove the top of priority queue O(log d)
#  time is required, so if k elements are removed
#  then O(k log d) time is required and 
# to traverse the distinct elements O(d) time is required.
# Auxiliary Space: O(d), where d is the 
# count of distinct elements in the array. 
# To store the elements in HashMap O(d) 
# space complexity is needed.

import heapq

# Function to print the k numbers with
# most occurrences
def print_N_mostFrequentNumber(arr, n, k):
	
	mp = dict()
	
	# Put count of all the distinct elements
	# in dictionary with element as the
	# key & count as the value.
	for i in range(0, n):
		if arr[i] not in mp:
			mp[arr[i]] = 0
		else:
			mp[arr[i]] += 1
			
	# Using heapq data structure
	heap = [(value, key) for key,
			value in mp.items()]
			
	# Get the top k elements
	largest = heapq.nlargest(k, heap)

	# Insert the data from the map to
	# the priority queue
	print(k, " numbers with most "
			"occurrences are:", sep = "")
			
	# Print the top k elements
	for i in range(k):
		print(largest[i][1], end =" ")

# Driver code
if __name__=="__main__":
	
	arr = [ 3, 1, 4, 4, 5, 2, 6, 1 ]
	n = len(arr)
	k = 2
	
	print_N_mostFrequentNumber(arr, n, k)