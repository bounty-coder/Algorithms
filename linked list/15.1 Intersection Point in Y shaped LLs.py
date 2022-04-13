
# TC- O(m+n)
# SC- O(1) improved

def getIntersectionNode(headA, headB):
    
    #count the number of nodes in A(length)
    temp1=headA
    a=0
    while temp1:
        temp1=temp1.next
        a+=1
    
    #counting B nodes
    temp2=headB
    b=0
    while temp2:
        temp2=temp2.next
        b+=1
    
    #difference between both length
    c=b-a
    #traverse the longer length LL uptil the both become same length
    if c>0:
        xb=headB
        while c and xb:
            xb=xb.next
            c-=1
        temp1=headA
        while temp1 and xb:
            if temp1==xb:
                return xb
            temp1=temp1.next
            xb=xb.next
    elif c<0:
        xa=headA
        while c and xa:
            xa=xa.next
            c-=1
        temp2=headB
        while temp2 and xa:
            if temp2==xa:
                return xa
            temp2=temp2.next
            xa=xa.next
    elif c==0:
        return headA
    return None