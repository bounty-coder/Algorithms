// https://www.geeksforgeeks.org/problems/high-effort-vs-low-effort0213/1

/* Question from GFG
You are given n days and for each day (di) you can select one of the following options:
1)perform no task 
2)perform a high effort task (hi) only if its the first day or if you chose no-task on the previous day
3)perform a low effort task (li)
Write a program to find the maximum amount of tasks you can perform within these n days. 

Input:
n = 3
hi[] = {2,8,1}
li[] = {1,2,1}
Output: 9  */

//{ Driver Code Starts
#include <iostream>
#include <vector>
using namespace std;
// Solution 1 recursive
class Solution
{
    vector<int> dp;
    public:
        int func(int curr,int n,bool choosetask,int hi[],int li[]){
            if(curr==n){
                return 0;
            }
            if(dp[curr]!=-1 && !choosetask) return dp[curr];
            int result = 0;
            if(choosetask==false){
                result = max(hi[curr]+func(curr+1,n,true,hi,li),
                           max(li[curr]+func(curr+1,n,true,hi,li),
                           func(curr+1,n,false,hi,li)));
            }
            else{
                result = max(li[curr]+func(curr+1,n,true,hi,li),
                           func(curr+1,n,false,hi,li));
            }
            if(!choosetask) dp[curr] = result;
            return result;
        }
        int maxAmt(int n , int hi[] , int li[])
        {
            if(n<=0) return 0;
            dp = vector<int>(n, -1);
            bool choosetask=false;
            return func(0,n,choosetask,hi,li);
        }
};
//Solution 2 iterative
class Solution
{
    vector<vector<int>> dp;
public:
    int maxAmt(int n , int hi[] , int li[]){
        if(n<=0)  return 0;
        dp = vector<vector<int>>(n+1,vector<int>(2,0));
        for(int i=n-1;i>=0;i--){
            dp[i][0]= max(hi[i] + dp[i+1][1],max(li[i]+dp[i+1][1], dp[i+1][0]));
            dp[i][1]= max(li[i]+dp[i+1][1], dp[i+1][0]);
        }
        return dp[0][0];
    }
}

int main()
{
    int t;
    cin>>t;
    while(t--)
        {
            int n;
            cin>>n;
            int hi[n] , li[n];
            for(int i = 0 ;i<n;i++)
                cin>>hi[i];
            for(int i = 0 ;i<n;i++)
                cin>>li[i];
            Solution ob;
            cout<<ob.maxAmt(n,hi,li)<<endl;    
        }
}
