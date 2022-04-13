# Cartesian tree :  is a heap ordered binary tree, where the 
# root is greater than all the elements in the subtree.

# Approach
# 1. Find the max in array, which will be root of tree
# 2. recursively go to left and right sub array and hence create tree. 

class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


def solve(A,start,end):
    if start>end:
        return 
    maxi=float("-inf")
    ind=-1
    for i in range(start,end+1):
        if A[i]>maxi:
            maxi=A[i]
            ind=i

    root=TreeNode(maxi)
    root.left=solve(A,start,ind-1)
    root.right=solve(A,ind+1,end)
    return root

def buildTree(A):
    return solve(A,0,len(A)-1,)

A=list(map(int,input("Enter inorder traversal:").split()))
print(buildTree(A))