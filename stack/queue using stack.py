# Python3 program to implement Queue using
# two stacks with costly deQueue()
 
class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []
 
    # EnQueue item to the queue
    def enQueue(self, x):
        self.s1.append(x)
 
    # DeQueue item from the queue
    def deQueue(self):
 
        # if both the stacks are empty
        if len(self.s1) == 0 and len(self.s2) == 0:
            print("Q is Empty")
            return
 
        # if s2 is empty and s1 has elements
        elif len(self.s2) == 0 and len(self.s1) > 0:
            while len(self.s1):
                temp = self.s1.pop()
                self.s2.append(temp)
            return self.s2.pop()
 
        else:
            return self.s2.pop()
 
    # Driver code
if __name__ == '__main__':
    q = Queue()
    q.enQueue(1)
    q.enQueue(2)
    q.enQueue(3)
 
    print(q.deQueue())
    print(q.deQueue())
    print(q.deQueue())



#     Complexity Analysis: 

# Time Complexity: 
# Push operation: O(1). 
# Same as pop operation in stack.
# Pop operation: O(N). 
# In the worst case we have empty whole of stack 1 into stack 2
# Auxiliary Space: O(N). 
# Use of stack for storing values.