# Given a positive integer A, return its corresponding column title
#  as appear in an Excel sheet.

# Input 1: A = 1
# op: "A"

# Input 2: A = 28
# op: "AB"

def convertToTitle( A):
    s=""
    while A:
        rem=A%26
        A=A//26
        if rem==0:
            c='Z'
            A-=1  #for carry
        else:
            c=chr(ord('A')+rem-1)
        s=c+s
    return s

A= int(input())
print(convertToTitle(A))