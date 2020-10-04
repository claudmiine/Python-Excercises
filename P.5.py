# Number of Years to Solve the Traveling Salesman Problem
#
# This program determines the estimated number of years it would take to
# solve the Traveling Salesman problem for a given number of cities, with
# the assumption that one million routes be second can be computed.

import math

# Determine number of seconds per year
secs_in_year = 60 * 60 * 24 * 365
# Get number of cities
num_cities = int(input('Enter the number of cities: '))
# Calculate time
time_to_solve = (math.factorial(num_cities) / 10**6) / secs_in_year
# Output Result
print('The time it would take to solve the Traveling Salesman problem')
print('of', num_cities, 'cities is approximately', time_to_solve, 'years')