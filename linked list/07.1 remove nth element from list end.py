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