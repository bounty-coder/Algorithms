# Python program to evaluate expression tree
 

#  As all the operators in the tree are binary hence each node will have either 0 or 2 children.

# Algorithm :
# Let t be the syntax tree
# If  t is not null then
#       If t.info is operand then  
#          Return  t.info
#       Else
#          A = solve(t.left)
#          B = solve(t.right)
#          return A operator B
#          where operator is the info contained in t

# Class to represent the nodes of syntax tree
 
 
class node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
 
# This function receives a node of the syntax tree
# and recursively evaluate it
 
 
def evaluateExpressionTree(root):
 
    # empty tree
    if root is None:
        return 0
 
    # leaf node
    if root.left is None and root.right is None:
        return int(root.data)
 
    # evaluate left tree
    left_sum = evaluateExpressionTree(root.left)
 
    # evaluate right tree
    right_sum = evaluateExpressionTree(root.right)
 
    # check which operation to apply
    if root.data == '+':
        return left_sum + right_sum
 
    elif root.data == '-':
        return left_sum - right_sum
 
    elif root.data == '*':
        return left_sum * right_sum
 
    else:
        return left_sum / right_sum
 
 
# Driver function to test above problem
if __name__ == '__main__':
 
    # creating a sample tree
    root = node('+')
    root.left = node('*')
    root.left.left = node('5')
    root.left.right = node('4')
    root.right = node('-')
    root.right.left = node('100')
    root.right.right = node('20')
    print(evaluateExpressionTree(root))
 
    root = None
 
    # creating a sample tree
    root = node('+')
    root.left = node('*')
    root.left.left = node('5')
    root.left.right = node('4')
    root.right = node('-')
    root.right.left = node('100')
    root.right.right = node('/')
    root.right.right.left = node('20')
    root.right.right.right = node('2')
    print(evaluateExpressionTree(root))