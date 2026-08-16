# A function to make sure the user types a real number that are required to prevent errors when running the program. 
# If they type words or a number that is too high or low, it asks them to try again.
def get_validated_float(prompt, min_val=None, max_val=None):
    # Looping is done forever until they type a good or valid number
    while True:
        try:
            # Get the input and try to turn it into a decimal number
            user_input = input(prompt)
            value = float(user_input)
            
            # Branch 1: Check if the number is too small
            # (Checking if min_val != None just makes sure a minimum was actually set)
            if min_val != None and value < min_val:
                print("Error: The number needs to be at least " + str(min_val) + ".")
                # The continue keyword skips the rest of the loop and starts over at the top
                continue
                
            # Branch 2: Check if the number is too big
            if max_val != None and value > max_val:
                print("Error: The score can't be bigger than the max score (" + str(max_val) + ").")
                continue
                
            # If the number passes all the checks, give it back to the program
            return value
            
        # Branch 3: This catches the crash if float() fails (like if they typed "hello")
        except ValueError:
            print("Error: That is not a valid number. Please try again.")

# A function to make sure the user types something for the date
# so they don't just hit enter and leave it empty.
def get_validated_date(prompt):
    # Also, looping is done until they type something valid
    while True:
        # .strip() removes any empty spaces they accidentally typed at the start or end
        date_str = input(prompt).strip()
        
        # Branch 1: Check if the string actually has letters or numbers in it
        if len(date_str) > 0:
            return date_str
            
        # Branch 2: If the length is 0, it means they just pressed enter
        else:
            print("Error: You can't leave this blank. Please type a date (YYYY-MM-DD).")