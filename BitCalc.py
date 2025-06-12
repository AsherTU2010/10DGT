print("Welcome to the Bit Calculator!")
def userinput(): 
    valid = False
    while not valid: 
        INPUTerror = f"Whoops, that is not a valid input. \nPlease enter one of the above choices."
        try: 
            choice = input("Please choose an input: \n- Text \n- Integer \n- Image (24-Bit)\n")
            if choice.upper() in ["TEXT","T","TXT"]:
                textInput = input(f"You chose 'Text' \nPlease enter your text input: ") 
                print(f"Your text contains {len(str(textInput))*8} bits.")  
                break
            elif choice.upper() in ["INTEGER","I","INT"]:
                intInput = input(f"You chose 'Integer' \nPlease enter your integer input: ") 
                print(f"Your integer contains {len(intInput)*8} bits.")  
                break
            elif choice.upper() in ["IMAGE","P","IMG"]:
                imageWidth = input(f"You chose 'image' \nPlease enter your width and height of your image in px. \nWidth: ") 
                imageHeight = input("Height: ") ; print(f"Your image contains {(float(imageHeight)*float(imageWidth))*24} bits.") 
                break
            elif choice == "":
                print(INPUTerror)
            else: 
                print(INPUTerror)
        except ValueError: print(INPUTerror)
    again = input("Would you like to do another calculation? \n<enter> - yes \nAny other key - no \n") 
    if again == "": 
        userinput() 
    else:
        print("Thanks for using the Bit Calculator!")
userinput() 

