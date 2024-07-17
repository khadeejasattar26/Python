#user is giving input for marks
marks = int(input("Enter marks (0-100): "))

#calculating and displaying grade20
if marks < 0 or marks > 100:
    print("Invalid Marks")
elif marks < 50:
    print("Grade F")
elif marks < 60:
    print("Grade E")
elif marks < 70:
    print("Grade D")
elif marks < 80:
    print("Grade C")
elif marks < 90:
    print("Grade B")
else:
    print("Grade A")
