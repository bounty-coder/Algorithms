// coin change greedy
// https://www.geeksforgeeks.org/problems/-minimum-number-of-coins4426/1

//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

class Solution{
public:
    vector<int> minPartition(int N)
    {
        vector<int> currency = {1,2,5,10,20,50,100,200,500,2000};
        int c=currency.size();
        vector<int> notes;
        int coins=0;
        while(c>=0){
            if(N>0){
                coins=N/(currency[c-1]);
                for(int i=0;i<coins;i++){
                    notes.push_back(currency[c-1]);
                }
                N%=currency[c-1];
            }
            c--;
        }
        return notes;
    }
};

//{ Driver Code Starts.

int main(){
    int t;
    cin>>t;
    while(t--){
        int N;
        cin>>N;
        
        Solution ob;
        vector<int> numbers = ob.minPartition(N);
        for(auto u: numbers)
            cout<<u<<" ";
        cout<<"\n";
    }
    return 0;
}
// } Driver Code Ends
