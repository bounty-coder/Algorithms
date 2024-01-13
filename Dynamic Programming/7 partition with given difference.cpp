// https://www.geeksforgeeks.org/problems/partitions-with-given-difference/1
#include <bits/stdc++.h>
using namespace std;

class Solution {
//   public:
//     int countPartitions(int n, int d, vector<int>& arr) {
//         // Code here
//         int mod=1e9+7;
//         int sum=0;
//         for(auto i:arr){
//             sum+=i;
//         }
//         if(sum%2==1)return 0;
//         int W=(sum+d)/2;
        
//         int dp[W+1][n+1]={0};
        
//         for(int i=0;i<n+1;i++){
//             dp[0][i]=1;
//         }
        
//         for(int i=1;i<W+1;i++){
//             for(int j=1;j<n+1;j++){
//                 if(arr[j-1]<=i){
//                     dp[i][j]=(dp[i][j-1]+dp[i-arr[j-1]][j-1])%mod;
//                 }
//                 else{
//                     dp[i][j]=dp[i][j-1]%mod;
//                 }
//             }
//         }
//         return dp[W][n]%mod;
//     }
    int mod = (int)(1e9+7);
  public:
    int countPartitions(int n, int d, vector<int>& arr) {
        int total_sum = 0;
        for(auto it : arr) total_sum += it;
        if(total_sum-d < 0 || (total_sum-d)%2) return 0;          // S2 cannot be a decimal number
        int s2 = (total_sum-d)/2;
        vector<vector<int>> dp(n,vector<int>(s2+1,0));
        
        if(arr[0]==0) dp[0][0] = 2;
        else dp[0][0]=1;
        if(arr[0]!=0 && arr[0] <= s2) dp[0][arr[0]]=1;
        
        for(int ind=1; ind<n; ind++){
            for(int sum = 0; sum <= s2; sum++){
                int take = 0;
                if(arr[ind]<=sum) take = dp[ind -1][sum - arr[ind]];
                int not_take = dp[ind-1][sum];
                
                dp[ind][sum] =(take+not_take)%mod;
            }
        }
        return dp[n-1][s2];
    }
};

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n, d;
        cin >> n >> d;
        vector<int> arr;

        for (int i = 0; i < n; ++i) {
            int x;
            cin >> x;
            arr.push_back(x);
        }

        Solution obj;
        cout << obj.countPartitions(n, d, arr) << "\n";
    }
    return 0;
}
