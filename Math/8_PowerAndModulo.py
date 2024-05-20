# Implement pow(x, n) % M.

# TC - O(log(n))

def power(x, n, M):
    result = 1
    while n > 0:
        if n % 2 == 1:
            result = (result * x) % M
        x = (x * x) % M
        n = n // 2
    return result


''' 
1. Initialize with result 1, because n^0 is 1
2. Loop until n is 0
3. If n is odd, multiply result by x  ( x^5 = x^4 * x)
4. Square x and half n  ( x^2n = (x^2)n )
5. Take modulo at each step. ( x^n mod m) 
'''
