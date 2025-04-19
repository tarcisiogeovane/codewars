def solution(n):
    # if n is negative or zero, return 0
    if n <= 0:
        return 0
    
    # initialize sum of multiples
    sum_multiples = 0
    
    # loop through numbers from 1 to n-1
    for i in range(1, n):
        # check if i is a multiple of 3 or 5
        if i % 3 == 0 or i % 5 == 0:
            sum_multiples += i
    
    return sum_multiples

# get input from the user
try:
    n = int(input("Enter a number: "))  # prompt user for input and convert to integer
    result = solution(n)  # call the solution function with user input
    print(f"The sum of multiples of 3 or 5 below {n} is: {result}")
except ValueError:
    print("Please enter a valid integer.")