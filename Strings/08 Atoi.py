# Implement atoi to convert a string to an integer.

# Input : "9 2704"
# Output : 9

# Input: "-54332872018247709407 4 54"
# output:  -2147483648
def atoi(A):
    A=A.split()
    if A[0][0]=="+" or A[0][0]=="-":
        i=1
    else:
        i=0
    s=""
    while i<len(A[0]) and A[0][i].isdigit():
        s+=A[0][i]
        i+=1
    l=s
    if s.isdigit() and int(s)>2147483647:
        s="2147483647"

    if s.isdigit() and int(l)>2147483648 and A[0][0]=="-":
        s="2147483648"
    
    if A[0][0]=="+" and len(s)>0:
        return s
    elif A[0][0]=="-" and len(s)>0:
        return "-"+str(int(s))
    elif s.isdigit():
        return int(s)
    return 0

A="-54332872018247709407 4 54"
print(atoi(A))