def main():
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

if __name__ == "__main__":
    main()
