# https://www.geeksforgeeks.org/problems/ancestors-in-binary-tree/1

'''
    Given a Binary Tree and an integer target. Find all the ancestors of the given target.

Note:

The ancestor of node x is node y, which is at the upper level of node x, and x is directly connected with node y. Consider multiple levels of ancestors to solve this problem.
In case there are no ancestors available, return an empty list.
'''

'''
    Input:
         1
       /   \
      2     3
    /  \    /  \
   4   5  6   8
  /
 7
target = 7
Output: [4 2 1]
Explanation: The given target is 7, if we go above the level of node 7, then we find 4, 2 and 1. Hence the ancestors of node 7 are 4 2 and 1
'''

# our strategy will be to find the target first using DFS and as we got the target just go back till the root and print the nodes which we saw while coming back 
def Ancestors(root, target):
    '''
    :param root: root of the given tree.
    :return: None, print the space separated post ancestors of given target., don't print new line
    '''
    if not root:
        return []
    val=[]
    def solve(root,target,val):
        if not root:
            return False
        if root.data==target:
            return True
        a=solve(root.left,target,val)
        if a:
            val.append(root.data)
            return True
        b=solve(root.right,target,val)
        if b:
            val.append(root.data)
            return True
        return False
    
    solve(root,target,val)
    return val
