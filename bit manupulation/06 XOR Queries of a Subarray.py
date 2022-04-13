# You are given an array arr of positive integers. You are also 
# given the array queries where queries[i] = [lefti, righti].

# For each query i compute the XOR of elements from lefti to 
# righti (that is, arr[lefti] XOR arr[lefti + 1] XOR ... XOR arr[righti] ).

# Return an array answer where answer[i] is the answer to the ith query.

# Input: arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]
# Output: [2,7,14,8] 

def xorQueries(arr, queries) :
    prefix=[arr[0]]
    for i in range(1,len(arr)):
        prefix.append(prefix[i-1]^arr[i])
    ans=[]
    for i,j in queries:
        if i==0:
            ans.append(prefix[j])
        else:
            ans.append(prefix[i-1]^prefix[j])
    return ans

arr = [1,3,4,8]
queries = [[0,1],[1,2],[0,3],[3,3]]
print(xorQueries(arr,queries))