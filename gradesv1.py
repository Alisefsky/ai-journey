#grades average version1

def calculate_average(grades): #Calculates average of grades
    for i in grades:
        if i < 0 or i > 100:
            return "Invalid input"
        
    average = round((sum(grades) / len(grades)), 2)
    return average

def get_letter_grade(average): #Gets a letter grade based on average
    average = int(average)
    if average < 0 or average > 100:
        return "Invalid value"
    elif 100 >= average >= 90:
        grade_letter = 'A'
    elif average >= 75:
        grade_letter = 'B'
    elif average >= 60:
        grade_letter = 'C'
    elif average >= 50:
        grade_letter = 'D'
    elif average >= 0:
        grade_letter = 'F'
    
    return grade_letter

def main():
    grades = list(map(int, input("Enter your exam grades: ").split()))
    average = calculate_average(grades)
    letter_grade = get_letter_grade(average)
    print(f"Your average grade: {average} which is {letter_grade}")

if __name__ == "__main__":
    main()