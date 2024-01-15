//Unbounded Knapsack
/* Difference between unbounded and bounded knapsack is, in unbounded knapsack u can pick any number of same item until the weight(knpasack/target) is not fulfilled)
  Code variation will be-> just don't reduce the number of item, and use again the same item*/

//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
// User function Template for C++

class Solution{
public:
    int knapSack(int N, int W, int val[], int wt[])
    {
        if(N<0) return 0;
        vector<vector<int>> dp(W+1,vector<int>(N+1,0));
        for(int i=1;i<W+1;i++){
            for(int j=1;j<N+1;j++){
                if(wt[j-1]<=i){
                    dp[i][j]=max(dp[i][j-1],val[j-1]+dp[i-wt[j-1]][j]);   //code variation here only => not reducing the number of N(item)
                }
                else{
                    dp[i][j]=dp[i][j-1];
                }
            }
        }
        return dp[W][N];
    }
};

//{ Driver Code Starts.

int main(){
    int t;
    cin>>t;
    while(t--){
        int N, W;
        cin>>N>>W;
        int val[N], wt[N];
        for(int i = 0;i < N;i++)
            cin>>val[i];
        for(int i = 0;i < N;i++)
            cin>>wt[i];
        
        Solution ob;
        cout<<ob.knapSack(N, W, val, wt)<<endl;
    }
    return 0;
}
// } Driver Code Ends
