/* Given an integer N, print all the divisors of N in the ascending order. */

// Idea is, 2 divisors multiply and always will make the number n. 
/*  Example: 
    1*40 = 40
    2*20 = 40
    4*10 = 40
    5*8  = 40
So, if we are gettign the first value, at the same time we can get the another one, and also the biggest number will be i*i=n;
      */
void print_divisors(int n) {
    vector<int> divisor;
    vector<int> div2;
    for(int i=1;i*i<=n;i++){
        if(n%i==0){
            divisor.push_back(i);
            if(n/i!=i){
                div2.push_back(n/i);
            }
        }
    }
    for(auto i:divisor){
        cout<<i<<" ";
    }
    for(int i=div2.size()-1;i>=0;i--){
        cout<<div2[i]<<" ";
    }
    return;
}
