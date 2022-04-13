# Given the head of a singly linked list, return true if it is a palindrome.

# Input: head = [1,2,2,1]
# Output: true

#steps:
#  go to mid node
#  reverse last half list
#  taverse and check each element

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head.next :
            return True
        else:
            slow=fast=head
            while fast and fast.next:
                slow=slow.next
                fast=fast.next.next
            
            # reverse the list
            temp=slow.next
            slow.next=None
            prev=slow
            while temp:
                curr=temp.next
                temp.next=prev
                prev=temp
                temp=curr
            backhead=prev
            
            temp=head
            backtemp=backhead
            while backtemp and temp:
                if temp.val!=backtemp.val:
                    return False
                    break
                else:
                    temp=temp.next
                    backtemp=backtemp.next
            return True