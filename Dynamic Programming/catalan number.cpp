//Given a number N. The task is to find the Nth catalan number.
//The first few Catalan numbers for N = 0, 1, 2, 3, … are 1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, …

//Catalan number:
// Cn = C0.Cn-1 +C1.Cn-1 + ....... + Cn-1.C0

//TC- O(n^2)  using DP
class Solution
{
    public:
    unsigned long int C[1000]={0};
    int M=1e9+7;
    unsigned long int findCatalan(int n) 
    {
        if(n==0 || n==1){
            C[n]=1;
            return C[n];
        }
        else if(C[n]!=0){
            return C[n];
        }
        
        for(int i=0;i<n;i++){
            C[n]+=(findCatalan(i)*findCatalan(n-1-i));
            C[n]%=M;
        }
        
        return findCatalan(n);
    }
};


/* O(n) soln is also possible but solve the equation `Cn = C0.Cn-1 +C1.Cn-1 + ....... + Cn-1.C0` 
  which will be short to 
  Cn = (2n!) / ((n+1)! * n!)
  Cn = Cn-1 *((4n-2)/(n+1))
*/
