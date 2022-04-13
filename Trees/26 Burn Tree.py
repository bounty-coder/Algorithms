# Given a binary tree and a node called target. Find the minimum time
#  required to burn the complete binary tree if the target is set on 
# fire. It is known that in 1 second all nodes connected to a given
#  node get burned. That is its left child, right child, and parent.

# Input:      
#           1
#         /   \
#       2      3
#     /  \      \
#    4    5      6
#        / \      \
#       7   8      9
#                    \
#                    10
# Target Node = 8
# Output: 7

# BFS approach:
# Steps:
# 1) Find targetNode and Map for child to parent.
# 2) BFS start with targetNode and keep checking for non-visited left,
#  right or parent of currentNode and add it to q.
# 3) Keep increasing the time, if any node is burnt in any iteration.

class Solution:
    #recursive function
    def _recurse(self, root):
        # if root is NuLL
        if root == None: return (0, False)

        # recursing left and right child
        l, checkl = self._recurse(root.left)
        r, checkr = self._recurse(root.right)

        # if current root is the target        
        if root.data == self.target:
            # compare maximum burn timr with its left and right child's burn time from here
            self.m = max(self.m, max(l, r))

            # but return only the 0 with True
            # it means every ancester of target node will get to know it.
            return (0, True)

        # if target is not down the tree
        elif checkl == False and checkr == False:
            # simply return the maximum depth or time to burn
            return (max(l, r)+1, False)

        # else target is down the tree
        else:
            # compare the maximum burn time with righ and left and current elements burn time
            self.m = max(self.m, l+r+1)
            
            # but only return the time to burn from target to current element
            return (l+1 if checkl else r+1, True)
    
    # main function
    def minTime(self, root, target):
        
        #defining class variabel target and m ( maximum time to burn )
        self.target = target
        self.m = 0
        
        #recursing the tree
        self._recurse(root)
        
        # simply return the maximum of all burn time
        return self.m


#{ 
#  Driver Code Starts
#Initial Template for Python 3

from collections import deque

# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root

if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        line=input()
        target=int(input())
        root=buildTree(line)
        print(Solution().minTime(root,target))

# } Driver Code Ends