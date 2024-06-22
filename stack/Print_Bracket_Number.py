'''
Given a string str, the task is to find the bracket numbers, i.e., for each bracket in str, return i if the bracket is the ith opening or closing bracket to appear in the string. 

 Examples:

Input:  str = "(aa(bdc))p(dee)"
Output: 1 2 2 1 3 3
Explanation: The highlighted brackets in
the given string (aa(bdc))p(dee) are
assigned the numbers as: 1 2 2 1 3 3.
'''

def bracketNumbers(str):
    if len(str)==0:
        return []
    lb,rb=0,0
    ls=[]
    stack=[]
    for i in str:
        if i=="(":
            lb+=1
            stack.append(lb)
            ls.append(lb)
        elif i==")":
            ls.append(stack.pop())
    return ls
