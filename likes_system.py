def likes(names):
    # get the number of names
    n = len(names)
    
    # handle each case based on the number of names
    if n == 0:
        return "no one likes this"
    elif n == 1:
        return f"{names[0]} likes this"
    elif n == 2:
        return f"{names[0]} and {names[1]} like this"
    elif n == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:  # n >= 4
        return f"{names[0]}, {names[1]} and {n-2} others like this"