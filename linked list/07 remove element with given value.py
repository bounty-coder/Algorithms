# Given the head of a linked list and an integer val,
#  remove all the nodes of the linked list that 
# has Node.val == val, and return the new head.

#  Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]

# Input: head = [7,7,7,7], val = 7
# Output: []

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None:
            return head
        else:
            temp=head
            while temp.next:
                if temp.next.val==val:
                    new=temp.next.next
                    temp.next=None
                    temp.next=new
                else:
                    temp=temp.next
        if head.val==val:
            curr=head
            head=head.next
        return head