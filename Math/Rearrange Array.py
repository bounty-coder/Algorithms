# Rearrange a given array so that Arr[i] becomes Arr[Arr[i]]
# with O(1) extra space. (without using any array)

# ip-[ 4, 0, 2, 1, 3 ]
# op-[ 3, 4, 2, 0, 1 ]

# Approach 1 directly using another array(discarded)
# Aprroach 2 
# so we have to store 2 numbers at a place(old&new). But how to do this??
# trick: Increase every Array element Arr[i] by (Arr[Arr[i]] % n)*n.
# then: Divide every element by N.
#    A = B + C * N   if ( B, C < N )
#    A % N = B
#    A / N = C

def arrange(A):
    n=len(A)

    # First step: Increase all values
    # by (arr[arr[i]] % n) * n
    for i in range(n):
        A[i]+=(A[A[i]]%n)*n
    
    # Second Step: Divide all values
    # by n
    for i in range(n):
        A[i]//=n 
    return A

A=[3, 2, 0, 1]
print(arrange(A))