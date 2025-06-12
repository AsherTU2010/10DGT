# Fence Cost Calculator
# Asher Thompson
# 28/05/2025
# Version 1.1

# Welcome the user to the calculator
print("Hello user!")
print("Welcome to the Fence Cost Calculator! \n")

def userinput(lowest): # define the function to check the user's input
    valid = False # use a variable to make sure that we can turn off the while loop below

    while not valid: 
        # if an invalid input is put in the program will return an error message
        error = f"Whoops, you have entered an invalid input. \n Please enter a value above 0."

        try:  
            print("Please enter the measurements for the area you want to fence below: ")
            width = float(input("Width: "))
            
            # if the width > 0 then ask user for the fence price, then ask for height, then price, 
            if width > lowest: 
                length = float(input("Length: "))
                if length > lowest:
                    fencePrice = round(float(input("\nWhat price are you purhcasing fencing for? ($/metre) ")),2) 

                    if fencePrice <= lowest:
                        print(error)
                    else:
                         # caculate the perimeter of the fenced area and give a price for the total amount for fence needed
                        peri = 2 * (width + length) 
                        totalCost = peri * fencePrice
                        print (f"\nThe perimeter of your area is {peri} metres. \nAt a price of ${fencePrice}/metre, the total cost of your fencing project will be ${totalCost}") 

                        # ask the user if they want to continue cacualting
                        userAnswer = input("\nIf you would like to do another caculation press <enter>, otherwise peress any other key ")
                        if userAnswer == "":
                            valid = False
                        else:
                            print("Thanks for using the caculator")
                            valid = True
                else:
                    print (error)
            else:
                 print(error)
                 
        except ValueError: # if the user input is not a number (string/boolean) then print an error message
            print(error)


# call the function with the parameter lowest as 0
userinput(lowest = 0)



        

        