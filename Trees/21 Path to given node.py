# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

# SC- O(n) TC-O(height)
class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return a list of integers
    def getpath(self,A ,ls,B):
        if not A:
            return False
        
        ls.append(A.val)
        
        if A.val==B:
            return True
        
        if self.getpath(A.left,ls,B) or self.getpath(A.right,ls,B):
            return True
        ls.pop()
        return False

    def solve(self, A, B):
        ls=[]
        if A is None:
            return ls
        self.getpath(A,ls,B)
        return ls