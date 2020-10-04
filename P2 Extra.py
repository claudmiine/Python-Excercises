"""Write a Python program that prompts the user for two 
floating-point values and displays the result of the first 
number divided by the second, with exactly six decimal places 
displayed. """

import math 
num1 = int(input("Insert first number: "))
num2 = int(input("Insert second number: "))

formatted_num = "{0:.6f}".format(num1/num2)
print(formatted_num)

