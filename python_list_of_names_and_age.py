# PLD
# this program asks the user to input a name and age, then adds their input to a dictionary

names_list = {}

# variable to control the while loop
if_continue = "yes"

# loop to continue asking for user input
while if_continue == "yes":

    # ask the user for name
    name = input("Please enter a name. ")

    # ask the user for age, then convert string to integer
    age = int(input("Please enter your age. "))

    # add the values to the dictionary
    names_list[name] = age

    # ask the user to continue adding names and ages
    if_continue = input("Continue? yes/no ")

print(names_list)
