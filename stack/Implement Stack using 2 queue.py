# Implementing stack using queue
# push operation
# Step 1- insert into Q1
# Step 2- push remaining elements of Q2 into Q1
# Step 3- Swap Q1 and Q2

# pop operation
# pop from Q2 as all the element in Q2

#Function to push an element into stack using two queues.
def push(x):
    
    # global declaration
    global queue_1
    global queue_2
    
    # code here
    queue_1.append(x)
    while queue_2:
        queue_1.append(queue_2.pop(0))
    queue_1,queue_2=queue_2,queue_1


#Function to pop an element from stack using two queues.     
def pop():
    
    # global declaration
    global queue_1
    global queue_2
    # code here
    if not queue_2:
        return -1
        
    return queue_2.pop(0)

queue_1 = [] # first queue
queue_2 = [] # second queue

a = list(map(int,input().strip().split()))
i = 0
while i<len(a):
    if a[i] == 1:
        push(a[i+1])
        i+=1
    else:
        print(pop(),end=" ")
    i+=1

# clear both the queues
queue_1 = []
queue_2 = []
print()
# } Driver Code Ends