# ProgrammingOneFormativeAssignment

# Student Grade/Assignment Tracker 

# Project Overview
The Student Grade/Assignment Tracker is a command line application that is developed using Python inorder to monitor and evaluate academic performance. The application follows object oriented programming(OPP) principles, utilizing a base class and specialized subclasses to represent distinct academic assessments. The program system is designed to be run as single use. This provides an interactive interface for data entry, retrieval, and statistical aggregation for single use only. One the program is terminated the stored data of the "Grades, Assignments, and exams" cannot be retrived.

# Core Features
1. Object Oriented Program(OPP): The software uses a foundational template for all academic tasks. This main template is then expanded to create specific categories, like homework and exams, which keeps the code organized and easier to manage.
2. Data Entry: The program allows users to save their assignment details. It automatically checks the information entered by the user to ensure that numbers and dates are typed correctly before saving them to prevent errors.
3. Filtering: Users can search through their saved assignments to find exactly what they need. They can view assignments by looking at the specific type of task, the subject name, or the month the task is due.
4.  Statistical analysis and summary: The system calculates overall grades and performance. It shows the total grade percentage, the average score for each subject, and points out which assignments received the best and worst scores.

# Execution Instructions
To execute the program locally, ensure that a compatible Python 3 interpreter is installed on the host machine. 
1. Open a terminal or command prompt window.
2. Navigate to the directory containing the program file.
3. Execute the script using the standard Python execution command:
   `python main.py`

# Error Prevention Strategies
To ensure optimal operation and avoid runtime exceptions, users must adhere to the following input constraints enforced by the validation logic:
1. Numeric Constraints: When prompted for scores, input valid floating point or integer values. The system will reject scores that exceed the specified maximum possible score and scores below the minimum possible score.
2. Date Formatting: The application strictly requires dates to be entered sequentially as Year, Month, and Day (YYYY-MM-DD) format. Providing empty strings will result in an error prompt.
3. Menu Navigation: Only select integer values ranging from 0 to 5 during main menu navigation.

# Menu Structure
The application utilizes a linear numerical menu system:
* Option 1: Add new homework. Requires subject, title, maximum score, achieved score, and due date 
* Option 2: Add new exam. Requires identical parameters to the homework function 
* Option 3: List assignments. Displays all stored records sequentially with calculated percentages 
* Option 4: Filter assignments. Provides a secondary prompt to query records by type, subject, or month 
* Option 5: Show summary. Generates the statistical report encompassing total grades and subject averages 
* Option 0: Exit. Terminates the session and clears all stored memory collections 

## Sample Interaction
STUDENT GRADE TRACKER
1) Add homework
2) Add exam
3) List assignments
4) Filter assignments
5) Show summary
0) Exit
Select an option (0-5): 1

--- Add New Homework ---
Enter subject name: Computer Science
Enter homework title: Programming Formative
Enter maximum possible score: 100
Enter achieved score: 95
Enter due date (YYYY-MM-DD): 2026-08-15
Status: Homework assignment recorded successfully.