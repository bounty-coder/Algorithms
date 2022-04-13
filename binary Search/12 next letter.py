

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