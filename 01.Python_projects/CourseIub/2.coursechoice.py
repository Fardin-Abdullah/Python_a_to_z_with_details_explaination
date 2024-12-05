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
