# Pull in the classes from our assignments.py file
from assignments import GradeTracker, Homework, Exam

# Pull in the helper tools from our validation.py file
from validation import get_validated_float, get_validated_date

# My Student Grade Tracker App
# Create an empty list to hold all the assignments and exams
my_grades = []

print("Welcome to the Student Grade Tracker!")

# Main loop to keep the program running
while True:
    print("\n  STUDENT GRADE TRACKER")
    print("1) Add homework")
    print("2) Add exam")
    print("3) List assignments")
    print("4) Filter assignments")
    print("5) Show summary")
    print("0) Exit")
    
    choice = input("Select an option (0-5): ")

    if choice == '1':
        print("\n--- Add New Homework ---")
        subject = input("Enter subject name: ")
        title = input("Enter homework title: ")
        # Using float() to turn the input into a number
        max_score = float(input("Enter maximum possible score: "))
        score = float(input("Enter achieved score: "))
        due_date = input("Enter due date (YYYY-MM-DD): ")
        
        # Save it as a dictionary
        homework = {
            "type": "homework",
            "subject": subject,
            "title": title,
            "max_score": max_score,
            "score": score,
            "due_date": due_date
        }
        my_grades.append(homework)
        print("Homework added!")

    elif choice == '2':
        print("\n--- Add New Exam ---")
        # I copied this from the homework part above
        subject = input("Enter subject name: ")
        title = input("Enter exam title: ")
        max_score = float(input("Enter maximum possible score: "))
        score = float(input("Enter achieved score: "))
        due_date = input("Enter due date (YYYY-MM-DD): ")
        
        exam = {
            "type": "exam",
            "subject": subject,
            "title": title,
            "max_score": max_score,
            "score": score,
            "due_date": due_date
        }
        my_grades.append(exam)
        print("Exam added!")

    elif choice == '3':
        print("\n--- All Assignments ---")
        if len(my_grades) == 0:
            print("Nothing here yet!")
        else:
            # loop through the list and print each one
            for item in my_grades:
                print(item["title"] + " (" + item["subject"] + ") - Score: " + str(item["score"]) + "/" + str(item["max_score"]))

    elif choice == '4':
        print("\n--- Filter Assignments ---")
        print("1) Type  2) Subject  3) Month")
        filter_choice = input("Enter option (1-3): ")
        
        if filter_choice == '1':
            ftype = input("Enter type (homework or exam): ")
            for item in my_grades:
                if item["type"] == ftype:
                    print(item["title"] + " - " + str(item["score"]))
                    
        elif filter_choice == '2':
            fsubject = input("Enter subject: ")
            for item in my_grades:
                if item["subject"] == fsubject:
                    print(item["title"] + " - " + str(item["score"]))
                    
        elif filter_choice == '3':
            fmonth = input("Enter month (YYYY-MM): ")
            for item in my_grades:
                # check if the date starts with the month they typed
                if item["due_date"].startswith(fmonth):
                    print(item["title"] + " - " + item["due_date"])
        else:
            print("Wrong filter choice.")

    elif choice == '5':
        print("\n--- Grade Summary ---")
        total_score = 0
        total_max = 0
        
        for item in my_grades:
            total_score = total_score + item["score"]
            total_max = total_max + item["max_score"]
            
        if total_max > 0:
            percentage = (total_score / total_max) * 100
            print("Total Points: " + str(total_score) + "/" + str(total_max))
            print("Overall Grade: " + str(percentage) + "%")
        else:
            print("No grades entered yet to summarize.")

    elif choice == '0':
        print("Bye!")
        break # stops the while loop
        
    else:
        print("Invalid choice, please type a number between 0 and 5.")