//Given two positive integer arrays arr and brr, find the number of pairs such that xy > yx (raised to power of) where x is an element from arr and y is an element from brr.

// Input: arr[] = [2, 1, 6], brr[] = [1, 5]
// Output: 3
// Explanation: The pairs which follow xy > yx are: 21 > 12,  25 > 52 and 61 > 16 .

long long countPairs(vector<int> &arr, vector<int> &brr) {
    long long count=0;
    sort(brr.begin(),brr.end());    //Sort the second array
    
    for(auto i:arr){
        if(i<=1)continue;
        else if(i==2){
            count+=upper_bound(brr.begin(),brr.end(),1)-brr.begin();    //Counting all 1's  ( 2^1 > 1^2 )
            count+=brr.end()-lower_bound(brr.begin(),brr.end(),5);        // Counting all number greater than 4
        }
        else{
            count+=brr.end()-lower_bound(brr.begin(),brr.end(),i+1);    // All number greater than i (ex: i<j)
            count+=upper_bound(brr.begin(),brr.end(),1)-                // All 1 (ones)
                   lower_bound(brr.begin(),brr.end(),1);
        }
        if(i==3){
            count+=upper_bound(brr.begin(),brr.end(),2)-                // All 2's (3^2 > 2^3) exception for i<j
                    lower_bound(brr.begin(),brr.end(),2);
        }
    }
    return count;
}
