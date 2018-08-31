def square(x):
    """Finds the square of the input.

    Args:
        x (float): The number to be squared.

    Returns:
        x2 (float): The squared number.
    """

    return x**2

def factorial(n):
    """Factorial calculates the factorial of the provide integer

    Args:
        n (int): The value that the factorial will be computed from.

    Returns:
        fact (int): The factorial of n.

    Raises:
        ValueError: If n is not an integer.
    """
    if not isinstance(n,int):
        if int(n) == n:
            n = int(n)
        else:
            raise ValueError("The input to factorial must be an integer.")

    if n <= 0:
        fact = 1
    else:
        fact = n
        for i in range(1,n):
            fact = i*fact

    return fact

def add_all_ints(n):
    """add_all_ints adds up all integers from 1 to n and returns the result

    Args:
        n (int): The value that will be summed to. Must be positive.

    Returns:
        summation (int): The sum of all integers from 1 to n.

    Raises:
        ValueError: If n is not an integer.
    """

    if not isinstance(n,int):
        if int(n) == n:
            n = int(n)
        else:
            raise ValueError("The input to add_all_ints must be a positive integer.")

    if n < 0:
        raise ValueError("The input to add_all_ints must be a positive integer.")
    
    if n == 0:
        summation = 0
    else:
        summation = 0
        for i in range(1,n + 1):
            summation += i
            
    return summation

