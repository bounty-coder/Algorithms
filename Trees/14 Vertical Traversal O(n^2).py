# Given a binary tree, print it vertically.

# Approach 
# traverse the tree once and get the minimum and maximum horizontal
#  distance with respect to root.
# Once we have maximum and minimum distances from root, we iterate
#  for each vertical line at distance minimum to maximum from root,
#  and for each vertical line traverse the tree and print the nodes
#  which lie on that vertical line.

#O(n^2)
class Solution:
    
    #Function to find the vertical order traversal of Binary Tree.
    def findminmax(self,root,mini,maxi,hd):
        if root is None:
            return 
        if hd<mini[0]:
            mini[0]=hd
        elif hd>maxi[0]:
            maxi[0]=hd
        
        self.findminmax(root.left,mini,maxi,hd-1)
        self.findminmax(root.right,mini,maxi,hd+1)
            
    def printvertical(self,root,line,hd):
        if root is None:
            return 
        if hd==line:
            self.ans.append(root.data)
            
        self.printvertical(root.left,line,hd-1)
        self.printvertical(root.right,line,hd+1)
        
    def verticalOrder(self, root): 
        # declaring mini maxi in list as list is immutable
        # and in python, we can pass by object reference
        mini=[0]
        maxi=[0]
        self.findminmax(root,mini,maxi,0)
        self.ans=[]
        for line in range(mini[0],maxi[0]+1):
            self.printvertical(root,line,0)
        return self.ans

# Driver code
from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
  
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
    import sys
    sys.setrecursionlimit(10000)
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        res = Solution().verticalOrder(root)
        for i in res:
            print (i, end=" ")
        print()