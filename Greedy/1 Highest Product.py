# Given an array A, of N integers A.
# Return the highest product possible by multiplying
#  3 numbers from the array.

# A = [1, 2, 3, 4]
# Output 1:
# 24

# Explanation 1:
# 2 * 3 * 4 = 24

# Soln1:

def maxp3(A):
    A.sort()
    return max(A[-1]*A[-2]*A[-3], A[0]*A[1]*A[-1])

# Soln2

def maxp3(A):
    firstMax = float("-inf")
    secondMax = float("-inf")
    thirdMax = float("-inf")
    
    for i in A:
        if i > thirdMax:
            thirdMax = i
            if thirdMax > secondMax:
                secondMax, thirdMax = thirdMax, secondMax
                if secondMax > firstMax:
                    firstMax, secondMax = secondMax, firstMax
    
    negativeValues = [i for i in A if i < 0]
    if len(negativeValues) <= 1:
        return firstMax * secondMax * thirdMax
    
    firstMin = min(negativeValues)
    negativeValues.remove(firstMin)
    secondMin = min(negativeValues)
    
    candidate1 = abs(secondMin) * abs(firstMin) * firstMax
    candidate2 = firstMax * secondMax * thirdMax
    
    if candidate1 > candidate2:
        return candidate1
    else:
        return candidate2