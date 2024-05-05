# https://www.geeksforgeeks.org/problems/vertical-sum/1
'''Given a binary tree having n nodes, find the vertical sum of the nodes that are in the same vertical line.
   Return all sums through different vertical lines starting from the left-most vertical line to the right-most vertical line.

   Input:
       1
    /    \
  2      3
 /  \    /  \
4   5  6   7
Output: 
4 2 12 3 7
'''

#User function Template for python3

'''
# Node Class:
class Node:
    def __init__(self,val):
         data = val
         left = None
         right = None
'''


# start from root as index 0.
# If going right, increase the index. 
# If moving left decrease the index.


class Solution:
    def verticalSum(self, root):
        if root is None:
            return 0
        def Xaxis(root,index,dic):
            if root is None:
                return dic
            if index in dic.keys():
                dic[index]+=root.data
            else:
                dic[index]= root.data
            Xaxis(root.left,index-1,dic)
            Xaxis(root.right,index+1,dic)
            return dic
        
        dic=dict()
        dic = Xaxis(root,0,dic)
        
        maxDic = max(dic)
        minDic = min(dic)
        # print( dic)
        v = []
        for i in range(minDic,maxDic+1):
            v.append( dic[i])
        return v
        
