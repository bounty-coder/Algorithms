# The idea of the solution is to hold all values in 
# Function Call Stack until the stack becomes empty.
# When the stack becomes empty, insert all held items 
# one by one in sorted order. Here sorted order is important.

class Solution:
    def sortedInsert(self,s,element):
        if len(s)==0 or element>s[-1]:
            s.append(element)
            return
        else:
            temp=s.pop()
            self.sortedInsert(s,element)
            s.append(temp)
    
    def sorted(self, s):
        # Code here
        if len(s)!=0:
            temp=s.pop()
            self.sorted(s)
            self.sortedInsert(s,temp)

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.sorted(arr)
        for e in range(len(arr)):
            print(arr.pop(), end=" ")
        print()