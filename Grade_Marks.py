# Mark=int(input("Enter the marks:"))
# if(Mark>=90):
#     print("Grade:O")
# elif(Mark>=80 and Mark<90):
#     print("Grade:A")
# elif(Mark>=70 and Mark<80):
#     print("Grade:B")
# elif(Mark>=60 and Mark<70):
#     print("Grade:C")
# else:
#     print("Grade:Fail")

while True:
    mark = int(input("Enter the marks (0–100): "))
    if 0 <= mark <= 100:
        break
    else:
        print("Invalid input! Try again.")

if mark >= 90:
    print("Grade: O")
elif mark >= 80:
    print("Grade: A")
elif mark >= 70:
    print("Grade: B")
elif mark >= 60:
    print("Grade: C")
else:
    print("Grade: Fail")
