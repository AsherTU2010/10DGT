# Ultimate Conversion
# Asher Thompson
# 11/06/2025
# Version 1.0

print("Welcome to the Ultimate Conversion Tool!")
def userinput(): 
    valid = False
    while not valid: 
        INPUTerror = f"Whoops, that is not a valid input. \nPlease enter a metric time, mass, volume (liquid), distance value."
        try: 
            choice = input("Please choose an input: \n- time \n- mass \n- volume (liquid) \n- distance\n")
            if choice.upper() == "TIME":
                startUnit = input("What specific value is your Time? \n Seconds (s) \n Minutes (m) \n Hours (h) \n Days (d) \n Years (y) \n")
                if startUnit.upper() in ["SECONDS", "S"]:
                    value = input(f"What value is your input {choice.title()} ({startUnit.lower()})") 
                elif startUnit.upper()in ["MINUTES", "M"]:
                    value = input(f"What value is your input {choice.title()} ({startUnit.lower()})") 
                elif startUnit.upper() in ["HOURS", "H"]:
                    value = input(f"What value is your input {choice.title()} ({startUnit.lower()})") 
                elif startUnit.upper() in ["DAYS", "D"]:
                    value = input(f"What value is your input {choice.title()} ({startUnit.lower()})") 
                elif startUnit.upper() in ["YEARS", "Y"]:
                    value = input(f"What value is your input {choice.title()} ({startUnit.lower()})? ") 
                else: print(INPUTerror)
                print(value)
            elif choice.upper() == "MASS":
                startUnit = input("What specific value is your Mass? \n Milligrams \n Grams \n Kilograms \n")
                if startUnit.upper() in ["MILLGRAMS", "MG"]:
                    value = input(f"What value is your input {choice.title()} ({startUnit.lower()})") 
                elif startUnit.upper() == "Miuntes":
                    value = input(f"What value is your input {choice.title()} ({startUnit.lower()})") 
                elif startUnit.upper() == "Hours":
                    value = input(f"What value is your input {choice.title()} ({startUnit.lower()})") 
                elif startUnit.upper() == "Days":
                    value = input(f"What value is your input {choice.title()} ({startUnit.lower()})") 
                elif startUnit.upper() == "Years":
                    value = input(f"What value is your input {choice.title()} ({startUnit.lower()})") 
                else: print(INPUTerror)
            elif choice.upper() == "VOLUME":
                startUnit = input("What specific value is your Time? \n Seconds \n Minutes \n Hours \n Days \n Years \n")
                if startUnit.upper() == "Seconds":
                    value = input(f"What value is your input {choice.title()} ({startUnit.lower()})") 
                elif startUnit.upper() == "Miuntes":
                    value = input(f"What value is your input {choice.title()} ({startUnit.lower()})") 
                elif startUnit.upper() == "Hours":
                    value = input(f"What value is your input {choice.title()} ({startUnit.lower()})") 
                elif startUnit.upper() == "Days":
                    value = input(f"What value is your input {choice.title()} ({startUnit.lower()})") 
                elif startUnit.upper() == "Years":
                    value = input(f"What value is your input {choice.title()} ({startUnit.lower()})") 
                else: print(INPUTerror)
            elif choice.upper() == "DISTANCE":
                startUnit = input("What specific value is your Distance? \n Millimetres (mm) \n Centimetres (cm) \n Metres (m) \n Kilometres (km) \n")
                if startUnit.upper() in ["MILLIMETRES", "MM"]:
                    value = input(f"What value is your input {choice.title()} ({startUnit.lower()})") 
                elif startUnit.upper() in ["CENTIMETRES", "CM"]:
                    value = input(f"What value is your input {choice.title()} ({startUnit.lower()})") 
                elif startUnit.upper() in ["METRES", "M"]:
                    value = input(f"What value is your input {choice.title()} ({startUnit.lower()})") 
                elif startUnit.upper() in ["KILOMETRES", "KM"]:
                    value = input(f"What value is your {startUnit.title()}? ") 
                else: print(INPUTerror)
            elif choice.upper() == "EXIT": break
            elif choice == "": print(INPUTerror)
            else: print(INPUTerror)
        except ValueError: print(INPUTerror)
    again = input("Would you like to do another calculation? \n<enter> - yes \nAny other key - no \n") 
    if again == "": userinput() 
    else: print("Thanks for using the Bit Calculator!")
userinput()