# Reverse a linked list from position m to n. Do it in-place and in one-pass.
# Given 1->2->3->4->5->NULL, m = 2 and n = 4,
# return 1->4->3->2->5->NULL.

#A=head, B/C=start/end node number
def reverseBetween(A, B, C):
    head = A
    current = A
    prv = None
    nxt = None
    
    step = 1
    
    while current is not None:
        
        if step < B:
            prv = current
            current = current.next

        if step >= B and step <= C:
            if step == B:
            # this is a start of the reversed list
                last_non_reversed = prv
                last_reversed = current
            
            if step == C:
                # this is the end of the reversed list
                first_reversed = current
                first_non_reversed = current.next
            
            # part that does reverse
            nxt = current.next
            current.next = prv
            prv = current
            current = nxt

        if step > C:
            # We can skip these steps
            break
        
        step += 1
    
    if last_non_reversed is not None:
        last_non_reversed.next = first_reversed
        
    last_reversed.next = first_non_reversed
    
    if B == 1:
        # In this case we did reverse from the very first element
        head = prv
        
    return head
