


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