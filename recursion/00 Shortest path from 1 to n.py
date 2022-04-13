# Consider a directed graph whose vertices are numbered from
#  1 to n. There is an edge from a vertex i to a vertex j iff
#  either j = i + 1 or j = 3 * i. The task is to find the min
# number of edges in a path in G from vertex 1 to vertex n.

class Solution:
    # recursive solution
    def minStep (self, n):
        if n==1:
            return 0
        if n%3==0:
            return 1+self.minStep(n//3)
        else:
            return 1+self.minStep(n-1)

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        ob = Solution()
        print(ob.minStep(n))

# iterative approach
def minStep ( n):
    count=0
    while n>1:
        if n%3==0:
            n/=3
        else:
            n-=1
        count+=1
    return count