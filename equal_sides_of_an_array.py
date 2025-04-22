def find_even_index(arr): # This function finds the index of the first element in the array where the sum of the elements to its left is equal to the sum of the elements to its right.
    for i in range(len(arr)):# Iterate through the array
        if sum(arr[:i]) == sum(arr[i+1:]): # Check if the sum of the elements to the left is equal to the sum of the elements to the right
            return i # If they are equal, return the index
    return -1 # If no such index is found, return -1