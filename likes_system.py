def likes(names): # Function to generate a message based on the number of names
    n = len(names) # Get the number of names
    
    if n == 0: 
        return "no one likes this" # If there are no names, return "no one likes this"
    elif n == 1:
        return f"{names[0]} likes this" # If there is one name, return "{name} likes this"
    elif n == 2:
        return f"{names[0]} and {names[1]} like this" # If there are two names, return "{name1} and {name2} like this"
    elif n == 3: 
        return f"{names[0]}, {names[1]} and {names[2]} like this" # If there are three names, return "{name1}, {name2} and {name3} like this"
    else:
        return f"{names[0]}, {names[1]} and {n-2} others like this" # If there are more than three names, return "{name1}, {name2} and {n-2} others like this"