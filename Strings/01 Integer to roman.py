# Given an integer A, convert it to a roman numeral, and 
# return a string corresponding to its roman numeral version

# 1 <= A <= 3999
# Input :  A = 5
# Output :  "V"

def intToRoman(A):
    thousand=["","M","MM","MMM"]
    hundred=["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
    tens=["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
    ones=["","I","II","III","IV","V","VI","VII","VIII","IX"]
    return thousand[A//1000]+hundred[(A%1000)//100]+tens[(A%100)//10]+ones[A%10]

A=int(input())
print(intToRoman(A))