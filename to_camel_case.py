def to_camel_case(text): # Convert a string to camel case
    if not text: # Check if the string is empty
        return "" # Return an empty string if it is
    
    delimiters = ["-", "_"] # List of delimiters to split the string
    for delimiter in delimiters: # Iterate through each delimiter
        if delimiter in text: # Check if the delimiter is in the string
            text = text.replace(delimiter, " ") # Replace the delimiter with a space
    
    words = text.split() # Split the string into words
    
    camel_case_text = words[0] # Initialize the camel case string with the first word in lowercase
    
    for word in words[1:]: # Iterate through the rest of the words
        camel_case_text += word.capitalize() # Capitalize the first letter of each word and append it to the result
    
    return camel_case_text # Return the camel case string
    