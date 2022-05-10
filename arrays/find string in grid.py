# Given a 2D grid of n*m of characters and a word, 
# find all occurrences of given word in grid.
# A word can be matched in all 8 directions at any point. 
# Word is said be found in a direction if all characters
# match in this direction

# Input: word = "abe", grid =
#  {{a,b,a,b},
#   {a,b,e,b},
#   {e,b,e,b}}
# 
# Output: {{0,0},{0,2},{1,0}}

#User function Template for python3

class Solution:
    def searchWord(self, A, B):
        row,col=len(A),len(A[0])

        def dfs(i,j,k):
            if A[i][j]!=B[0]:
                return False
            directions=[[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,1],[1,0],[1,-1]]
            for x,y in directions:
                rd,cd=i+x,j+y
                flag=True
                
                for k in range(1,len(B)):
                    if (0<=rd<row and 0<=cd<col and B[k]==A[rd][cd]):
                        rd+=x
                        cd+=y
                    else:
                        flag=False
                        break
                if flag:
                    return True
            return False
        ls=[]
        for i in range(row):
            for j in range(col):
                if A[i][j]==B[0]:
                    if dfs(i,j,0):
                        ls.append([i,j])
        return ls

#{ 
#  Driver Code Starts
#Initial Template for Python 3


n, m = input().split()
n = int(n); m = int(m);
grid = []
for _ in range(n):
    cur  = input()
    temp = []
    for __ in cur:
        temp.append(__)
    grid.append(temp)
word = input()
obj = Solution()
ans = obj.searchWord(grid, word)
for _ in ans:
    for __ in _:
        print(__, end = " ")
    print()
if len(ans)==0:
    print(-1)

# } Driver Code Ends