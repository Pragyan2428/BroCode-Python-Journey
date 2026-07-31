def main():
    students = {
        "Pragyan" : "A",
        "Laksha"  : "A",
        "Neevan" :  "B"
    }
    student = input("Enter the name of the student: ")
    if student not in students:
        print(f"{student} was not found in the list.")
    else:
        print("Student was found.")
        print(f"{student} grade is {students[student]}")
main()