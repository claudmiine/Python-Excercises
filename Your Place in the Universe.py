"""Your Place in the Universe Program: Modified for Units of 
Kilograms. Modify the Your Place in the Universe program for international
 users, so that the user enters their weight in kilograms, and not
 in pounds. 
"""
#initialization
num_atoms_universe = 10e80
weigh_avg_person = 70 #70 kg (154 lbs)
num_atoms_avg_person = 7e27

#program greeting
print("\nHello, this program will determine your place in the universe.")

#prompt for user's weight
weight_lbs = int(input("\nEnter your weight in pounds: "))

#convert lbs to kg
weight_kg = weight_lbs * 2.2

#determine number atoms in person
num_atoms_person = (weight_kg / 70) * num_atoms_avg_person
percent_of_universe = (num_atoms_person / num_atoms_universe) * 100

#display results
print("\nYou contain approximately", format(num_atoms_person, '.2e'), 'atoms\n')
print("Therefore, you comprise", format(percent_of_universe, '.2e'), '% of the universe\n')
