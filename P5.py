"""Write a simple Python program that prompts the user for a 
certain number of cities for the Traveling Salesman problem, 
and displays the total number of possible routes that can be taken,
 Your program should function as shown below. """

import math

cities = int(input("How many cities? "))
routes = math.factorial(cities)

print("For", cities, "cities, there are", routes, "possible routes.")