//You are given array A consisting of N integers.
/*
  You want to select two sections, each of which consists of adjacent numbers in the array. The two sections must not overlap with other.
  You can calculate the sum of the left setion (First_sum) and the sum of right section(Second_sum) as the two sections are divided into two parts-left and right.

  You have the select a section that has the maximum value of Second_sum-First_sum

  Ex- 2,-1,-2,1,-4,2,-2,3,-1,3,8,2,-5
        |_________|     |_________|
        First_sum=-6    Second_sum=15
        Difference = Second_sum-First_sum = 21
*/

#include <iostream>
#include <vector>
#include <climits>

std::tuple<int, int, int> maxSubArraySum(const std::vector<int>& nums) {
    int maxSum = INT_MIN;
    int currentSum = 0;
    int start = 1, end = 1, tempStart = 1;

    for (int i = 1; i < nums.size(); ++i) {
        currentSum += nums[i];

        if (currentSum > maxSum) {
            maxSum = currentSum;
            start = tempStart;
            end = i;
        }

        if (currentSum < 0) {
            currentSum = 0;
            tempStart = i + 1;
        }
    }

    return {maxSum, start, end};
}

std::tuple<int, int, int> minSubArraySum(const std::vector<int>& nums, int endIndex) {
    int minSum = INT_MAX;
    int currentSum = 0;
    int start = 0, tempStart = 0;

    for (int i = 0; i <= endIndex; ++i) {
        currentSum += nums[i];

        if (currentSum < minSum) {
            minSum = currentSum;
            start = tempStart;
        }

        if (currentSum > 0) {
            currentSum = 0;
            tempStart = i + 1;
        }
    }

    return {minSum, start, endIndex};
}

int main() {
    std::vector<int> nums = {2,-1,-2,1,-4,2,8};
    auto [maxSum, start, end] = maxSubArraySum(nums);

    std::cout << "Maximum sum: " << maxSum << std::endl;
    std::cout << "Starting index: " << start << std::endl;
    std::cout << "Ending index: " << end << std::endl << std::endl;
    
    
    int endIndex = start-1; // Example ending index
    auto [minSum, start1, end1] = minSubArraySum(nums, endIndex);
    std::cout << "Minimum sum: " << minSum << std::endl;
    std::cout << "Starting index: " << start1 << std::endl;
    std::cout << "Ending index: " << end1 << std::endl;
    
    std::cout<<"maxSum-minSum=" << maxSum-minSum;
    return 0;
}
