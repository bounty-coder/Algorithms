# arr=[ a, b, e, f, j, l, m ]
#Find next letter of f or h -> j
# if target > last letter, then return first letter

def nextGreatestLetter(letters, target):
    res=' '
    start,last=0,len(letters)-1
    if(letters[last]<=target):
        res=letters[start]
        return res
    
    while(start<=last):
        mid= start+ (last-start)//2
        if(letters[mid]==target):
            start=mid+1
        elif(letters[mid]<target):
            start=mid+1
        elif(letters[mid]>target):
            res=letters[mid]
            last=mid-1
    return res;

letters = ["c","f","j"]
target = "a"
print(nextGreatestLetter(letters,target))