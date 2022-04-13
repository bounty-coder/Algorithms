# Given a binary tree, find if it is height balanced or not. 
# A tree is height balanced if difference between heights of left 
# and right subtrees is not more than one for all nodes of tree. 

# Approach 1
# O(n) for traversal * O(n) for finding height= O(n^2)
def height(root):
    if root is None:
        return 0
    return max(height(root.left),height(root.right))+1
        
def isBalanced(root):
    if root is None:
        return True
    lh=height(root.left)
    rh=height(root.right)
    
    if abs(lh-rh)<=1 and isBalanced(root.left) and isBalanced(root.right):
        return True
    
    return False

# Approach 2 
# O(n)
def isBalanced(root):
        ans = isBalancedUtil(root)
        if ans != -1:
            return True
        return False
        
def isBalancedUtil(root):
    if root is None:
        return 0
    lh = isBalancedUtil(root.left)
    if lh == -1:
        return -1
    rh = isBalancedUtil(root.right)
    # print(lh,rh)
    if rh == -1:
        return -1
    if abs(lh-rh) > 1:
        return -1
    return max(lh, rh) + 1