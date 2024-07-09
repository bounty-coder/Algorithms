'''
Given an array A of integers and another number K. Find all the unique quadruple from the given array that sums up to K.

Also note that all the quadruples which you return should be internally sorted, ie for any quadruple [q1, q2, q3, q4] the following should follow: q1 <= q2 <= q3 <= q4.

Example 1:

Input:
N = 5, K = 3
A[] = {0,0,2,1,1}
Output: 0 0 1 2 
Explanation: Sum of 0, 0, 1, 2 is equal
to K.
'''

class Solution:
    def fourSum(self, arr, target):
        n=len(arr)
        if n<4:
            return []
        arr.sort()
        ls=[]
        for i in range(n-3):
            if i>0 and arr[i]==arr[i-1]:    #to avoid duplicate 
                continue
            for j in range(i+1,n-2):
                if j>i+1 and arr[j]==arr[j-1]:    #to avoid duplicate
                    continue
                k,l=j+1,n-1
                while k<l:
                    s=arr[i]+arr[j]+arr[k]+arr[l]
                    if s==target:
                        ls.append([arr[i],arr[j],arr[k],arr[l]])
                        k+=1
                        l-=1
                            #to avoid duplicate
                        while k<l and arr[k]==arr[k-1]:
                            k+=1
                        while k<l and arr[l]==arr[l+1]:
                            l-=1
                    elif s<target:
                        k+=1

                    else:
                        l-=1
        return ls
