grade = float(input())
if 0 <= grade <= 10:
    if grade % 0.5 == 0:
        # Check if Grade A
        if 10 >= grade >= 8.5:
            print("Grade A")
        elif 8 >= grade >= 7.5:
            print("Grade B")
        elif 7 >= grade >= 6.5:
            print("Grade C")
        elif 5.5 >= grade <= 6:
            print("Grade D")
        elif 5 > grade >= 0:
            print("Grade F")
        else:
            print("Grades sshould be between zero and 10.")
    else:
        print("Grades should be rounded to the nearest half point.")
else:
    print("Grades should be between zero and 10.")