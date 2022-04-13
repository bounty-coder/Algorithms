# Josephus
# Given the total number of persons n and a number k which 
# indicates that k-1 persons are skipped and kth person is killed in
#  circle. The task is to choose the place in the initial circle so 
# that you are the last one remaining and so survive.


def solve(arr,index,k):
    if len(arr)==1:
        return
    # index of first person who will die
    index=(index+k)%len(arr)
    arr.pop(index)
    solve(arr,index,k)
    
def safePos(n, k):
    arr=[i for i in range(1,n+1)]
    index=0
    solve(arr,index,k-1)
    return arr[0]

n,k=map(int,input().split())
print(safePos(n,k))


#non recursive solution

# def safePos(self, n, k):
#     arr = [i for i in range(1,n+1)]
#     count = 0
#     while len(arr) > 1:
#         count = (count + k-1)%len(arr)
#         arr.pop(count)
#     return arr[0]