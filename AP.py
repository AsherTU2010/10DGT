# Area and Perimeter
# Asher Thompson
# 21/05/2025
# Version 1.0

'''
Width = int(input("Please enter a measurement for the width of a rectangle. ")) # Ask user for the width
Height = int(input("Now, a measurement for the height please. ")) # Ask user for the height


print (Height) # Print inputs to check input is stored correctly
print (Width)

Area = (Width * Height) # Calculate the area 
Peri_ = 2 * (Width + Height) # Calculate the perimeter (Peri_)

print (f"The area of your rectangle is {Area}. \nThe perimeter of your rectangle is {Peri_}") # Output the area and perimeter
'''

# Verision 1.1
def numcheck(lowest): # define the function to check the user's input
    valid = False # use a variable to make sure that we can turn off the while loop below

    while not valid: 
        # if an invalid input is put in the program will return an error message
        error = f"Whoops, you have entered an invalid input. Please enter a valid integer more than 0."

        try:  
            width = float(input("Please enter a measurement for the width of a rectangle. ")) # Ask user for the width

            if width > lowest: # if the width is > 0 then continue with the program: ask the user for the height
                height = float(input("Now, a measurement for the height please. ")) # Ask user for the height

                if height > lowest: # if the height is > 0 then end the program

                    valid = True

                else: # if the height isnt < 0 then print an error message
                    print (error)

            else: # if the width isnt < 0 then print an error message
                print (error)

        except ValueError: # if the user input is not a number (string/boolean) then print an error message
            print(error)
    return width, height

width, height = numcheck(lowest = 0)  # run the fucntion with the parameter 'lowest' being the lowest possible measurement for the user to input
# running the function also stores the values in the function in the variable width, height
# with the help of google I learnt how to do this above...it wasnt working when I only had numcheck(lowest = 0) then continued with below

area = (width * height) # Calculate the area 
peri = 2 * (width + height) # Calculate the perimeter (peri)
print (f"The area of your rectangle is {area}.") # print the caculated area from the user's inputs
print (f"The perimeter of your rectangle is {peri}") # print the caculated perimeter from the user's inputs