N=int(input("Enter number:"))
count=0
while N>0:
    N=N&(N-1)
    count+=1
print("Number of set bits are ",count)


# Soln 2
# while (N) {
#     cnt += (N & 1);
#     N >>= 1;
# }

#both O(logn)