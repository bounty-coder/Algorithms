# Given two integers representing the numerator and denominator
#  of a fraction, return the fraction in string format.

# Given numerator = 1, denominator = 2, return "0.5"
# Given numerator = 2, denominator = 1, return "2"
# Given numerator = 2, denominator = 3, return "0.(6)"

# The idea is to first calculate the absolute part before 
# decimal point and then calculate the fractional part.
# To check if the fractional part is repeating, insert the 
# remainder (numerator % denominator) in a map with key as 
# remainder and value as the index position at which this 
# remainder occurs. If at any point of time, the remainder 
# becomes zero, then there doesn’t exist a repeating fraction 
# otherwise if the remainder is already found in the map, 
# then there exists a repeating fraction.

def calculateFraction(num, den) :
     
    # If the numerator is zero, answer is 0
    if (num == 0):
        return "0"
 
    # If any one (out of numerator and denominator)
    # is -ve, sign of resultant answer -ve.
    sign = -1 if (num < 0) ^ (den < 0) else 1
 
    num = abs(num)
    den = abs(den)
 
    # Calculate the absolute part
    # (before decimal point).
    initial = num // den
 
    # Output string to store the answer
    res = ""
 
    # Append sign
    if (sign == -1):
        res += "-"
 
    # Append the initial part
    res += str(initial)
 
    # If completely divisible, return answer.
    if (num % den == 0):
        return res
 
    res += "."
 
    # Initialize Remainder
    rem = num % den
    mp = {}
 
    # Position at which fraction starts
    # repeating if it exists
    index = 0
    repeating = False
    while (rem > 0 and not repeating) :
 
        # If this remainder is already seen,
        # then there exists a repeating fraction.
        if ( rem in mp):
 
            # Index to insert parentheses
            index = mp[rem]
            repeating = True
            break
         
        else:
            mp[rem] = len(res)
 
        rem = rem * 10
 
        # Calculate quotient, append it to result
        # and calculate next remainder
        temp = rem // den
        res += str(temp )
        rem = rem % den
     
    # If repeating fraction exists,
    # insert parentheses.
    if (repeating) :
        res += ")"
        x = res[:index]
        x += "("
        x += res[index:]
        res = x
     
    # Return result.
    return res