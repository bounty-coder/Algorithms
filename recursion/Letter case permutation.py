# Given a string s, you can transform every letter individually to
#  be lowercase or uppercase to create another string.

# Input: s = "a1b2"
# Output: ["a1b2","a1B2","A1b2","A1B2"]

def solve(ip,op,l):
    if len(ip)==0:
        l.add(op)
        return 
    op1=op+ip[0].upper()
    op2=op+ip[0].lower()
    solve(ip[1:],op1,l)
    solve(ip[1:],op2,l)
    
def letterCasePermutation(s):
    op=""
    l=set()
    solve(s,op,l)
    return list(l)

s=input()
letterCasePermutation(s)