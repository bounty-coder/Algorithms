# Given the root of a binary tree A, the value of a target node B,
# and an integer C, return an array of the values of all nodes
# that have a distance C from the target node.

# A =     1
#        / \          B = 2
#       2   3         C = 1
#      / \
#     4   5

# Output 1: [1, 4, 5]

# Approach 
# problem is we can go left,right but How do we traverse to 
# the parent of a node? So, first traverse dfs wise and save the parent node in 
# some data structure. 

# main points
# 1. to get parents pointer
# 2.keep on moving by 1 distance every time upward, leftward and downwards
# 3. when distance equals k, stop.

# extra explanantion
#1) If node == B, then we should add nodes that are distance C in the subtree rooted at target.
# 2) If target is in the left branch of node, say at distance L+1, 
#    then we should look for nodes that are distance C - L - 1 in the right branch.
# 3) If target is in the right branch of node, the algorithm proceeds similarly.
# 4) If target isn't in either branch of node, then we stop.

# In the above algorithm, we make use of the auxillary function subtree_add(node, dist) 
# which adds the nodes in the subtree rooted at node that 
# are distance C - dist from the given node.

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

import collections
class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @param C : integer
    # @return a list of integers
    def distanceK(self, A, B, C):
        
        def pathto(root, val):
            stack = [(root, 0)]
            while len(stack) > 0:
                node, state = stack.pop()
                if state == 2 or node.left is None and node.right is None:
                    if node.val == val:
                        return [n for n, _ in stack] + [node]
                elif state == 1:
                    stack.append((node, 2))
                    if node.right:
                        stack.append((node.right, 0))
                else:
                    stack.append((node, 1))
                    if node.left:
                        stack.append((node.left, 0))
            return None
            
        def distance(root, k):
            queue = collections.deque()
            queue.append(root)
            queue.append(None)
            level = 0
            results = []
            while len(queue) > 0:
                node = queue.popleft()
                if node is None:
                    if len(queue):
                        level += 1
                        queue.append(None)
                else:
                    if level == k:
                        results.append(node.val)
                    else:
                        if node.left:
                            queue.append(node.left)
                        if node.right:
                            queue.append(node.right)
            return results
            
        def reroot(stack):
            stack[-1].left = stack[-1].right = None
            isright = True
            for i in range(len(stack) - 1, 0, -1):
                if isright:
                    stack[i].right = stack[i - 1]
                else:
                    stack[i].left = stack[i - 1]
                if stack[i - 1].right == stack[i]:
                    stack[i - 1].right = None
                    isright = True
                else:
                    stack[i - 1].left = None
                    isright = False
            return stack[-1]

        # create path to parents node    
        path = pathto(A, B)
        nodes = distance(path[-1], C)
        nodes.extend(distance(reroot(path), C))
        
        return nodes
        