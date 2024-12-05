
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

# Example usage
year = int(input("Enter the year: "))
semester = input("Choose a semester (Spring/Summer/Autumn): ")
full_semester_key = semester.capitalize() + " " + str(year)
calculate_gpa(full_semester_key)
