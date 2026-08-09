class Assignment:
    # This is the main blueprint for any school task. 
    # It stores basic details like the subject, name, score, and when it is due.
    def __init__(self, subject, title, score, max_score, due_date, atype):
        # Sets up a new assignment with all its starting details.
        self.subject = subject.lower().strip()
        self.title = title.strip()
        self.score = float(score)
        self.max_score = float(max_score)
        self.due_date = due_date.strip() 
        self.type = atype.lower().strip() 

    def display_details(self):
        # Turns the assignment's details and grade percentage into a neat sentence 
        # so we can easily print it out for the user to read.
        percentage = (self.score / self.max_score) * 100 if self.max_score > 0 else 0
        return (f"Subject: {self.subject.title()} | Title: {self.title} | "
                f"Type: {self.type.title()} | Score: {self.score}/{self.max_score} "
                f"({percentage:.2f}%) | Due Date: {self.due_date}")


class Homework(Assignment):
    # A specific type of assignment just for homework. 
    # It uses the main Assignment blueprint above to set itself up.
    def __init__(self, subject, title, score, max_score, due_date):
        super().__init__(subject, title, score, max_score, due_date, "homework")


class Exam(Assignment):
    # A specific type of assignment just for exams. 
    # Like homework, it also borrows the main Assignment blueprint.
    def __init__(self, subject, title, score, max_score, due_date):
        super().__init__(subject, title, score, max_score, due_date, "exam")


class GradeTracker:
    # This is the main brain of our app! It holds all our assignments in a list 
    # and lets us do things like view, filter, or summarize them.
    def __init__(self):
        # Creates an empty digital folder (a list) to hold all our assignments.
        self.assignments = []

    def add_assignment(self, assignment):
        # Takes a new assignment and drops it into our digital folder.
        self.assignments.append(assignment)

    def list_assignments(self):
        # Looks through our folder and prints out every assignment we've saved so far. 
        # If the folder is empty, it tells the user.
        if not self.assignments:
            print("\n[Notice] No assignments recorded in the system currently.")
            return
        
        print("\n--- Recorded Assignments ---")
        for index, assignment in enumerate(self.assignments, start=1):
            print(f"{index}. {assignment.display_details()}")

    def filter_assignments(self, criteria_type, criteria_value):
        # Searches our folder for specific assignments—like all 'math' work 
        # or only 'exams'—and shows just those results.
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
            filtered = [a for a in self.assignments if a.due_date.startswith(criteria_value)]

        if not filtered:
            print(f"\n[Notice] No assignments found matching {criteria_type}: '{criteria_value}'.")
            return

        print(f"\n--- Filtered Assignments ({criteria_type}: {criteria_value}) ---")
        for index, assignment in enumerate(filtered, start=1):
            print(f"{index}. {assignment.display_details()}")

    def show_summary(self):
        # Crunches the numbers to show our overall grade, how we are doing 
        # in each subject, and our very best and worst assignments.
        if not self.assignments:
            print("\n[Notice] No assignments available to generate a summary report.")
            return

        # STATISTICAL ANALYSIS: Overall Grade
        # Adds up all our earned points and divides by the total possible points 
        # to calculate our final, overall big-picture grade.
        total_score = sum(a.score for a in self.assignments)
        total_max_score = sum(a.max_score for a in self.assignments)
        overall_percentage = (total_score / total_max_score) * 100 if total_max_score > 0 else 0

        # STATISTICAL ANALYSIS: Subject Averages
        # Groups our scores together by subject (like Math or History) so we can 
        # see our average grade for each specific class.
        subjects = {}
        for a in self.assignments:
            if a.subject not in subjects:
                subjects[a.subject] = {"score": 0.0, "max_score": 0.0, "count": 0}
            subjects[a.subject]["score"] += a.score
            subjects[a.subject]["max_score"] += a.max_score
            subjects[a.subject]["count"] += 1

        # STATISTICAL ANALYSIS: Highest and Lowest Scores
        # Looks at the percentage of every single assignment to find 
        # the absolute best and worst scores we got.
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