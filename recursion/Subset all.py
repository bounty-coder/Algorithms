# Print all subsequences of a string
# Input : abc
# Output : a, b, c, ab, bc, ac, abc

# Pick and Don’t Pick Concept

def recursion(ip,op):
    if len(ip)==0:
        print(op,end=" ")
        return

    # output is passed with including the
    # 1st character of input string
    recursion(ip[1:],op+ip[0])

    # output is passed without including the
    # 1st character of input string
    recursion(ip[1:],op)


ip=input()
op=""
recursion(ip,op)