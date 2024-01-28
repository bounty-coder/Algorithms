//{ Driver Code Starts
// Initial Template for C++
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
// User function Template for C++
class Solution {
  public:
	bool isPrime(int n){
	    int i=2;
	    if(n==2) return true;
	    if(n%2==0)return false;
	    i++;
	    bool prime=false;
	    while(i*i<=n){
	        if(n%i==0){
	            return prime;
	        }
	        i+=2;
	    }
	    return true;
	}
    vector<int> allPrime(int n){
        vector<int> allprime;
        if(n<=1) return allprime;
        allprime.push_back(2);
        if(n==2){
            return allprime; 
        }
        int i=3;
        while(i<=n){
            if(isPrime(i)){
                allprime.push_back(i);
            }
            i+=2;
        }
        return allprime;
    }
    vector<int> leastPrimeFactor(int n) {
        vector<int> least;
        least.push_back(0);
        vector<int> allprime = allPrime(n);
        if(n>=1){
            least.push_back(1);
        }
        for(int i=2;i<=n;i++){
            for(auto j:allprime){
                if(i%j==0){
                    least.push_back(j);
                    break;
                }
            }
        }
        return least;
    }
};

//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        Solution ob;
        vector<int>ans = ob.leastPrimeFactor(n);
        for(int i=1;i<=n;i++)cout<<ans[i]<<" ";
        cout<<endl;  
    }
    return 0;
}

// } Driver Code Ends
