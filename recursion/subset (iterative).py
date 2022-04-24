a=[1,2,3,4,5]
b=[[]]
for i in a:
    b+=[j+[i] for j in b]
print(b)