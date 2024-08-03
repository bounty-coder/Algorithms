// Given a number N, the task is to count minimum steps to
// minimize it to 1 according to the following criteria:

// If N is divisible by 2 then you may reduce N to N/2.
// If N is divisible by 3 then you may reduce N to N/3.
// Otherwise, Decrement N by 1.

int minSteps(int n) 
{
    int dp[n+1]={0};
    if(n==1)return 0;
    else if(n==2 || n==3) return 1;
    dp[2]=1;
    dp[3]=1;
    for(int i=4;i<n+1;i++){
        int x=INT_MAX;
        if(i%2==0 && i%3==0){
            x=min(dp[i/2],dp[i/3]);
        }
        else if(i%2==0){
            x=dp[i/2];
        }
        else if(i%3==0){
            x=dp[i/3];
        }
        dp[i]=min(x,dp[i-1])+1;
    }
    return dp[n];
} 
