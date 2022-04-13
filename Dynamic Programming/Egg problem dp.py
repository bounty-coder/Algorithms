import sys
 
MAX = 1000;
 
memo = [[-1 for i in range(MAX)] for j in range(MAX)] ;
 
def solveEggDrop(n, k):
 
    if (memo[n][k] != -1):
        return memo[n][k];
     
    if (k == 1 or k == 0):
        return k;
 
    if (n == 1):
        return k;
 
    min = sys.maxsize;
    res = 0;
 
    for x in range(1,k+1):
        res = max(solveEggDrop(n - 1, x - 1), solveEggDrop(n, k - x));   #max for worst case
        if (res < min):
            min = res;
     
 
    memo[n][k] = min + 1;
    return min + 1;
 
# Driver code
if __name__ == '__main__':
    n = 2;
    k = 36;
    print(solveEggDrop(n, k));