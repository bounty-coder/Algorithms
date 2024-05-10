# For each node there can be four ways that the max path goes through the node: 
# 1. Node only 
# 2. Max path through Left Child + Node 
# 3. Max path through Right Child + Node 
# 4. Max path through Left Child + Node + Max path through Right Child

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
 
    #Function to calculate maximum path sum.
    def findMaxUtil(self, root): 
          
        #base case for recursion.
        if root is None: 
            return (0,float('-inf'))
      
        #l and r store maximum path sum going recursively through left and
        #right subtrees of root(current node) respectively.(basically max value in that subroot, or in simple->max height)
        l, l1 = self.findMaxUtil(root.left) 
        r, r1 = self.findMaxUtil(root.right)
          
        #max path sum for parent call of root. This path must
        #include at-most one child of root.
        max_single = max(max(l, r) + root.val, root.val) 
          
        #max_top represents the sum when the node under consideration is the root
        #of the max sum path and no ancestors of root are there in max sum path.
        max_top = max(max_single, l+r+ root.val) 
        
        res = max(max_top, l1, r1)
      
        return (max_single,res)
      
    #Function to return maximum path sum from any node in a tree. 
    def maxPathSum(self, root): 
        
        res = self.findMaxUtil(root) 
        #returning the result.
        return max(res)




#same thing as above, just small code and did analogy with diameter of binary tree
def findMaxSum(self, root): 
    def dfs(root):
        if not root:
            return float("-inf"),0
        #ld left diameter, lh left height
        ld,lh=dfs(root.left)
        rd,rh=dfs(root.right)
        
        return max(ld,rd,lh+rh+root.data,lh+root.data,rh+root.data,root.data), max(max(lh,rh)+root.data,root.data)
    
    return dfs(root)[0]
