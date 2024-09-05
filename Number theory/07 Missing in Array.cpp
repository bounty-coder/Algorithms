// Given an array arr of size n−1 that contains distinct integers in the range of 1 to n (inclusive),
// find the missing element. 
// The array is a permutation of size n with one element missing. Return the missing element.

// Input: n = 5, arr[] = [1,2,3,5]
// Output: 4
// Explanation : All the numbers from 1 to 5 are present except 4.

int missingNumber(int n, vector<int>& arr) {
    long long int totalsum = (n*(n+1))/2;
    //accumulate is used for sum of a vector
    long long int s = accumulate(arr.begin(), arr.end(),0);
    return totalsum-s;
}
