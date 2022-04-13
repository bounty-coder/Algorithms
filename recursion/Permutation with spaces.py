# Given a string you need to print all possible strings that
# can be made by placing spaces (zero or one) in between them.
#  The output should be printed in sorted increasing order of strings

# Easiest Backtracking Solution
# what we will do is fix the A, then pick B or _B
# similarly C or _C and so on backtrack up till end. 

# Input:
# S = "ABC"
# Output: (A B C)(A BC)(AB C)(ABC)

class Solution:
    def solve(self,ip,op,ls):
        if len(ip)==0:
            ls.append(op)
            return
        op1=op+ip[0]
        op2=op+" "+ip[0]
        self.solve(ip[1:],op1,ls)
        self.solve(ip[1:],op2,ls)
    def permutation (self, S):
        # code here
        op=S[0]
        ls=[]
        self.solve(S[1:],op,ls)
        ls.sort()
        return ls

if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        S = input()
        ans = ob.permutation(S);
        write = "";
        for i in ans:
            write += "(" + i + ")"
        print(write)