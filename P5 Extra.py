"""P5 	
Write a Python program that allows the user to enter two integer 
values, and displays the results 
when each of the following arithmetic operators are applied."""

import math

num1 = int(input("Please insert a number: "))
num2 = int(input("Please insert a second number: "))

print("{:.2f}".format(num1 + num2))
print("{:.2f}".format(num1 - num2))
print("{:,.2f}".format(num1 * num2))
print("{:,.2f}".format(num1 / num2))
print("{:.2f}".format(num1 // num2))
print("{:.2f}".format(num1 % num2))
print("{:,.0f}".format(num1 ** num2))
