# https://www.geeksforgeeks.org/problems/merge-two-bst-s/1

# Given two BSTs, return elements of merged BSTs in sorted form.


# Input:
# BST1:
#        5
#      /   \
#     3     6
#    / \
#   2   4  
# BST2:
#         2
#       /   \
#      1     3
#             \
#              7
#             /
#            6
# Output: 1 2 2 3 3 4 5 6 6 7
# Explanation: After merging and sorting the two BST we get 1 2 2 3 3 4 5 6 6 7.


class Solution:
    def merge(self, root1, root2):
        ans=[]
        
        def findAns(root1,root2,ans):
            if not root1 and not root2:
                return 
            if not root1 and root2:
                findAns(root1,root2.left,ans)
                ans.append(root2.data)
                findAns(root1,root2.right,ans)
            elif root1 and not root2:
                findAns(root1.left,root2,ans)
                ans.append(root1.data)
                findAns(root1.right,root2,ans)
            else:
                findAns(root1.left,root2.left,ans)
                ans.append(root1.data)
                ans.append(root2.data)
                findAns(root1.right,root2.right,ans)
        
        findAns(root1,root2,ans)
        ans.sort()
        return ans
