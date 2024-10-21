# PLD
# this program asks the user to input a name and age, then adds their input to a dictionary

# check if a name is valid (no special characters)
def check_special_char(given):
    special_characters = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~0123456789"
    for i in given:
        if i in special_characters:
            return False
    return True

names_list = {}

# variable to control the while loop
if_continue = "yes"

# loop to continue asking for user input
while if_continue == "yes":

    # ask the user for name
    name = input("Please enter a name. ")

    # check if name is valid
    while not check_special_char(name):
        name = input("Name must not have special characters! ")
    
    # clear trailing and leading spaces in name
    name = name.strip()
    
    # ask the user for age, then convert string to integer
    try:
        age = int(input("Please enter your age. "))
        if age < 0 or age > 120:
            raise

    except:
        age = int(input("Enter a valid age! (years old) "))

    # add the values to the dictionary
    names_list[name] = age

    # ask the user to continue adding names and ages
    if_continue = input("Continue? yes/no ")
    while if_continue.lower() != "yes" and if_continue.lower() != "no":
        if_continue = input("Continue? ONLY yes/no ")

# find the person with the highest age
highest_age = 0
name_with_highest_age = ""
for n,a in names_list.items():
    if a > highest_age:
        highest_age = a
        name_with_highest_age = n

print(f"The person with the highest age is {name_with_highest_age}, who is {highest_age} years old.")