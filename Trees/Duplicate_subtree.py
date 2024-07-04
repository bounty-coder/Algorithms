'''
    Given a binary tree, your task is to find all duplicate subtrees from the given binary tree.
    Duplicate Subtree : Two trees are duplicates if they have the same structure with the same node values.
    Note:  Return the root of each tree in the form of a list array & the driver code will print the tree in pre-order tree traversal in lexicographically increasing order.
    Link: https://www.geeksforgeeks.org/problems/duplicate-subtrees/1
'''

'''
    The plan is to traverse each node and save that node along with its subtree in map and later check if the subtree has been encountered earlier
    Now the question is how will you store the subtree?
    What Data structure u will use?
    So, we will go ahead with a string and wherever it's NULL we will fill 'N'. Later check if this has been encountered twice. If it came twice then add the node in answer
'''
def printAllDups(root):
    ans=[]
    mp ={}
    def solve(root,mp,ans):
        if root==None:
            return "N"
        s=str(root.data) + "," + solve(root.left,mp,ans) + "," + solve(root.right,mp,ans)
        if s in mp:
            mp[s]+=1
        else:
            mp[s]=1
        if mp[s]==2:
            ans.append(root)
        return s
    solve(root,mp,ans)
    return ans
