def is_square(n): # Check if a number is a perfect square
    if n < 0: # If the number is negative, it cannot be a perfect square
        return False
    return int(n**0.5) ** 2 == n # Check if the square of the integer part of the square root of the number is equal to the number itself