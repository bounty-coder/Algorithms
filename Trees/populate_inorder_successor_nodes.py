# https://www.geeksforgeeks.org/problems/populate-inorder-successor-for-all-nodes/1

# Given a Binary Tree, complete the function to populate the next pointer for all nodes. The next pointer for every node should point to the Inorder successor of the node.
# You do not have to return or print anything. Just make changes in the root node given to you.

# Note: The node having no in-order successor will be pointed to -1. You don't have to add -1 explicitly, the driver code will take care of this.

# Input:
#        10
#        /  \
#       8   12
#      /
#     3
# Output: 3->8 8->10 10->12 12->-1
# Explanation: The inorder of the above tree is : 3 8 10 12. So the next pointer of node 3 is pointing to 8 , next pointer of 8 is pointing to 10 and so on.And next pointer of 12 is pointing to -1 as there is no inorder successor of 12.


''' 
  Solution:
      Go from right to left and add the previous node as temporary so as to assign next
'''
class Solution:
    node=None
    def populateNext(self, root):
        if not root:
            return None
        self.populateNext(root.right)
        root.next=self.node
        self.node=root
        self.populateNext(root.left)
