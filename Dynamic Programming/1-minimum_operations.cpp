// Given a number N. Find the minimum number of operations required
// to reach N starting from 0. You have 2 operations available:

// Double the number
// Add one to the number

// // Input:
// N = 8
// Output: 4
// Explanation: 
// 0 + 1 = 1 --> 1 + 1 = 2 --> 2 * 2 = 4 --> 4 * 2 = 8.


int minOperation(int n)
{
    if(n==0){
        return 0;
    }
    int dp[n+1]={0};
    dp[1]=1;
    for(int i=2;i<=n;i++){
        int x=INT_MAX;
        if(i&1){    //if number is odd then, check for i*2+1 = n
            x=dp[i/2]+1;
        }
        else{        // if number is even then, i*2 = n
            x=dp[i/2];
        }
        dp[i]=min(x,dp[i-1])+1;    // check if i+1 or i/2 is min
    }
    return dp[n];
}
