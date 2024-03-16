# https://www.geeksforgeeks.org/problems/delete-without-head-pointer/1
'''
You are given a node del_node of a Singly Linked List where you have to delete a value of the given node from the linked list but you are not given the head of the list.

By deleting the node value, we do not mean removing it from memory. We mean:

The value of the given node should not exist in the linked list.
The number of nodes in the linked list should decrease by one.
All the values before & after the del_node node should be in the same order.
'''



def deleteNode(self,del_node):
      del_node.data=del_node.next.data
      if del_node.next.next:
          del_node.next=del_node.next.next
      else:
          del_node.next=None

# u do not have to actually delete the pointer, instead delete the value of the pointer and swap next values in it.Delete the next pointer and pointer change to the next's next pointer
