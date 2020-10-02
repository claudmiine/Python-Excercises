"""Write a Python program that allows the user to enter a 
four-digit binary number and displays the value in base 10.  
Each binary digit should be entered one per line,
starting with the leftmost digit, as shown below. """
"""
n1 = int(input("Enter leftmost digit: "))
n2 = int(input("Enter next digit: "))
n3 = int(input("Enter next digit: "))
n4 = int(input("Enter next digit: "))

if n1 == 1:
    n1 = 8
else: 
    n1 = 0

if n2 == 1:
    n2 = 4
else:
    n2 = 0

if n3 == 1:
    n3 = 2
else:
     n3 = 0

if n4 == 1:
    n4 = 1
else: 
    n4 = 0

total = n1 + n2 + n3 + n4

print("The value is", total)
"""
#1110012 = 1⋅25+1⋅24+1⋅23+0⋅22+0⋅21+1⋅20 = 5710
new_binary_num = list(input('Enter the whole binary number: '))
decimal_num = []

for x in new_binary_num:
    
    decimal_num.append(x)
    print(x)
