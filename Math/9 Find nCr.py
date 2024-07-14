# Find nCr
'''
nCr = n! / (r! * (n-r)!)
nCr = n*(n-1)*....(n-r+1)/(1*2...r)
'''

n=int(input())
r=int(input())

nr=1
dr=1
r=min(r,n-r)
for i in range(r):
    nr=nr*(n-i)    #find numerator
    dr=dr*(i+1)    #find denominator
    
#pow(x,y,z) z denotes mod
ans= (nr//dr)    # nr * 1/dr
