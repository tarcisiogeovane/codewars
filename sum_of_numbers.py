def get_sum(a,b): # This function returns the sum of all numbers between a and b (inclusive).
    if a == b: # If a and b are equal, return a (or b, since they are the same)
        return a # or b
    else: # If a and b are not equal, calculate the sum of all numbers between them.
        if a > b: # If a is greater than b, swap them to ensure a is less than b.
            a, b = b, a # Swap a and b
        return sum(range(a, b + 1)) # Calculate the sum of all numbers from a to b (inclusive) using the range function and the sum function.
