//https://www.geeksforgeeks.org/problems/maximize-dot-product2649/1

/* Given two arrays a and b of positive integers of size n and m where n >= m, the task is to maximize the dot product by inserting zeros in the second array but you cannot disturb the order of elements. 
Dot product of array a and b of size n is a[0]*b[0] + a[1]*b[1] + ... + a[n-1]*b[n-1].*/

class Solution{
	vector< vector<int> > dp;	
	public:
	int maxdot(int a[],int b[],int n,int m)
	{
	    if(n==0 || m==0){
	        dp[n][m]=0;
	        return dp[n][m];
	    }
	    if(dp[n][m]!=-1){
	        return dp[n][m];
	    }
	    if(n>m){
	        dp[n][m]=max(a[n-1]*b[m-1]+maxdot(a,b,n-1,m-1),maxdot(a,b,n-1,m));
	    }
	    else{
	        dp[n][m]=a[n-1]*b[m-1]+maxdot(a,b,n-1,m-1);
	    }
	    return dp[n][m];
	}
	int maxDotProduct(int n, int m, int a[], int b[]) 
	{
	    dp = vector<vector<int>>(n+1,vector<int>(m+1,-1));
	    return maxdot(a,b,n,m);
	} 
};
