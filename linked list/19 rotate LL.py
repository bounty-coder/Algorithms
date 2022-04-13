# Given the head of a linked list, rotate the list to the right by k places.
#find length of LL
# go upto (n-k) node  
# last node's None to first node
# n-k th node's next to none
# n-k+1 as head

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next or k==0:
            return head
        tail=head
        n=1   #calculate Length
        while tail.next:
            tail=tail.next
            n+=1
        k=k%n
        if k==0:
            return head
        i=1
        temp=head
        while i<(n-k):
            temp=temp.next
            i+=1
        temp2=temp.next
        tail.next=head
        temp.next=None
        head=temp2
        return head