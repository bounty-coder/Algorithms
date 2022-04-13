# The idea is to use recursive calls. We first remove 
# all items one by one, uptil the mid element then we recur.
#  After recursive calls,
#  we push all items back except the middle item.  
class Solution:
    def solve(self,s,mid):
        if mid==1:
            s.pop()
            return
        temp=s[-1]
        s.pop()
        self.solve(s,mid-1)
        s.append(temp)
        return
    
    #Function to delete middle element of a stack.
    def deleteMid(self, s, sizeOfStack):
        # code here
        if len(s)==0:
            return
        mid=sizeOfStack//2 +1
        self.solve(s,mid)
        return

def main():
    t=int(input())
    while(t>0):
        sizeOfStack=int(input())
        myStack=[int(x) for x in input().strip().split()]
        ob = Solution()
        ob.deleteMid(myStack,sizeOfStack)
        while(len(myStack)>0):
            print(myStack[-1],end=" ")
            myStack.pop()
        print()
        t-=1


if __name__=="__main__":
    main()
