from calculator import add, subtract
import student_analyzer as std
if __name__ == "__main__":
    print("main is executing")

students=[
    {"name":"Alice","cgpa":3.5},
    {"name":"Bob","cgpa":2.8},
    {"name":"Charlie","cgpa":3.9},
    {"name":"David","cgpa":2.5},
    {"name":"Eve","cgpa":3.2}
    ]
# Student Analytics Engine
print("===============================")
print("   Student Analytics Engine")
print("===============================")
print("1. Display Students")
print("2. Add Student")
print("3. Get Names of Students")
print("4. Get CGPAs of Students")
print("5. Calculate Average CGPA")
print("6. Get Top Students")
print("7. Get Passing Students")
print("8. Generate Report")
print("9. Add two numbers")
print("10.Subtract two numbers")

operation=int(input("Select an operation (1-8): "))
if operation==1:
    std.display_students(students)
elif operation==2:
    std.add_student(students)
elif operation==3:
    names=std.get_names(students)
    print(names)
elif operation==4:
    cgpas= std.get_cgpas(students)
    print(cgpas)
elif operation==5:
    average_cgpa= std.calculate_average_cgpa(students)
    print(average_cgpa)
elif operation==6:
    top_students= std.get_top_students(students)
    print(top_students)
elif operation==7:
    passing_students=std.get_passing_students(students)
    print(passing_students)
elif operation==8:
    std.generate_report(students)
elif operation==9:
    number1=float(input("Enter first number"))
    number2=float(input("Enter second number"))
    result=add(number1,number2)
    print(result)
elif operation==10:
    number1=float(input("Enter first number"))
    number2=float(input("Enter second number"))
    result=subtract(number1,number2)
    print(result)
else:
    print("Invalid option!")