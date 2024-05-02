# https://www.geeksforgeeks.org/problems/serialize-and-deserialize-a-binary-tree/1

''' Serialize a tree and then deserialize it '''
#  serialize() : stores the tree into an array a and returns the array.
#  deSerialize() : deserializes the array to the tree and returns the root of the tree.


from collections import deque
class Solution:
    #Function to serialize a tree and return a list containing nodes of tree.
    def serialize(self, root):
        if root is None:
            return [0]
        vector = []
        queue = deque()
        queue.append(root)
        vector.append(root.data)
        while queue:
            tmp = queue.popleft()
            if tmp.left is None:
                vector.append(0)
            else:
                vector.append(tmp.left.data)
                queue.append(tmp.left)
            
            if tmp.right is None:
                vector.append(0)
            else:
                vector.append(tmp.right.data)
                queue.append(tmp.right)
        return vector
    
    #Function to deserialize a list and construct the tree.   
    def deSerialize(self, a):
        if a[0]==0:
            return None
        root = Node(a[0])
        i=1
        queue = deque()
        queue.append(root)
        while i<len(a):
            tmp = queue.popleft()
            
            left = None
            if a[i]!=0:
                left = Node(a[i])
            if left is not None:
                tmp.left = left
                queue.append(left)
            
            right = None
            if a[i+1]!=0:
                right = Node(a[i+1])
            if right is not None:
                tmp.right = right
                queue.append(right)
            
            i+=2
            
        return root
    
