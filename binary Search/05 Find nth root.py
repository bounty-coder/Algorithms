# if x in (0,1] set low=x and high=1
# else x in [1,x] set low=1,high=x
# declare variable for approximation(epsilon here)
# # guess=(low+high)/2
# if the absolute error of our guess is more than epsilon then do: 
# if guess^n > x, then high=guess
# else low=guess
# Making a new better guess i.e., guess=(low+high)/2.
def findNthRoot(x, n):

	# Initialize boundary values
	x = float(x)
	n = int(n)
	if (x >= 0 and x <= 1):
		low = x
		high = 1
	else:
		low = 1
		high = x

	# used for taking approximations
	# of the answer
	epsilon = 0.00000001

	# Do binary search
	guess = (low + high) / 2
	while abs(guess ** n - x) >= epsilon:
		if guess ** n > x:
			high = guess
		else:
			low = guess
		guess = (low + high) / 2
	print(guess)

x = 5
n = 2
findNthRoot(x, n)
