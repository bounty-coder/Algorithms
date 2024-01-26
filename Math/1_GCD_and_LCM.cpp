/* Finding GCD & LCM of two numbers*/

// a*b= gcd*lcm
// gcd = using euclidean algorithm


//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution {
  public:
    long long gcd(long long A , long long B) {
        if(B==0){
            return A;
        }
        gcd(B,A%B);
    }
    vector<long long> lcmAndGcd(long long A , long long B) {
        vector<long long> op;
        long long g = gcd(A,B);
        long long l = A*B/g;
        op.push_back(l);
        op.push_back(g);
        return op;
    }
};

int main() {
    int t;
    cin >> t;
    while (t--) {
        long long A,B;
        
        cin>>A>>B;

        Solution ob;
        vector<long long> ans = ob.lcmAndGcd(A,B);
        cout<<ans[0]<<" "<<ans[1]<<endl;
    }
    return 0;
}
