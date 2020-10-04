"""P4. Write a Python program that prompts the user to enter an 
upper or lower case letter and displays the corresponding Unicode 
encoding."""

letter = input("Enter a lower or upper case letter: ")
print("The Unicode value for the letter ", letter, "is", ord(letter))