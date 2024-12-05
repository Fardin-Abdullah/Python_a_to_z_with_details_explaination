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

# Example usage:
semester1_grades = [(3, 3.7), (4, 4.0), (3, 3.3)]  # (credit_hours, gpa_value) for each course
semester2_grades = [(3, 3.0), (4, 3.7), (3, 3.3)]
semester3_grades = [(3, 3.3), (4, 3.0), (3, 2.7)]
semester4_grades = [(3, 3.7), (4, 3.3), (3, 3.0)]
semester5_grades = [(3, 3.0), (4, 3.7), (3, 3.3)]

all_semester_grades = semester1_grades + semester2_grades + semester3_grades + semester4_grades + semester5_grades
cgpa_result = calculate_cgpa(all_semester_grades)

print(f"Your CGPA: {cgpa_result:.2f}")
