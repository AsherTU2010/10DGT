# Demonstrate how to create functions, thus making the coode recyclable
# Author: Asher Thompson
# Date: 14/05/2025
# Version 3.0


# While loops
# Version 1.0
'''
keep_going = "" # The variable contains an empty string
# == is used to check if the variable meets the condition
while keep_going == "":

    like_coffee = input("Do you like coffee? ")

    if like_coffee == "yes"
        print("That is great. I like coffee too!")
        keep_going = "end" # This will end the loop
    if like_coffee == "no":
        print("Fair enough.") # This will end the loop
        keep_going = "end" '''

# Version 2.0 Making the code more pythonic`
''' keep_going = ""
while keep_going == "":
    like_coffee = input("Do you like coffee? ").lower() # .lower() makes the input lowercase

    if like_coffee == "yes" or like_coffee == "y":
        print("That is great. I like coffee too!")
        keep_going = "end"  
    elif like_coffee == "no":
        print("Fair enough.")

        like_tea = input("Do you like tea? ").upper()

        if like_tea == "YES" or like_tea == "Y":
            print("Good for you. Give coffee another try :)")
            keep_going = "end"
        elif like_tea == "NO" or like_tea == "N":
            print("I am sorry. That is all I have for now.")
            keep_going = "end"
        else:
            print("I don't understand. Please answer with either 'yes' or 'no'.")
    else:
        print("I don't understand. Please answer with either 'yes' or 'no'.")

    keep_going = "Press <enter> to continue or any other key to quit."
'''

# Version 3.0 
# Create a function that i can use over and over again
# Makes my code recyclable
# The program will ask a person for a numebr and do something with it
# Loop the program until a valid number gets entered
'''
def intcheck(): # def creates a function
    valid = False
    while not valid: 
        error = "Whoops, you have entered the wrong number. Please enter a valid integer between 1 and 10"

        try:  
            response = int(input("Enter an integer between 1 and 10. "))

            if response >= 1 and response <= 10:
                print(response)
                valid = True
            else:
                print(error)

        except ValueError:
            print(error)

intcheck() # To call the function
'''
# Version 3.1
# Create a function that i can use over and over again
# Makes my code recyclable
# The program will ask a person for a numebr and do something with it
# Loop the program until a valid number gets entered

def intcheck(question, low, high): # def creates a function
    valid = False
    while not valid: 
        error = f"Whoops, you have entered the wrong number. Please enter a valid integer between {low} and {high}"

        try:  
            response = int(input(f"Enter an integer between  {low} and {high}. "))

            if low <= response <= high:
                print(f"You have entered {response}")
                valid = True
            else:
                print(error)

        except ValueError:
            print(error)
    return response 

num1 = intcheck("Enter a number between 1 and 10", 1, 10) # To call the function
num2 = intcheck("Enter a number between 1 and 10", 15, 20)

# Adding the two numbers together
sum_number = num1 + num2

# multiplying the two numbers together
product_number = num1 * num2

print(f"Your two numbers added together is {sum_number}.\n")
print(f"Your two numbers multiplied together is {product_number}.")