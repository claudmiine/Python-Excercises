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
def convert_binary_to_decimal():

    new_binary_num = list(input('Enter the whole binary number: '))
    decimal_num = []

    for x in new_binary_num:
        decimal_num.append(x)

    decimal_num = decimal_num[::-1] #reverse the list 
    # The reversed list is needed for the for loop.
    # The first element is multiply by power to 2 "2" and added 
    decimal = 0 #declare the decimal number
    power = 0   #declare power variable
    for number in decimal_num: 
        if number == '1':  
            decimal += 2**power  # add the number to decimal
            #print(f'The sum decimal is {decimal} afer power used: {power}')
            power += 1 #increase power by 1    
            
    return decimal

new_number = convert_binary_to_decimal()

print(f"Here is the converted number: {new_number}")