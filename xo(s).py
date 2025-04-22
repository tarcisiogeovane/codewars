def xo(s): # Check if the number of 'x' and 'o' in the string are equal
    s = s.lower() # Convert the string to lowercase to make the check case-insensitive
    return s.count('x') == s.count('o') # Count the number of 'x' and 'o' in the string and check if they are equal