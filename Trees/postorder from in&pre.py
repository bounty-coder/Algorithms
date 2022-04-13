def search(x,arr,n):
    for i in range(n):
        if arr[i]==x:
            return i
    return -1

def printpostorder(pre,ino,n):
    root=search(pre[0],ino,n)
    if root!=0:
        printpostorder(pre[1:n],ino,root)
    if root!=n-1:
        printpostorder(pre[root+1:n],ino[root+1:n],n-root-1)
    print(pre[0],end=" ")


pre=[1,2,4,5,3,6]
ino=[4,2,5,1,3,6]
n=len(pre)

print("Postorder Traversal:")
printpostorder(pre,ino,n)