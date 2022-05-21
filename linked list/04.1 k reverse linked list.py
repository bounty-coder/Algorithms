# Given a singly linked list and an integer K, reverses the nodes of the
# list K at a time and returns modified linked list.

# ip: 1 -> 2 -> 3 -> 4 -> 5 -> 6 and K=2
# op: 2 -> 1 -> 4 -> 3 -> 6 -> 5

# Input: 1->2->3->4->5->6->7->8->NULL, K = 3 
# Output: 3->2->1->6->5->4->8->7->NULL 

# Try to split the list into buckets of K.
# Split the list into buckets of length K and then 
# reverse each of them. After this you have to concatenate the
#  buckets and return the list. To split the list into buckets
#  of length K, use 2 pointers that are K elements afar.

#iterative approach
def reverseList1(A, B):
    if B == 1:
        return A
    l=None
    prev,curr=None,A  
    while curr!=None:
        k=B
        head=curr
        p,n=None,curr.next  # using two pointers(previous and next)
        while curr!=None and k>1:
            curr.next=p
            p=curr
            curr=n
            n=n.next if n else None
            k-=1
        head.next=curr.next
        curr.next=p
        if prev:
            prev.next=curr
        else:
            l=curr
        prev=head
        curr=head.next
    return l

#same recursive soln
def reverseList( head,k):
    
    if head == None:
        return None
    current = head
    next = None
    prev = None
    count = 0

    # Reverse first k nodes of the linked list
    while(current is not None and count < k):
        next = current.next
        current.next = prev
        prev = current
        current = next
        count += 1

    # next is now a pointer to (k+1)th node
    # recursively call for the list starting
    # from current. And make rest of the list as
    # next of first node
    if next is not None:
        head.next = reverseList(next, k)

    # prev is new head of the input list
    return prev