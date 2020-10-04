"""Restaurant Tab Calculation Program: User-Entered Tax Rate 
Modify the Restaurant Tab Calculation program so that, instead of
 the restaurant tax being hard coded in the program, the tax rate is
  entered by the user. """
import math 

tax_rate = int(input("Enter restaurant tax rate: "))
amount_of_gift = int(input("Enter the amonut of gift certificate: "))

print("Enter ordered items for person 1")
print()

num = int(input("How many items did you order? "))

amount =  0.0

for x in range(num):
    item = float(input("Enter the price for each item: "))
    amount+=item


print("Enter ordered items for person 2")
print()

num2 = int(input("How many items did you order? "))

for x in range(num2):
    item = float(input("Enter the price for each item: "))
    amount+=item


tax_amount = "{:.2f}".format((tax_rate)/100 * amount)
change = amount_of_gift - amount

print(f"This is the total: {amount} amount.")
print(f"Restaurant tax is {tax_amount}.")
print(f"You have still {change} unused amount of gift certificate.")
