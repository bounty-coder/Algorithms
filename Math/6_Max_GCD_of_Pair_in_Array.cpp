// https://www.geeksforgeeks.org/problems/maximum-gcd-pair3534/1

/* Given an array of integers find the pair in the array with maximum GCD. Find the maximum possible GCD.*/

// Solution 1 - Good
/* Idea is to 
    1) find the maximum element, create an array of high+1 element with 0
    2) Go through each element and find its divisors, and mark each array[divisor]+1
    3) start from last element of array, and find if any index is greater than 1. That will be the biggest GCD*/
vector<int> divisorCount;
void AllDivisors(int n){
    int i=1;
    while(i*i<=n){
        if(n%i==0){
            divisorCount[i]++;
            if(n/i!=i){
                divisorCount[n/i]++;
            }
        }
        i++;
    }
}
int MaxGcd(int n, int a[]) { 
    if(n<=0) return 0;
    int m = 0;
    for(int i=0;i<n;i++){
        if(m<a[i]) m=a[i];
    }
    divisorCount = vector<int>(m+1,0);
    for(int i=0;i<n;i++){
        AllDivisors(a[i]);
    }
    for(int i=m;i>0;i--){
        if(divisorCount[i]>1){
            return i;
        }
    }
}
