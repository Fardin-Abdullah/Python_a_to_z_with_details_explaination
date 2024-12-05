def calculate_required_grades(current_cgpa, target_cgpa, total_credits_completed, total_credits_planned):
    """
    Calculates the required grades to achieve a target CGPA.

    Args:
        current_cgpa (float): Current CGPA (e.g., 2.00).
        target_cgpa (float): Target CGPA (e.g., 3.5).
        total_credits_completed (int): Total credits completed so far.
        total_credits_planned (int): Total credits planned for future courses.

    Returns:
        dict: A dictionary mapping course names to required letter grades.
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

    current_total_grade_points = current_cgpa * total_credits_completed
    target_total_grade_points = target_cgpa * (total_credits_completed + total_credits_planned)
    additional_grade_points_needed = target_total_grade_points - current_total_grade_points

    required_grades = {}

    for course_name in range(1, total_credits_planned + 1):
        # Calculate the required grade for each course
        required_grade_points = additional_grade_points_needed / total_credits_planned
        for grade, points in grade_points.items():
            if points >= required_grade_points:
                required_grades[f"Course {course_name}"] = grade
                break

    return required_grades

# Example usage:
current_cgpa = 2.00
target_cgpa = 3.5
total_credits_completed = 60  # Example: Total credits completed so far
total_credits_planned = 30  # Example: Total credits planned for future courses

required_grades = calculate_required_grades(current_cgpa, target_cgpa, total_credits_completed, total_credits_planned)
for course, grade in required_grades.items():
    print(f"To achieve a CGPA of {target_cgpa}, aim for {grade} in {course}.")
