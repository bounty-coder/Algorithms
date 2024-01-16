//Memoization code


class Solution{
    vector<vector<int>> dp;
  public:
    int func(int curr,int n,int leng,int price[]){
        if(leng<=0 || curr>leng){
            dp[curr][leng]= 0;
            return dp[curr][leng];
        }
        if(dp[curr][leng]!=-1) return dp[curr][leng];
        if(curr<=leng){
            dp[curr][leng]= max(price[curr-1]+func(curr,n,leng-curr,price),func(curr+1,n,leng,price));
        }
        else{
            dp[curr][leng]= func(curr+1,n,leng,price);
        }
        return dp[curr][leng];
    }
    int cutRod(int price[], int n) {
        int leng=n;
        dp = vector<vector<int>>(n+2,vector<int>(leng+2,-1));
        return func(1,n,leng,price);   
    }
};
