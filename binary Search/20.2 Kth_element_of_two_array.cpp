// Given two sorted arrays arr1 and arr2 and an element k. The task is to find the element that would be at the kth position of the combined sorted array.

// Input: k = 5, arr1[] = [2, 3, 6, 7, 9], arr2[] = [1, 4, 8, 10]
// Output: 6
// Explanation: The final combined sorted array would be - 1, 2, 3, 4, 6, 7, 8, 9, 10. The 5th element of this array is 6.

/*
Initialize Boundaries: Set the lower and upper bounds for binary search on arr1 as low = max(0, k - n2) and high = min(k, n1) where n1 and n2 are the sizes of arr1 and arr2.

Binary Search:

Calculate the partition point for arr1 as i and for arr2 as j = k - i.
Check if the current partition is valid by comparing the elements around the partition points.
Adjust the binary search boundaries based on the comparisons.
Determine the Kth Element:

Once the correct partition is found, the kth element will be the maximum of the left partitions.
*/

int kthElement(int k, vector<int>& arr1, vector<int>& arr2) {
    if(arr1.size()>arr2.size()){
        return kthElement(k,arr2,arr1);
    }
    
    int n1 = arr1.size();
    int n2 = arr2.size();
    
    int low = max(0,k-n2);
    int high= min(n1,k);
    
    while(low<=high){
        int mid1=(low+high)/2;
        int mid2=k-mid1;
        
        int l1 = (mid1==0)?INT_MIN:arr1[mid1-1];
        int l2 = (mid2==0)?INT_MIN:arr2[mid2-1];
        int r1 = (mid1==n1)?INT_MAX:arr1[mid1];
        int r2 = (mid2==n2)?INT_MAX:arr2[mid2];
        
        if(l1<=r2 && l2<=r1){
            return max(l1,l2);
        }
        else if(l1>r2){
            high = mid1-1;
        }
        else{
            low=mid1+1;
        }
    }
    return -1;
}
