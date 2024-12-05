semesters_data = {}

while True:
    semester = input("Enter the semester (e.g., 'Spring 2023'): ")
    year = input("Enter the year (e.g., '2023'): ")
    course_name = input("Enter the course name: ")
    grade = input("Enter the grade (e.g., 'A'): ")

    # Combine semester and year to create a unique key
    semester_key = f"{semester} {year}"
    
    # Add the course name and grade to the dictionary
    if grade == 'C':
        semesters_data[semester_key] = course_name
    
    another_semester = input("Do you want to add another semester? (yes/no): ")
    if another_semester.lower() != 'yes':
        break

print("Courses to retake:")
for semester_key, course_name in semesters_data.items():
    print(f"{semester_key}: {course_name}")
