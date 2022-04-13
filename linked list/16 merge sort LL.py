''' 
    MergeSort(headRef)
1) If the head is NULL or there is only one element in the Linked List 
    then return.
2) Else divide the linked list into two halves.  
      FrontBackSplit(head, &a, &b); /* a and b are two halves */
3) Sort the two halves a and b.
      MergeSort(a);
      MergeSort(b);
4) Merge the sorted a and b (using SortedMerge() discussed here) 
   and update the head pointer using headRef.
     *headRef = SortedMerge(a, b);
 
'''
# approach 1:
# def mergeTwoLists(a, b):
#     if a.val > b.val:
#         a, b = b, a

#     h = a
    
#     while a.next and b:
#         if a.next.val < b.val:
#             a = a.next
#         else:
#             a.next, b.next, a, b = b, a.next, b, b.next
            
#     if b:
#         a.next = b
        
#     return h

# approach 2 recursive
class Solution:
    def sortedMerge(self, a, b):
        result = None
         
        # Base cases
        if a == None:
            return b
        if b == None:
            return a
             
        # pick either a or b and recur..
        if a.data <= b.data:
            result = a
            result.next = self.sortedMerge(a.next, b)
        else:
            result = b
            result.next = self.sortedMerge(a, b.next)
        return result
     
    def mergeSort(self, h):
         
        # Base case if head is None
        if h == None or h.next == None:
            return h
 
        # get the middle of the list
        middle = self.getMiddle(h)
        nexttomiddle = middle.next
 
        # set the next of middle node to None
        middle.next = None
 
        # Apply mergeSort on left list
        left = self.mergeSort(h)
         
        # Apply mergeSort on right list
        right = self.mergeSort(nexttomiddle)
 
        # Merge the left and right lists
        sortedlist = self.sortedMerge(left, right)
        return sortedlist
     
    # Utility function to get the middle
    # of the linked list
    def getMiddle(self, head):
        if (head == None):
            return head
 
        slow = head
        fast = head
 
        while (fast.next != None and
               fast.next.next != None):
            slow = slow.next
            fast = fast.next.next
             
        return slow
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

# Node Class
class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None


# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node    
            return
        self.tail.next = new_node
        self.tail = new_node

# prints the elements of linked list starting with head
def printList(head):
    if head is None:
        print(' ')
        return
    curr_node = head
    while curr_node:
        print(curr_node.data,end=" ")
        curr_node=curr_node.next
    print(' ')


if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        n = int(input())
        p = LinkedList() # create a new linked list 'a'.
        nodes_p = list(map(int, input().strip().split()))
        for x in nodes_p:
            p.append(x)  # add to the end of the list

        printList(Solution().mergeSort(p.head))