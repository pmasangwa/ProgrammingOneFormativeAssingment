def get_validated_float(prompt, min_val=None, max_val=None):
    # A helper tool that makes sure the user types a real number. 
    # If they type words or a number that's too high or low, it asks them to try again.
    while True:
        try:
            value = float(input(prompt))
            if min_val is not None and value < min_val:
                print(f"Error: Value must be equal to or greater than {min_val}.")
                continue
            if max_val is not None and value > max_val:
                print(f"Error: Achieved score cannot exceed maximum score ({max_val}).")
                continue
            return value
        except ValueError:
            print("Error: Invalid numeric format. Please enter a valid number.")

def get_validated_date(prompt):
    # A helper tool that makes sure the user actually types a date 
    # and doesn't just hit 'enter' leaving it completely blank.
    while True:
        date_str = input(prompt).strip()
        if date_str:
            return date_str
        print("Error: Date field cannot be left blank. Please use format YYYY-MM-DD.")