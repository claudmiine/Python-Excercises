"""P3	
Write a Python program that prompts the user for
 two floating-point values and displays the 
 result of the first number divided by the second, with exactly 
 six decimal places displayed in scientific notation. 
"""

import math

num1 = float(input("Insert a float number: "))
num2 = float(input("Insert second float numder: "))

answer = format(num1/num2, '.6e')

print(answer)