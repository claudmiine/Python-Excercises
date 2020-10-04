"""Write a Python program that prompts the user for two 
integer values and displays the result of the first number divided 
by the second, with exactly two decimal places displayed."""

num1 = int(input("Please insert first number: "))
num2 = int(input("Please insert second number: "))

answer = "{0:.2f}".format(num1/num2)
print(answer)