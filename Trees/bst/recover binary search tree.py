# Two elements of a binary search tree (BST) are swapped by mistake.
# Tell us the 2 values swapping which the tree will be restored.

# Input : 
#          1
#         / \
#        2   3

# Output : 
#        [1, 2]

# idea is to traverse the tree in inorder as it is already sorted
# find the elements which are swapped in almost sorted array
# A - root of tree

def recoverTree(A):
    stack=[]
    current=A
    ls=[]
    while True:
        if current is not None:
            stack.append(current)
            current=current.left

        elif stack:
            current=stack.pop()
            ls.append(current.val)
            current=current.right
        else:
            break
    # print(ls)
    n=len(ls)
    i=n-1
    while i>0:
        if ls[i]<ls[i-1]:
            j=i-1
            while j>=0 and ls[i]<ls[j]:
                j-=1
            break
        i-=1
    return [ls[i],ls[j+1]]

