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

# Example usage:
semesters_data = {
    'Spring 2023': ['A', 'B-', 'C', 'D'],
    'Summer 2023': ['B+', 'A-', 'F'],
    'Autumn 2023': ['C', 'B', 'A']
}

retake_recommendations = check_grades(semesters_data)
for recommendation in retake_recommendations:
    print(recommendation)
