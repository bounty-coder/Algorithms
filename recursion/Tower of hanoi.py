#tower of hanoi
# step1: n-1 disks from (start rod) to helper rod
# step2: 1 disk from (start rod) to end rod
# step3: n-1 disks from helper rod to end rod

    
class Solution:
    count=0
        
    def toh(self, N, fromm, to, aux):
        # Your code here
        if N==0:
            return
        self.count+=1
        # step 1
        self.toh(N-1,fromm,aux,to)
        # step 2
        print("move disk "+str(N)+" from rod "+str(fromm)+" to rod "+str(to))
        # step 3
        self.toh(N-1,aux,to,fromm)
        return self.count

import math
def main():

    T = int(input())

    while(T > 0):
        N = int(input())
        ob = Solution()
        print(ob.toh(N, 1, 3, 2))
        T -= 1
if __name__ == "__main__":
    main()
