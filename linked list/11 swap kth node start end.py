# You are given the head of a linked list, and an integer k.

# Return the head of the linked list after swapping the
#  values of the kth node from the beginning and the kth
#  node from the end (the list is 1-indexed).


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """  
        node1 = node2 = head
        l = 0   # recode lenght of head
        while node1 :
            l += 1
            if l == k : # move to node1
                t1 = node1  # recode node1 data 
                
            node1 = node1.next
            
            if not node1 : # snap all element
                if l == k == 1 :
                    return head
                
                elif l%2==0 and k > l//2 :
                    return self.swapNodes(head, l-k+1)
                
                elif k > l//2+1 : 
                    return self.swapNodes(head, l-k+1)
                
                else :     
                    node2 = t1
                    for _ in range(l-k-k+1) : 
                        node2 = node2.next

                    t2 = node2 # recode node2 data 
                
                    t1.val, t2.val = t2.val, t1.val  #swap
                    
                    return head