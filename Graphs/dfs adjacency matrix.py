adj_mat = [
    #0 1 2 3 4 5
    [0,1,0,0,1,0],  #0
    [1,0,1,1,0,0],  #1
    [0,1,0,0,0,0],  #2
    [0,1,0,0,0,1],  #3
    [1,0,0,0,0,1],  #4
    [0,0,0,1,1,0]   #5
]

visited = [0]*6
stack=[]
ans=[]

def stack_display():
    for val in stack:
        print(val,end='|')
    print()

def dfs(n):
    if visited[n]!=0:
        return
    else:
        visited[n]=1
        stack.append(n)
        stack_display()
        num=0
        for i in adj_mat[n]:
            if i!=0:
                dfs(i)
            num+=1
        print(n)
        ans.append(n)
        stack.pop()
        stack_display()


src_node = int(input())
dfs(src_node)
print(ans)