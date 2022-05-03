# Given a column title A as appears in an Excel sheet, return its
# corresponding column number.

# Input: "A"
# Op: 1

# Input:"AB"
# Op: 28

def titleToNumber(A):
    result=0
    for i in range(len(A)):
        result*=26
        result+=ord(A[i])-ord('A')+1
    return result

A=str.upper(input())
print(titleToNumber(A))