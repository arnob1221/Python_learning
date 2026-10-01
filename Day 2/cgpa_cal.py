# total_cource = int(input("Number of cource:"))
# total_credit = 0
# total_grade_point = 0
# for i in range(total_cource):

#     cource_credit = float(input("Enter particular cource credit:"))
#     grade_point = float(input("Enter the grade of that cource:"))
# total_credit = float(input("Total credit:"))
# cgpa = (cource_credit*grade_point)/(total_credit)
# print("Your CGPA is:",cgpa)

total_course = int(input("Number of your total scourses: "))

total_credit = 0
total_grade_point = 0

for i in range(total_course):
    print(f"\nCourse {i + 1}")

    course_credit = float(input("Enter your course credit: "))
    grade_point = float(input("Enter your getting grade point: "))

    total_credit += course_credit
    total_grade_point += course_credit * grade_point

cgpa = total_grade_point / total_credit

print("\nTotal Credit:", total_credit)
print("Your CGPA is:", cgpa)