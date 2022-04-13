# Input: N = 7
# S = T|T&F^T
# Output: 4

# find no of ways to parenthesis the expression so that the value
# expression is True
class Solution:
    def parenthesis_count(self,Str, i, j, isTrue, dp) :
         
        if (i > j) :
          return 0
         
        if (i == j) :
         
          if (isTrue == 1) :
           
            return 1 if Str[i] == 'T' else 0
           
          else :
           
            return 1 if Str[i] == 'F' else 0
         
        if (dp[i][j][isTrue] != -1) :
          return dp[i][j][isTrue]
         
        temp_ans = 0
         
        for k in range(i + 1, j, 2) :
         
          if (dp[i][k - 1][1] != -1) :
            leftTrue = dp[i][k - 1][1]
          else :
            # Count number of True in left Partition
            leftTrue = self.parenthesis_count(Str, i, k - 1, 1, dp)
             
          if (dp[i][k - 1][0] != -1) :
            leftFalse = dp[i][k - 1][0]
          else :
            # Count number of False in left Partition
            leftFalse = self.parenthesis_count(Str, i, k - 1, 0, dp)
          
          if (dp[k + 1][j][1] != -1) :
            rightTrue = dp[k + 1][j][1]
          else :
            # Count number of True in right Partition
            rightTrue = self.parenthesis_count(Str, k + 1, j, 1, dp)
           
          if (dp[k + 1][j][0] != -1) :
            rightFalse = dp[k + 1][j][0]
          else :
            # Count number of False in right Partition
            rightFalse = self.parenthesis_count(Str, k + 1, j, 0, dp)
         
          # Evaluate AND operation
          if (Str[k] == '&') :
            if (isTrue == 1) :
              temp_ans = temp_ans + leftTrue * rightTrue
            else :
              temp_ans = temp_ans + leftTrue * rightFalse + leftFalse * rightTrue + leftFalse * rightFalse
          # Evaluate OR operation
          elif (Str[k] == '|') :
            if (isTrue == 1) :
              temp_ans = temp_ans + leftTrue * rightTrue + leftTrue * rightFalse + leftFalse * rightTrue
            else :
              temp_ans = temp_ans + leftFalse * rightFalse
         
          # Evaluate XOR operation
          elif (Str[k] == '^') :
            if (isTrue == 1) :
              temp_ans = temp_ans + leftTrue * rightFalse + leftFalse * rightTrue
            else :
              temp_ans = temp_ans + leftTrue * rightTrue + leftFalse * rightFalse
          dp[i][j][isTrue] = temp_ans
     
        return temp_ans
                
    def countWays(self, n, S):
        # code here
        dp = [[[-1 for k in range(2)] for i in range(N + 1)] for j in range(N + 1)]
        return self.parenthesis_count(S, 0, N - 1, 1, dp)%1003
        
import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        S = input()
        
        ob = Solution()
        print(ob.countWays(N, S))
