# Example of Recursion Function

# Here is an example code in Python that demonstrates recursion:


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


# This function calculates the factorial of a given number `n` using recursion. The base case is when `n` equals 1, and the function returns 1. The recursive case is when `n` is greater than 1, and the function calls itself with `n-1` as the argument until it reaches the base case.

# Example usage of factorial function
print(factorial(5))  # Output: 120


# This code will output the factorial of 5, which is 5 x 4 x 3 x 2 x 1 = 120.

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


print(factorial(6))
