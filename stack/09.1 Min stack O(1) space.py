# Design a Data Structure SpecialStack that supports all the
# stack operations like push(), pop(), isEmpty(), isFull() 
# and an additional operation getMin() which should return 
# minimum element from the SpecialStack. All these operations
#  of SpecialStack must be O(1).

# The simplest way you can encode the new min with the 
# previous min is a linear combination of them both, as in,
#  push some "c1 * new_min + c2 * prev_min (where c1 and c2 are some integers).

# below solution is the better explanation

class MinStack:
    stack=[]
    mini=-1
    def __init__(self):
        self.stack=[]
        self.mini=-1

    # @param x, an integer
    def push(self, x):
        if len(self.stack)==0:
            self.mini=x
            self.stack.append(x)
        else:
            if x>=self.mini:
                self.stack.append(x)
            else:
                self.stack.append(2*x-self.mini)
                self.mini=x        
        return self.stack

    # @return nothing
    def pop(self):
        if len(self.stack)==0:
            return -1
        elif len(self.stack)==1:
            self.mini=-1
            self.stack.pop()
        else:
            if self.top()>=self.mini:
                self.stack.pop()
            else:
                self.mini=2*self.mini-self.top()
                self.stack.pop()
       
    # @return an integer
    def top(self):
        if len(self.stack)==0:
            return -1
        return self.stack[-1]

    # @return an integer
    def getMin(self):
        return self.mini


# So we need to find a way to encode the new minimum element 
# with the previous minimum element and then update the minimum
#  element with the new one. After we encode the two mins using
#  a special formula, if later a pop operation comes in which 
# this encoded number is at the top, it means we've to remove 
# the new min from stack and as we stored separately, we can get
#  back the previous min from this encoded number. 

# The simplest way you can encode the new min with the previous
#  min is a linear combination of them both, as in, push some 
# "c1 * new_min + c2 * prev_min (where c1 and c2 are some integers). 

# But there's a small catch. We need to ensure that our encoded
#  number is less than the new min, because we need to know as 
# to when do we have to remove the new min and retrieve the 
# previous one. The best way to know is to see if the current 
# stack top has a value smaller than the new minimum. It should
#  technically be impossible that an element in stack is smaller
#  than the new minimum, because if it was, then our new minimum
#  would've been that element instead