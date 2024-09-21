# https://www.geeksforgeeks.org/problems/clone-a-linked-list-with-next-and-random-pointer/1

# Clone a linked list with next and random pointer
# Given a linkedlist and it has two pointers, next and random. Next will point to next, but the random may point to any nodes given in list.
# You have to create an exact copy of this LinkedList.


# Approach
''' 
    1. Create all nodes first, and save in a dictionary(map)
    2. Traverse again the list, but this time create the next and random nodes
'''

def copyList(head):
    d = dict()
    
    temp = head
    while temp:
        d[temp] = Node(temp.data)
        temp = temp.next
    
    d[None] = None
    temp = head
    while temp:
        d[temp].next = d[temp.next]
        d[temp].random = d[temp.random]
        temp = temp.next
    
    return d[head]
