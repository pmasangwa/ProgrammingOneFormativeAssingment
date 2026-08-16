# This is my main class to hold all the data for an assignment to be created.

class Assignment:
    # This runs everytime when I create a new assignment object.
    def __init__(self, subject, title, score, max_score, due_date, atype):
        # I'm saving all the variables passed in to the object
        self.subject = subject.lower()
        self.title = title
        # Making sure scores are decimals so the math works later
        self.score = float(score)
        self.max_score = float(max_score)
        self.due_date = due_date
        self.type = atype.lower()

    # A function to print out the assignment details in one line
    def display_details(self):
        # This is to prevent division by zero if any max_score is 0 by mistake
        if self.max_score > 0:
            percentage = (self.score / self.max_score) * 100
        else:
            percentage = 0
            
        # I just added strings together because it's easier to read and follow than using f-strings or .format().
        return "Subject: " + self.subject + " | Title: " + self.title + " | Type: " + self.type + " | Score: " + str(self.score) + "/" + str(self.max_score) + " (" + str(round(percentage, 2)) + "%) | Due: " + self.due_date

# I made separate classes for Homework and Exam.
# They inherit from Assignment so I don't have to rewrite the __init__ code all over again.
class Homework(Assignment):
    def __init__(self, subject, title, score, max_score, due_date):
        # super() calls the Assignment __init__ and passes "homework" as the type
        super().__init__(subject, title, score, max_score, due_date, "homework")

class Exam(Assignment):
    def __init__(self, subject, title, score, max_score, due_date):
        # same thing is done here but passing "exam"
        super().__init__(subject, title, score, max_score, due_date, "exam")

# This is the class that manages all my grades in one place
class GradeTracker:
    def __init__(self):
        # Just an empty list to hold my objects
        self.assignments = []

    def add_assignment(self, assignment):
        # add the new assignment to the end of the list
        self.assignments.append(assignment)

    def list_assignments(self):
        # check if the list is empty first
        if len(self.assignments) == 0:
            print("No assignments saved yet.")
            return # stops the function here
        
        print("\n--- Recorded Assignments ---")
        # I used a count variable to number my list
        count = 1
        for item in self.assignments:
            print(str(count) + ". " + item.display_details())
            count = count + 1

    def filter_assignments(self, criteria_type, criteria_value):
        if len(self.assignments) == 0:
            print("Nothing to filter.")
            return

        # Empty list to hold the ones that match what we are looking for
        filtered_list = []
        criteria_value = criteria_value.lower()

        # Branch 1: If they want to search by type (homework or exam)
        if criteria_type == "type":
            for item in self.assignments:
                if item.type == criteria_value:
                    filtered_list.append(item)
                    
        # Branch 2: If they want to search by a specific subject
        elif criteria_type == "subject":
            for item in self.assignments:
                if item.subject == criteria_value:
                    filtered_list.append(item)
                    
        # Branch 3: If they want to search by a date/month
        elif criteria_type == "month":
            for item in self.assignments:
                # check if the start of the date matches the user's input
                if item.due_date.startswith(criteria_value):
                    filtered_list.append(item)

        # See if we actually found anything
        if len(filtered_list) == 0:
            print("Couldn't find anything matching that.")
        else:
            print("\n--- Filtered Results ---")
            count = 1
            for item in filtered_list:
                print(str(count) + ". " + item.display_details())
                count = count + 1

    def show_summary(self):
        # Check if we have grades to summarize
        if len(self.assignments) == 0:
            print("No grades to summarize.")
            return

        # 1. Figure out the overall grade
        total_score = 0
        total_max = 0
        
        # Looping through everything and adding1 up the scores
        for item in self.assignments:
            total_score = total_score + item.score
            total_max = total_max + item.max_score
            
        if total_max > 0:
            overall_percent = (total_score / total_max) * 100
        else:
            overall_percent = 0
            
        print("\n--- Grade Summary ---")
        print("Total Assignments: " + str(len(self.assignments)))
        print("Overall Grade: " + str(round(overall_percent, 2)) + "%")

        # 2. Figure out the best and worst assignment
        # I set the highest and lowest to the first item to start comparing
        highest_item = self.assignments[0]
        lowest_item = self.assignments[0]
        
        highest_percent = (highest_item.score / highest_item.max_score) * 100
        lowest_percent = (lowest_item.score / lowest_item.max_score) * 100
        
        # Loop through everything to see if there is a higher or lower score
        for item in self.assignments:
            if item.max_score > 0:
                item_percent = (item.score / item.max_score) * 100
                
                # Check if this item is the new highest
                if item_percent > highest_percent:
                    highest_percent = item_percent
                    highest_item = item
                    
                # Check if this item is the new lowest
                if item_percent < lowest_percent:
                    lowest_percent = item_percent
                    lowest_item = item

        print("\nBest Assignment: " + highest_item.title + " - " + str(round(highest_percent, 2)) + "%")
        print("Worst Assignment: " + lowest_item.title + " - " + str(round(lowest_percent, 2)) + "%")
        
        # 3. Figure out grades per subject
        print("\nSubject Averages:")
        # Two dictionaries: one to hold the points earned, one for the total possible points
        subject_scores = {}
        subject_max = {}
        
        for item in self.assignments:
            # If we haven't seen this subject yet, add it to the dictionaries
            if item.subject not in subject_scores:
                subject_scores[item.subject] = 0
                subject_max[item.subject] = 0
            
            # Add the current item's scores to that subject's total
            subject_scores[item.subject] = subject_scores[item.subject] + item.score
            subject_max[item.subject] = subject_max[item.subject] + item.max_score
            
        # Loop through the dictionary we just built to print the results
        for subj in subject_scores:
            if subject_max[subj] > 0:
                subj_grade = (subject_scores[subj] / subject_max[subj]) * 100
                print(" - " + subj + ": " + str(round(subj_grade, 2)) + "%")