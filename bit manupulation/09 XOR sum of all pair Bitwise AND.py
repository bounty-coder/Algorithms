# The XOR sum of a list is the bitwise XOR of all its elements.
# If the list only contains one element, then its XOR sum will be equal to this element.
# Input: arr1 = [1,2,3], arr2 = [6,5]
# Output: 0

def getXORSum(arr1, arr2):
    m=len(arr1)
    n=len(arr2)

    #approach 1 bruteforce
    # ls=[]
    # for i in range(m):
    #     for j in range(n):
    #         ls.append(arr1[i]&arr2[j])
    # ans=ls[0]
    # for i in range(1,len(ls)):
    #     ans=ans^ls[i]
    # return ans

    #approach 2 
    #(a^b)&(c^d)=(a&c)^(a&d)^(b^c)&(b^d)
    x=arr1[0]
    for i in range(1,m):
        x=x^arr1[i]
    y=arr2[0]
    for j in range(1,n):
        y=y^arr2[j]
    return x&y

arr1 = [1,2,3]
arr2 = [6,5]

print(getXORSum(arr1,arr2))