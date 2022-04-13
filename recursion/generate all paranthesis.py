# Given n pairs of parentheses, write a function to generate all
#  combinations of well-formed parentheses of length 2*n.

# For example, given n = 3, a solution set is:
# "((()))", "(()())", "(())()", "()(())", "()()()"

# Again, think recursion.
# At every step, you have 2 options :
# 1) Add ‘(‘ to the string.
# 2) Add ‘)’ to the string.
# However, you need to make sure, that the number of closing 
# brackets do not exceed number of opening brackets at any point of time.
# Also, make sure that the number of opening brackets never exceeds n.

def solve( n, curr,  openn, close, ans):
    if openn==close and openn==n:
        ans.append(curr)
        return
    else:
        if openn<n:
            solve(n, curr+'(', openn+1, close, ans)
        if close<openn:
            solve(n, curr+')', openn, close+1, ans)
            
        
def generateParenthesis( n):
    ans=[]
    solve(n,'',  0, 0, ans)
    return ans

n=int(input())
print(generateParenthesis(n))