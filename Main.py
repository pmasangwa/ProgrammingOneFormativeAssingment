
class Assignment:
    """
    Base class representing a general academic assignment.
    Encapsulates core attributes common to all assignment types.
    """
    def __init__(self, subject, title, score, max_score, due_date, atype):
        self.subject = subject.lower().strip()
        self.title = title.strip()
        self.score = float(score)
        self.max_score = float(max_score)
        self.due_date = due_date.strip()  # Expected format: YYYY-MM-DD
        self.type = atype.lower().strip() # 'homework' or 'exam'

    def display_details(self):
        """
        Calculates percentage and returns a formatted string containing 
        assignment details for display in the terminal.
        """
        percentage = (self.score / self.max_score) * 100 if self.max_score > 0 else 0
        return (f"Subject: {self.subject.title()} | Title: {self.title} | "
                f"Type: {self.type.title()} | Score: {self.score}/{self.max_score} "
                f"({percentage:.2f}%) | Due Date: {self.due_date}")


class Homework(Assignment):
    """
    Subclass representing a homework assignment, extending the base Assignment class 
    using inheritance and the super() constructor.
    """
    def __init__(self, subject, title, score, max_score, due_date):
        super().__init__(subject, title, score, max_score, due_date, "homework")


class Exam(Assignment):
    """
    Subclass representing an examination, extending the base Assignment class 
    using inheritance and the super() constructor.
    """
    def __init__(self, subject, title, score, max_score, due_date):
        super().__init__(subject, title, score, max_score, due_date, "exam")


class GradeTracker:
    """
    Manager class responsible for maintaining the collection of assignments 
    and implementing operational methods (add, list, filter, summarize).
    """
    def __init__(self):
        # Collection to store assignment objects in memory during the session
        self.assignments = []

    def add_assignment(self, assignment):
        """Appends a validated Assignment object to the internal collection list."""
        self.assignments.append(assignment)

    def list_assignments(self):
        """Displays all recorded assignments in a structured format."""
        if not self.assignments:
            print("\n[Notice] No assignments recorded in the system currently.")
            return
        
        print("\n--- Recorded Assignments ---")
        for index, assignment in enumerate(self.assignments, start=1):
            print(f"{index}. {assignment.display_details()}")

    def filter_assignments(self, criteria_type, criteria_value):
        """
        Filters assignments dynamically based on type, subject, or due date month.
        """
        if not self.assignments:
            print("\n[Notice] No assignments available to filter.")
            return

        filtered = []
        criteria_value = criteria_value.lower().strip()

        if criteria_type == "type":
            filtered = [a for a in self.assignments if a.type == criteria_value]
        elif criteria_type == "subject":
            filtered = [a for a in self.assignments if a.subject == criteria_value]
        elif criteria_type == "month":
            # Matches assignments where due_date string starts with YYYY-MM
            filtered = [a for a in self.assignments if a.due_date.startswith(criteria_value)]

        if not filtered:
            print(f"\n[Notice] No assignments found matching {criteria_type}: '{criteria_value}'.")
            return

        print(f"\n--- Filtered Assignments ({criteria_type}: {criteria_value}) ---")
        for index, assignment in enumerate(filtered, start=1):
            print(f"{index}. {assignment.display_details()}")

    def show_summary(self):
        """
        Computes and outputs overall grade percentage, per-subject breakdowns, 
        and extreme scoring entries (highest and lowest).
        """
        if not self.assignments:
            print("\n[Notice] No assignments available to generate a summary report.")
            return

        total_score = sum(a.score for a in self.assignments)
        total_max_score = sum(a.max_score for a in self.assignments)
        overall_percentage = (total_score / total_max_score) * 100 if total_max_score > 0 else 0

        # Aggregating metrics per subject using a dictionary
        subjects = {}
        for a in self.assignments:
            if a.subject not in subjects:
                subjects[a.subject] = {"score": 0.0, "max_score": 0.0, "count": 0}
            subjects[a.subject]["score"] += a.score
            subjects[a.subject]["max_score"] += a.max_score
            subjects[a.subject]["count"] += 1

        # Determining highest and lowest assignments based on percentage ratio
        highest = max(self.assignments, key=lambda x: (x.score / x.max_score if x.max_score > 0 else 0))
        lowest = min(self.assignments, key=lambda x: (x.score / x.max_score if x.max_score > 0 else 0))

        print("\n--- Grade Summary Report ---")
        print(f"Total Assignments Recorded: {len(self.assignments)}")
        print(f"Overall Cumulative Grade Percentage: {overall_percentage:.2f}%")
        
        print("\nPer-Subject Performance Averages:")
        for subj, data in subjects.items():
            subj_pct = (data["score"] / data["max_score"]) * 100 if data["max_score"] > 0 else 0
            print(f"  - {subj.title()}: {subj_pct:.2f}% ({data['count']} assignments tracked)")

        print(f"\nHighest Scoring Assignment: {highest.title} ({highest.subject.title()}) - "
              f"{(highest.score / highest.max_score) * 100:.2f}%")
        print(f"Lowest Scoring Assignment: {lowest.title} ({lowest.subject.title()}) - "
              f"{(lowest.score / lowest.max_score) * 100:.2f}%")


def get_validated_float(prompt, min_val=None, max_val=None):
    """
    Input validation function, this is to ensure user provides a valid floating-point number 
    within specified operational and functional boundaries for the program.
    """
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
    """This is to validates that the entered date string is not empty."""
    while True:
        date_str = input(prompt).strip()
        if date_str:
            return date_str
        print("Error: Date field cannot be left blank. Please use format YYYY-MM-DD.")


def main():
    """
    Main execution loop controlling the command-line interface menu 
    and routing user decisions to appropriate methods.
    """
    tracker = GradeTracker()

    while True:
        print("   STUDENT GRADE TRACKER")
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