# Divide two integers without using multiplication, division and mod operator.
# Return the floor of the result of the division.

# dividend=quo*divisor+rem

#Approach 1
# Keep subtracting the divisor from the dividend until dividend becomes less than divisor. 

#approach 2
# double the number and check if it is greater than dividend
def divide( A, B):
    # 1.(++,--)=positive, 2.(+-,-+)=neg
    sign=(-1 if (A<0)^(B<0) else 1)
    A=abs(A)
    B=abs(B)
    result=0
    while (A-B>=0):
        count=0
        # A-something>=0
        #defining something how?
        #left shifting 2**count times(1<<count=2**count)
        while (A-(B<<1<<count)>=0):
            count+=1
        result+=1<<count
        A-=B<<count
    if sign==-1:
        return -result
    return result

A=int(input("Enter A:"))
B=int(input("Enter B:"))
print(divide(A,B))