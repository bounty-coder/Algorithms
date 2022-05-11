# For an integer N find the number of trailing zeroes in N!.

# N=5, op-1
# N=23 ,op-4

def trailingZeroes( N):
    #code here
    x=5
    ans=0
    while x<=N:
        ans+=(N//x)
        x*=5
    return ans