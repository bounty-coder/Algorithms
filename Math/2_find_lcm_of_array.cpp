/* find lcm of array
  To find lcm of array, start from lcm of first two numbers and go till the end of array
  lcm(a,b,c)=lcm(lcm(a,b),c)
*/

#include <iostream>

int GCD(int a,int b){
    if(b==0) return a;
    GCD(b,a%b);
}
int LCM(int a,int b,int gcd){
    return a*b/gcd;
}
int lcmOfArray(int N , int A[]) {
    if(N<=0)return 0;
    int hcf=A[0];
    int lcm=A[0];
    for(int i=1;i<N;i++){
        hcf = GCD(lcm,A[i]);
        lcm = LCM(lcm,A[i],hcf);
    }
    return lcm;
}
