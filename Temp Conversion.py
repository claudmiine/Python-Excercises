"""Temperature Conversion Program: Modified for Conversion of Celsius to 
Fahrenheit.
Modify the Temperature Conversion program to convert from Celsius to 
Fahrenheit instead.  The formula for the conversion is f = (c * 9/5) + 32. """

#greeting
print("This prgram will convert a temp. entered in Celsius to the equivalent degrees in Fahrenheit")

#get temp. in Celcius
temp_celsius = float(input("Enter a temp. in Celsius degree: "))

#convert temp. to Fahrenheit
temp_fahrenheit = (temp_celsius * 9/5) + 32

#display results
print(temp_celsius, "degrees Celsius equals", format(temp_fahrenheit, ".1f"), "degrees Fahrenheit.")