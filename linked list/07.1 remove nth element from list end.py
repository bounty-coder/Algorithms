# Given a linked list, remove the nth node from the end of list 
# and return its head.

# Given linked list: 1->2->3->4->5, and n = 2.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

# Approach 1: count total nodes, subtract n.
# again traverse from start to total-n and remove 
# that node.  TC- O(2n)
def removeNthFromEnd( A, B):
    length = 0
    cur = A
    while cur:     ##calculating the length of the list
        length += 1
        cur = cur.next
    if B >= length:    ## if this is the case deleting the head node of the list
        return A.next
    n = length - B    ## calucalting the node to be removed from listhead (node index starts with 'zero')
    count = 0
    prev = None
    cur = A
    while count < n:
        prev = cur
        cur = cur.next
        count += 1
    if cur.next is not None:    ## cur is the node required to be removed
        prev.next = cur.next    ## removing the cur node from list by linking the prev node directly to next of the cur node
    else:
        prev.next = None
    return A 
 
# Approach 2: 2 pointer approach TC-O(n)
def removeNthFromEnd( head, n):
    start=ListNode(1)
    start.next=head
    # Take two pointers – fast and slow. 
    # And initialize their values as head node
    fast=start
    slow=start

    # Iterate fast pointer till the value of n.
    for i in range(n):
        # Given in que(not necessary): If n is greater than the size of the
        # list, remove the first node of the list.
        if not fast.next:
            return start.next.next
        fast=fast.next

    # Now, start iteration of fast pointer till the None value 
    # of the linked list. Also, iterate slow pointer.
    # Hence, once the fast pointer will reach to the end the 
    # slow pointer will reach the node which you want to delete.
    while fast.next:
        fast=fast.next
        slow=slow.next
    
    # Replace the next node of the slow pointer with the next
    # to next node of the slow pointer.
    slow.next=slow.next.next

    return start.next