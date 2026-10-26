#grades average version1
grades = list(map(int, input("Enter your exam grades: ").split()))

average = round((sum(grades) / len(grades)), 2)

if 90 <= average <= 100:
    grade_letter = 'A'
elif 75 <= average:
    grade_letter = 'B'
elif 60 <= average:
    grade_letter = 'C'
elif 50 <= average:
    grade_letter = 'D'
elif 0 <= average:
    grade_letter = 'F'
else:
    grade_letter = 'Invalid value'
print(f"Average grade is: {average}    {grade_letter}")