#User function Template for python3
# Given two singly linked lists of size N and M,
# write a program to get the point 
# where two linked lists intersect each other.

#TC- O(n)
#SC- O(n) if list is large not efficient

# use a hash to store list first list's node
# check in 2nd list if the node exist

#Function to find intersection point in Y shaped Linked Lists.
def intersetPoint(head1,head2):
    #code here
    #use of hash table
    dic=set()
    if head1 is None or head2 is None:
        return -1
    temp1=head1
    while temp1:
        if temp1 not in dic:
            dic.add(temp1)
        temp1=temp1.next
    temp2=head2
    while temp2:
        if temp2 in dic:
            return temp2.data
        temp2=temp2.next
    return -1

# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        temp=None
    
    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_node):
        if self.head is None:
            self.head = new_node
            self.temp = self.head
            return
        else:
            self.temp.next = new_node
            self.temp = self.temp.next

if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        x,y,z = map(int,input().strip().split())
        a = LinkedList()  # create a new linked list 'a'.
        b = LinkedList()  # create a new linked list 'b'.
        nodes_a = list(map(int, input().strip().split()))
        nodes_b = list(map(int, input().strip().split()))
        nodes_common = list(map(int, input().strip().split()))

        for x in nodes_a:
            node=Node(x)
            a.append(node)  # add to the end of the list

        for x in nodes_b:
            node=Node(x)
            b.append(node)  # add to the end of the list

        for i in range(len(nodes_common)):
            node=Node(nodes_common[i])
            a.append(node)  # add to the end of the list a
            if i== 0:
                b.append(node)  # add to the end of the list b, only the intersection
        
        print(intersetPoint(a.head,b.head))

# } Driver Code Ends