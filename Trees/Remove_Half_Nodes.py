# https://www.geeksforgeeks.org/problems/remove-half-nodes/1

# You are given a binary tree and you need to remove all the half nodes (which have only one child). 
# Return the root node of the modified tree after removing all the half-nodes.

# Note: The output will be judged by the inorder traversal of the resultant tree, inside the driver code.

# Input: tree = 5
#             /   \
#           7     8
#         / 
#       2
# Output: 2 5 8
# Explanation: In the above tree, the node 7 has only single child. After removing the node the tree becomes  2<-5->8. Hence, the answer is 2 5 8 & it is in inorder traversal.

class Solution:
    def RemoveHalfNodes(self, node):
        if node:
            node.left=self.RemoveHalfNodes(node.left)
            node.right=self.RemoveHalfNodes(node.right)
            if (not node.left and not node.right) or (node.left and node.right):
                return node
            return node.left if node.left else node.right
