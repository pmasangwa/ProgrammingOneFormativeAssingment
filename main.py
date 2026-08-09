# Pull in the classes from our assignments.py file
from assignments import GradeTracker, Homework, Exam

# Pull in the helper tools from our validation.py file
from validation import get_validated_float, get_validated_date

def main():
    # The main loop that runs our app! It shows the menu on the screen, 
    # waits for the user to pick an option, and then tells the GradeTracker what to do.
    tracker = GradeTracker()

    while True:
        print("\n   STUDENT GRADE TRACKER")
        print("1) Add homework")
        print("2) Add exam")
        print("3) List assignments")
        print("4) Filter assignments")
        print("5) Show summary")
        print("0) Exit")
        
        choice = input("Select an option (0-5): ").strip()

        if choice == '1':
            print("\n--- Add New Homework ---")
            subject = input("Enter subject name: ").strip()
            title = input("Enter homework title: ").strip()
            max_score = get_validated_float("Enter maximum possible score: ", min_val=0.1)
            score = get_validated_float("Enter achieved score: ", min_val=0.0, max_val=max_score)
            due_date = get_validated_date("Enter due date (YYYY-MM-DD): ")
            
            homework = Homework(subject, title, score, max_score, due_date)
            tracker.add_assignment(homework)
            print("Status: Homework assignment recorded successfully.")

        elif choice == '2':
            print("\n--- Add New Exam ---")
            subject = input("Enter subject name: ").strip()
            title = input("Enter exam title: ").strip()
            max_score = get_validated_float("Enter maximum possible score: ", min_val=0.1)
            score = get_validated_float("Enter achieved score: ", min_val=0.0, max_val=max_score)
            due_date = get_validated_date("Enter due date (YYYY-MM-DD): ")
            
            exam = Exam(subject, title, score, max_score, due_date)
            tracker.add_assignment(exam)
            print("Status: Examination recorded successfully.")

        elif choice == '3':
            tracker.list_assignments()

        elif choice == '4':
            print("\n--- Filter Assignments ---")
            print("Select criteria: 1) Type (homework/exam)  2) Subject  3) Month (YYYY-MM)")
            filter_choice = input("Enter option (1-3): ").strip()
            
            if filter_choice == '1':
                ftype = input("Enter type ('homework' or 'exam'): ").strip()
                tracker.filter_assignments("type", ftype)
            elif filter_choice == '2':
                fsubject = input("Enter subject name: ").strip()
                tracker.filter_assignments("subject", fsubject)
            elif filter_choice == '3':
                fmonth = input("Enter target month (YYYY-MM): ").strip()
                tracker.filter_assignments("month", fmonth)
            else:
                print("Error: Invalid filter selection menu choice.")

        elif choice == '5':
            tracker.show_summary()

        elif choice == '0':
            print("\nTerminating application session. All memory collections cleared. Goodbye.")
            break
        else:
            print("\nError: Invalid menu choice. Please select a valid integer between 0 and 5.")

if __name__ == "__main__":
    main()