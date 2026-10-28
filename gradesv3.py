import gradesv1

def get_grades():
    try:
        grades = list(map(int, input("Enter grades in this order(Math Physics Computer_Science Programming): ").split()))
    except ValueError:
        return {"Error": "Invalid input"}
    if len(grades) != 4:
        return {"Error": "Invalid input"}
    
    grades_dict = {"Mathematics": grades[0], "Physics": grades[1], "Computer Science": grades[2], "Programming": grades[3]}
    return grades_dict

def calculate_average(grades): #Calculates average of grades

    average = round((sum(grades.values()) / len(grades)), 2)
    return average
if __name__ == "__main__":
    grades_dict = get_grades()
    if grades_dict == {"Error": "Invalid input"}:
        print("Error, please try again!")
    else:
        print(grades_dict)
        average = calculate_average(grades_dict)
        letter_grade = gradesv1.get_letter_grade(average)
        print(f"Your average grade: {average} which is {letter_grade}")