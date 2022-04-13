# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single digit.
#  Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def makenum(self,head):
        if head is None:
            return 0
        else:
            return head.val+self.makenum(head.next)*10
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        m=self.makenum(l1)
        n=self.makenum(l2)
        c=m+n
        c=list(str(c))
        ll3=ListNode()
        
        for i in range(0,len(c)):
            if i==len(c)-1:
                ll3.val=c[i]
            else:
                temp=ListNode()
                temp.val=c[i]
                temp.next=ll3.next
                ll3.next=temp
        return ll3