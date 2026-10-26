grades = list(map(int, input("Enter your exam grades: ").split()))

for i in grades:
        if i < 0 or i > 100:
            print( "Invalid input")
        else:
            average = round((sum(grades) / len(grades)), 2)
            print(average)
            print(type(average))