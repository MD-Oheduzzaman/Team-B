name = input("Enter student name: ")
marks = float(input("Enter marks: "))

if marks >= 80:
    grade = "A+"
elif marks >= 70:
    grade = "A"
elif marks >= 60:
    grade = "A-"
elif marks >= 50:
    grade = "B"
elif marks >= 40:
    grade = "C"
else:
    grade = "F"

print("\nStudent Name:", name)
print("Marks:", marks)
print("Grade:", grade)