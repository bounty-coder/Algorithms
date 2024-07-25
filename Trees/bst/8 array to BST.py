#similar to binary search we need to implement things
#First, go to mid element. Then assign it mid element.
# similarly go right and left, by dividing the vector in two. 

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

def sortedArrayToBST(self, nums):
    # code here
    if not nums:
        return  None
    mid=len(nums)//2
    root=Node(nums[mid])
    root.left=self.sortedArrayToBST(nums[:mid])
    root.right=self.sortedArrayToBST(nums[mid+1:])
    return root
