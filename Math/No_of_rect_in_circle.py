# Given a circular sheet of radius, r. 
# Find the total number of rectangles with integral length and width 
# that can be cut from the sheet that can fit on the circle, one at a time.
'''
Input: r=1
Output: 1
Explanation: Only 1 rectangle of dimensions 1x1.

Input: r=2
Output: 8
Explanation: The 8 possible rectangles are 
(1x1)(1x2)(1x3)(2x1)(2x2)(2x3)(3x1)(3x2).
'''

# The question asks to calculate the total number of rectangles with integral (whole number) length and width
# that can be cut from a circular sheet of radius ( r ) such that each rectangle can fit within the circle, one at a time.

# To fit a rectangle inside a circle, the diagonal of the rectangle must be less than or equal to the diameter of the circle.
# This is because the diagonal is the longest distance across the rectangle, and if this fits within the circle, then the entire rectangle will fit.

# it is a rectangle, so the angle will be 90 degree. And two lines joining at 90 degree in circle will surely go through diameter
# d = 2r  And by pythagoras theorem - x*x + y*y = (2r)*(2r)


def rectanglesInCircle(r):
    r2 = 4*r*r
    count=0
    for x in range(2*r):
        for y in range(2*r):
            if x*x+y*y<=r2:
                count+=1
    return count
