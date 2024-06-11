# https://www.geeksforgeeks.org/problems/maximum-tip-calculator2631/1
'''
In a restaurant, two waiters, A and B, receive n orders per day, earning tips as per arrays arr[i] and brr[i] respectively. If A takes the ith order, the tip is arr[i] rupees; if B takes it, the tip is brr[i] rupees.

To maximize total tips, they must distribute the orders such that:

A can handle at most x orders
B can handle at most y orders
Given that x + y ≥ n, all orders can be managed by either A or B. Return the maximum possible total tip after processing all the orders.
'''

# step1 we create pair the differnce array and index
# step2 Now we find the differnce between the array and kept them with their index
# step 3 now we sort  the array so that we can get the highest differnce consecutively
# step 4 now we travel through that diffence of the array from back so that we can get largest differnce and compare the arr and brr so same index 
# step 5 so which one is high we will add that to the ans

def maxTip(self, n : int, x : int, y : int, arr : List[int], brr : List[int]) -> int:
    diff=[]
    for i in range(n):
        diff.append((abs(arr[i]-brr[i]),i))
    diff.sort(reverse=True)
    total=0
    for i,j in diff:
        if arr[j]>brr[j] and x:
            total+=arr[j]
            x-=1
        else:
            if y:
                total+=brr[j]
                y-=1
            else:
                total+=arr[j]
                x-=1
    return total
