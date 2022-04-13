# First negative integer in every window of size k 
# Given an array A[] of size N and a positive integer K,
#  find the first negative integer for each 
# and every window(contiguous subarray) of size K.

# N = 5
# A[] = {-8, 2, 3, -6, 10}
# K = 2
# Output : -8 0 -6 -6

def printFirstNegativeInteger( A, n, k):
    # code here
    i,j,neg=0,k-1,0
    if k>n:
        return [-1]
    ls=[]
    while j<n:
        #neg index can't be less than i
        if neg<i:
            neg=i
        #first neg tk pahoch rhe
        while neg<j:
            if A[neg]<0:
                break
            neg+=1
        #appending 
        if A[neg]<0:
            ls.append(A[neg])
        else:
            ls.append(0)
        i+=1
        j+=1
    return ls

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        k = int(input())
        
        answer = printFirstNegativeInteger(a, n, k)
        for i in answer:
            print(i,end=" ")
        print()

        T -= 1


if __name__ == "__main__":
    main()