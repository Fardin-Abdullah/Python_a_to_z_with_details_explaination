class Varsity:

    #Function 1 ---> Course Registration
    def course_registration():
        year = int(input("Enter the year:"))

        semesters = {
            "spring " + str(year): [],
            "summer " + str(year): [],
            "autumn " + str(year): []
        }

        key = list(semesters.keys())

        while True:
            selected_semester = input("Choose a semester (Spring/Summer/Autumn): ").lower()
            full_semester_key = selected_semester + " " + str(year)
            full_semester_key_upper =full_semester_key.upper()
            if full_semester_key in semesters:
                break
            else:
                print("Invalid semester. Please choose from Spring, Summer, or Autumn.")

        while True:
            course_name = input("Enter a course name (or 'done' to finish): ")
            if course_name.lower() == "done":
                break
            semesters[full_semester_key].append(course_name)

        print("Courses for", full_semester_key.upper(), "semester:", semesters[full_semester_key])

    #Funtion 2 ---> calculate gpa

    def calculate_gpa(full_semester_key):
        grade_dic = {
            "A": 4.00,
            "A-": 3.70,
            "B+": 3.30,
            "B": 3.00,
            "B-": 2.70,
            "C+": 2.30,
            "C": 2.00,
            "C-": 1.70,
            "D+": 1.30,
            "D": 1.00,
            "F": 0.00
        }

        total_credits = 0
        total_gpa = 0.0

        while True:
            course_name = input("Enter course name (or 'done' to finish): ")
            if course_name.lower() == "done":
                break

            credit_hours = float(input("Enter credit hours for {}: ".format(course_name)))
            letter_grade = input("Enter grade for {}: ".format(course_name))

            if letter_grade in grade_dic:
                gpa_value = grade_dic[letter_grade]
                total_credits += credit_hours
                total_gpa += gpa_value * credit_hours
            else:
                print("Invalid grade. Please enter a valid letter grade.")

        if total_credits > 0:
            final_gpa = total_gpa / total_credits
            print("Your GPA for {} semester: {:.2f}".format(full_semester_key, final_gpa))
        else:
            print("No courses entered. GPA calculation not possible.")


    #Funtion 3 ---> calculate cgpa
    def calculate_cgpa(semester_grades):
        """
        Calculates the CGPA based on a list of semester grades.

        Args:
            semester_grades (list of tuples): Each tuple contains (credit_hours, gpa_value).

        Returns:
            float: The CGPA.
        """
        total_credits = 0
        total_weighted_gpa = 0.0

        for credit_hours, gpa_value in semester_grades:
            total_credits += credit_hours
            total_weighted_gpa += gpa_value * credit_hours

        if total_credits > 0:
            cgpa = total_weighted_gpa / total_credits
            return cgpa
        else:
            return 0.0  # No courses entered, so CGPA is 0

    

    #Funtion 4 ---> retake
    def check_grades(semesters):
        """
        Checks if any course grade is less than B and recommends retaking if needed.

        Args:
            semesters (dict): A dictionary containing semesters as keys and lists of course grades as values.

        Returns:
            list: Recommendations for retaking courses.
        """
        grade_points = {
            'A': 4.00,
            'A-': 3.70,
            'B+': 3.30,
            'B': 3.00,
            'B-': 2.70,
            'C+': 2.30,
            'C': 2.00,
            'C-': 1.70,
            'D+': 1.30,
            'D': 1.00,
            'F': 0.00
        }

        recommendations = []

        for semester, courses in semesters.items():
            for course_grade in courses:
                if course_grade in grade_points:
                    if grade_points[course_grade] < grade_points['B']:
                        recommendations.append(f"Consider retaking {course_grade} in {semester}.")
                else:
                    print(f"Invalid grade '{course_grade}' encountered.")

        return recommendations
    

    #Function 5 --->Target CGPA
    
    def calculate_required_grades(current_cgpa, target_cgpa, total_credits_completed, total_credits_planned):
        grade_points = {
            'A': 4.00,
            'A-': 3.70,
            'B+': 3.30,
            'B': 3.00,
            'B-': 2.70,
            'C+': 2.30,
            'C': 2.00,
            'C-': 1.70,
            'D+': 1.30,
            'D': 1.00,
            'F': 0.00
        }

        current_total_grade_points = current_cgpa * total_credits_completed
        target_total_grade_points = target_cgpa * (total_credits_completed + total_credits_planned)
        additional_grade_points_needed = target_total_grade_points - current_total_grade_points
        required_grades = additional_grade_points_needed/total_credits_planned
        if required_grades > 4.00 :
            print("You should retake previous course for improving\nCause your required grade is",required_grades)
            print("Let's check which course do you need to take to improve?")
            semesters_data = {}
            while True:
                semester = input("Enter the semester (e.g., 'Spring 2023'): ")
                grades = input("Enter the grades separated by spaces (e.g., 'A B- C D'): ").split()
                
                # Add the semester and grades to the dictionary
                semesters_data[semester] = grades
                
                another_semester = input("Do you want to add another semester? (yes/no): ")
                if another_semester.lower() != 'yes':   
                    break


            retake_recommendations = Varsity.check_grades(semesters_data)
            for recommendation in retake_recommendations:
                print(recommendation)
            Varsity.check_grades(semesters_data)

        else:
            print("You should get GP",required_grades, "for every course ")
                

        return required_grades

    
    #Funtion 6 --- Count semester
    def count_sem():
        semesters = {}  # Dictionary to store courses by semester

        while True:
            year = int(input("Enter the year (or 0 to finish): "))
            if year == 0:
                break

            semester = input("Choose a semester (Spring/Summer/Autumn): ").capitalize()
            full_semester_key = f"{semester} {year}"

            if full_semester_key not in semesters:
                semesters[full_semester_key] = []
            else:
                print(f"{full_semester_key} already exists. Please choose a different semester.")

            while True:
                course_name = input("Enter a course name (or 'done' to finish): ")
                if course_name.lower() == "done":
                    break
                semesters[full_semester_key].append(course_name)

        print("\nSemesters entered:")
        for semester_key in semesters:
            print(semester_key)

def main():
    options = ["Course Registration", "Calculate GPA", "Calculate CGPA", "Retake Courses", "Count Semester", "Target CGPA"]

    print("Available options:")
    for index, option in enumerate(options, start=1):
        print(f"{index}. {option}")

    # Example usage:
    user_choice = int(input("Enter the number corresponding to your choice: "))
    selected_option = options[user_choice - 1]
    print(f"You selected: {selected_option}")

    if selected_option == options[0]:
        Varsity.course_registration()

    elif selected_option == options[1]:
        year = int(input("Enter the year: "))
        semester = input("Choose a semester (Spring/Summer/Autumn): ")
        full_semester_key = semester.capitalize() + " " + str(year)
        Varsity.calculate_gpa(full_semester_key)
    elif selected_option == options[2]:
        # Example usage:
        n = int(input("How many semesters have you completed?"))
        semester_list = {f"Semester{i}": [] for i in range(1, n + 1)}
        all_semester_grades = []  # Initialize outside the loop

        for i in range(1, n + 1):
            credit_hours = float(input(f"Enter credit hours for Semester {i}: "))
            gpa_value = float(input(f"Enter GPA value for Semester {i}: "))
            semester_list[f"Semester{i}"].append((credit_hours, gpa_value))
            all_semester_grades.extend(semester_list[f"Semester{i}"])  # Accumulate grades
            cgpa_result = Varsity.calculate_cgpa(all_semester_grades)

        print(f"Your CGPA: {cgpa_result:.2f}")

    elif selected_option == options[3]:
        semesters_data = {}
        while True:
            semester = input("Enter the semester (e.g., 'Spring 2023'): ")
            grades = input("Enter the grades separated by spaces (e.g., 'A B- C D'): ").split()
            
            # Add the semester and grades to the dictionary
            semesters_data[semester] = grades
            
            another_semester = input("Do you want to add another semester? (yes/no): ")
            if another_semester.lower() != 'yes':   
                break


        retake_recommendations = Varsity.check_grades(semesters_data)
        for recommendation in retake_recommendations:
            print(recommendation)
        Varsity.check_grades(semesters_data)
    elif selected_option == options[4]:
        Varsity.count_sem()
    elif selected_option == options[5]:

        current_cgpa = float(input("Enter your current CGPA:"))
        target_cgpa = float(input("Enter your target CGPA:"))
        total_credits_completed = int(input("Enter your total credit:"))  # Example: Total credits completed so far
        total_credits_planned = int(input("Enter your total credits plan:"))  # Example: Total credits planned for future courses

        required_grades = Varsity.calculate_required_grades(current_cgpa, target_cgpa, total_credits_completed, total_credits_planned)
        print(required_grades)
if __name__ == "__main__":
    main()