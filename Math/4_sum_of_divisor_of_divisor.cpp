/*Given a natural number N, the task is to find the sum of the divisors of all the divisors of N.*/
// https://www.geeksforgeeks.org/problems/find-sum-of-divisors5636/1

//{ Driver Code Starts
#include<bits/stdc++.h> 
using namespace std; 

// } Driver Code Ends
//User function Template for C++
class Solution
{
public:
    int AllDivisor(int n,bool single){
        int sum=0;
        for(int i=1;i*i<=n;i++){
            if(n%i==0){
                if(!single){
                    sum+=AllDivisor(i,true);
                }
                else{
                    sum+=i;
                }
                if(n/i!=i){
                    if(!single){
                        sum+=AllDivisor(n/i,true);
                    }
                    else{
                        sum+=n/i;
                    }
                }
            }
        }
        return sum;
    }
    int sumOfDivisors(int N)
    {
        return AllDivisor(N,false);
    }
};

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int N;
        cin>>N;
        Solution ob;
        int ans  = ob.sumOfDivisors(N);
        cout<<ans<<endl;
    }
    return 0;
}
