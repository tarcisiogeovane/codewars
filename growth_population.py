def nb_year(p0, percent, aug, p): # Function to calculate the number of years required for a population to reach a certain size
    years = 0 # Initialize the number of years
    while p0 < p: # Loop until the population reaches the target size
        p0 += p0 * percent / 100 + aug # Update the population with the growth rate and the annual increase
        years += 1 # Increment the number of years
    return years # Return the number of years required