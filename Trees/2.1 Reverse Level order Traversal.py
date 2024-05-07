# Given a binary tree of size n, find its reverse level order traversal. ie- the traversal must begin from the last level.

# Input :
#         1
#       /   \
#      3     2

# Output: 
# 3 2 1
# Explanation:
# Traversing level 1 : 3 2
# Traversing level 0 : 1


'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
def reverseLevelOrder(root):
    ans = []
    if not root:
        return ans
    queue = deque()
    queue.append(root)
    while queue:
        tmp = queue.popleft()
        ans.append(tmp.data)
        if tmp.right:
            queue.append(tmp.right)
        if tmp.left:
            queue.append(tmp.left)
    ans.reverse()
    return ans
