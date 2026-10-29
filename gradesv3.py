import gradesv1

def get_grades():
    grades = {}
    while True:
        try:
            subject = input("Enter a subject name: (enter 0 to end) ")
            if subject == '0':
                break
        except ValueError:
            print("Enter a valid subject name")
            break

        try:
            subject_grade = int(input("Enter a grade for the subject: "))
            if subject_grade > 100 or subject_grade < 0:
                print("The grade should be between 0 and 100")
                return grades   
        except ValueError:
            print("Enter a number")

        grades[subject] = subject_grade

    return grades

def calculate_average(grades): #Calculates average of grades

    average = round((sum(grades.values()) / len(grades)), 2)
    return average

def main():
    grades = {}
    grades = get_grades()
    print(grades)
    average = calculate_average(grades)
    print(average)
    """get_letter_grade(grades)"""

if __name__ == "__main__":
    main()