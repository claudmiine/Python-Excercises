"""
Write a Python program that allows the user to 
enter any integer base and integer exponent, and displays the 
value of the base raised to that exponent. 
"""

def case_power():
    num = int(input("What case? "))
    power = int(input("What power of case? "))
    answer = num ** power
    print (answer)

case_power()