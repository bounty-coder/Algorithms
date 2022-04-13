# Optimal Substructure: 
# When we drop an egg from a floor x, there can be two cases 
# (1) The egg breaks 
# (2) The egg doesn’t break. 
 

# If the egg breaks after dropping from ‘xth’ floor, 
# then we only need to check for floors lower than ‘x’ with remaining eggs 
# as some floor should exist lower than ‘x’ in which egg would not break; 
# so the problem reduces to x-1 floors and n-1 eggs.
# If the egg doesn’t break after dropping from the ‘xth’ floor, 
# then we only need to check for floors higher than ‘x’; 
# so the problem reduces to ‘k-x’ floors and n eggs.

import sys
 
# Function to get minimum number of trials
# needed in worst case with n eggs and k floors
def eggDrop(n, k):
 
    # If there are no floors, then no trials
    # needed. OR if there is one floor, one
    # trial needed.
    if (k == 1 or k == 0):
        return k
 
    # We need k trials for one egg
    # and k floors
    if (n == 1):
        return k
 
    min = sys.maxsize
 
    # Consider all droppings from 1st
    # floor to kth floor and return
    # the minimum of these values plus 1.
    for x in range(1, k + 1):
 
        res = max(eggDrop(n - 1, x - 1),
                  eggDrop(n, k - x))
        if (res < min):
            min = res
 
    return min + 1
 
# Driver Code
if __name__ == "__main__":
 
    n = 2
    k = 10
    print("Minimum number of trials in worst case with",
           n, "eggs and", k, "floors is", eggDrop(n, k))