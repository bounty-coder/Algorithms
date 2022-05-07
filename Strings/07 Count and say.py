# The count-and-say sequence is the sequence of integers beginning as follows: 
# 1, 11, 21, 1211, 111221, ...
# 1 is read off as one 1 or 11. 11 is read off as two 1s or 21.
# 21 is read off as one 2, then one 1 or 1211.

# Given an integer n, generate the nth sequence.
# if n = 2, the sequence is 11.

def countAndSay(n):
    if n==1:
        return "1" 
    if n==2:
        return "11" 
    s="11"
    for i in range(2,n):
        t=""
        s=s+'&'
        c=1
        for j in range(1,len(s)):
            if s[j]!=s[j-1]:
                t=t+str(c)
                t=t+s[j-1]
                c=1
            else:
                c+=1
        s=t
    return s