# https://www.geeksforgeeks.org/problems/construct-list-using-given-q-xor-queries/1

'''
Given a list s that initially contains only a single value 0. There will be q queries of the following types:

0 x: Insert x in the list
1 x: For every element a in s, replace it with a ^ x. ('^' denotes the bitwise XOR operator)
Return the sorted list after performing the given q queries. 

'''

'''
Input:
q = 5
queries[] = {{0, 6}, {0, 3}, {0, 2}, {1, 4}, {1, 5}}
Output:
1 2 3 7
Explanation:
[0] (initial value)
[0 6] (add 6 to list)
[0 6 3] (add 3 to list)
[0 6 3 2] (add 2 to list)
[4 2 7 6] (XOR each element by 4)
[1 7 2 3] (XOR each element by 5)
The sorted list after performing all the queries is [1 2 3 7]. 
'''

#Normal soln
def constructList(q : int, queries : List[List[int]]) -> List[int]:
    s = [0]
    for i in queries:
        if i[0]==0:
            s.append(i[1])
        elif i[0]==1:
            for j in range(len(s)):
                s[j]=s[j]^i[1]
    s.sort()
    return s



# Think Again
# Can we somehow, precalculate it?
def constructList(q : int, queries : List[List[int]]) -> List[int]:
    s = []
    x = 0
    for i in reversed(queries):
        if i[0]==0:
            s.append(i[1]^x)
        elif i[0]==1:
            x^=i[1]
    s.append(x)
    s.sort()
    return s


# We started from backwards of the list
# queries = (0, a), (0, b), (0, c) ... (1, x1) (0, d) (1, x2)

#  [a b c]
#  [a^x1 b^x1 c^x1]
#  [a^x1 b^x1 c^x1 d]
#  [a^x1^x2 b^x1^x2 c^x1^x2 d^x2]

# so we can solve it backwards by keeping track of running xor, saving
# us O(n) factor for repeatedly applying xor

# TC- O(n+nlogn) ~ O(nlogn)
