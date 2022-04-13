# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. 
# Only nodes themselves may be changed.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# reverse the last half LL
# input 





class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        # checking the LL to be empty
        if head==None:
            return head
        else:

            # find the middle node
            slow=head
            fast=head
            while fast.next:
                slow=slow.next
                if fast.next.next is None:
                    break
                fast=fast.next.next

            # reverse the LL
            temp=slow
            curr=None
            prev=None
            while temp:
                curr=temp.next
                temp.next=prev
                prev=temp
                temp=curr
            backhead=prev
            
            # traverse from both side and attach the node as per given in que
            temp=head
            backtemp=backhead
            
            while backtemp.next:
                curr=temp.next
                backcurr=backtemp.next
                temp.next=backtemp
                backtemp.next=curr
                temp=curr
                backtemp=backcurr
            return head
                
        