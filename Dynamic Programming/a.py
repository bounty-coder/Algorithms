t=int(input())
while t:
    n=int(input())
    arr=list(map(int,input().split()))
    if n>1 and len(set(arr))==1:
        print(arr[0])
        continue
    dic={}
    win=[-1]
    for i in range(n):
        if arr[i] not in dic:
            dic[arr[i]]=1
            win.append(arr[i])
        elif dic[arr[i]]<=0:
            if arr[i] in win:
                win.remove(arr[i])
        else:
            dic[arr[i]]-=1
            win.remove(arr[i])
    if win[-1]==-1:
        print(-1)
    else:
        print(win[1])
    t-=1