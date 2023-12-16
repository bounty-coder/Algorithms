// Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
// You may assume that each input would have exactly one solution, and you may not use the same element twice.
// You can return the answer in any order.

//O(n) approach by using hashing

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int,int> m;
        int i=0;
        for(auto it:nums){
            if(m.find(target-it)!=m.end() && (m[target-it]!=i) ){
                return {m[target-it],i};
            }
            m[it]=i;
            i++;
        }
        return {};
    }
};
