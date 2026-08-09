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
        total_score = sum(a.score for a in self.assignments)
        total_max_score = sum(a.max_score for a in self.assignments)
        overall_percentage = (total_score / total_max_score) * 100 if total_max_score > 0 else 0

        # STATISTICAL ANALYSIS: Subject Averages
        subjects = {}
        for a in self.assignments:
            if a.subject not in subjects:
                subjects[a.subject] = {"score": 0.0, "max_score": 0.0, "count": 0}
            subjects[a.subject]["score"] += a.score
            subjects[a.subject]["max_score"] += a.max_score
            subjects[a.subject]["count"] += 1

        # STATISTICAL ANALYSIS: Highest and Lowest Scores
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