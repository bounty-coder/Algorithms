# Given an array arr[] of size n containing integers. 
# The problem is to find the length of the 
# longest sub-array having sum equal to the given value k.

# Input : arr[] = {-5, 8, -14, 2, 4, 12},
#             k = -5
# Output : 5

# initialise the sum variable which will be the sum uptil i th element
# as getting the new sum from adding i in sum, store it in dictionary 
# with the index number(use of dictionary to store the sum already got at every index)
# if sum is equal to k, it means its the sum from 0th index to ith index
# so max=i+1
# if sum-k present in dic it means (i-dic[sum-k]) = k

# function to find the longest
# subarray having sum k
def lenOfLongSubarr(arr, n, k):

	# dictionary mydict implemented
	# as hash map
	mydict = dict()

	# Initialize sum and maxLen with 0
	sum = 0
	maxLen = 0

	# traverse the given array
	for i in range(n):

		# accumulate the sum
		sum += arr[i]

		# when subArray starts from index '0'
		if (sum == k):
			maxLen = i + 1

		# check if 'sum-k' is present in
		# mydict or not
		elif (sum - k) in mydict:
			maxLen = max(maxLen, i - mydict[sum - k])

		# if sum is not present in dictionary
		# push it in the dictionary with its index
		if sum not in mydict:
			mydict[sum] = i

	return maxLen

# Driver Code
if __name__ == '__main__':
	arr = [10 , 2, -2, -20, 10]
	n = len(arr)
	k = 15
	print("Length =", lenOfLongSubarr(arr, n, k))


