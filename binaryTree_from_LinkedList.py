from collections import deque
#Function to make binary tree from linked list.
def convert(head):
    if not head:
        return None
    q=deque()
    root=Tree(head.data)
    q.append(root)
    temp=head
    while q:
        node=q.popleft()
        if temp.next:
            lft=Tree(temp.next.data)
            node.left=lft
            q.append(lft)
            temp=temp.next
        if temp.next:
            rgt=Tree(temp.next.data)
            node.right=rgt
            q.append(rgt)
            temp=temp.next
    
    return root
