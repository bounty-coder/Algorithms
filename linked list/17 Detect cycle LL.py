# Given a linked list of N nodes. 
# The task is to check if the linked list has a loop.
#  Linked list can contain self loop.
'''
# 1.Hashing Approach
Traverse the list one by one and keep putting the node addresses in a Hash Table.
 At any point, if NULL is reached then return false,
and if the next of the current nodes points to any of the previously
 stored nodes in  Hash then return true.

def detectLoop(self):
        s = set()
        temp = self.head
        while (temp):
            if (temp in s):
                return True
            s.add(temp)
            temp = temp.next
        return False

TC: O(n)   &  SC: O(n)
'''

# 2.Traverse linked list using two pointers.
# Move slow_p by one and fast_p by two.
# If these pointers meet at the same node then there is a loop.
#  If pointers do not meet then linked list doesn’t have a loop.

class Solution:
    #Function to check if the linked list has a loop.
    def detectLoop(self, head):
        #code here
        if not head:
            return None
        slow=fast=head
        while fast and fast.next:
            
            slow=slow.next
            fast=fast.next
            if slow==fast:
                return True
        return False

# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next
    
    #connects last node to node at position pos from begining.
    def loopHere(self,pos):
        if pos==0:
            return
        
        walk = self.head
        for i in range(1,pos):
            walk = walk.next
        
        self.tail.next = walk

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        
        LL = LinkedList()
        for i in input().split():
            LL.insert(int(i))
        
        LL.loopHere(int(input()))
        
        print(Solution().detectLoop(LL.head))
