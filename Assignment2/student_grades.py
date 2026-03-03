import sys


def print_menu():
	print("\nStudent Grades Manager")
	print("1. Add a new student and grade")
	print("2. Update an existing student's grade")
	print("3. Print all student grades")
	print("4. Exit")


def add_student(grades):
	name = input("Enter student name: ").strip()
	if not name:
		print("Name cannot be empty.")
		return
	if name in grades:
		print(f"{name} already exists with grade {grades[name]}.")
		return
	grade = input("Enter grade (0-100): ").strip()
	if not grade.isdigit():
		print("Invalid grade. Please enter a number.")
		return
	grades[name] = int(grade)
	print(f"Added {name} with grade {grades[name]}.")


def update_student(grades):
	name = input("Enter student name to update: ").strip()
	if name not in grades:
		print(f"{name} not found.")
		return
	grade = input(f"Enter new grade for {name} (0-100): ").strip()
	if not grade.isdigit():
		print("Invalid grade. Please enter a number.")
		return
	grades[name] = int(grade)
	print(f"Updated {name} to grade {grades[name]}.")


def print_grades(grades):
	if not grades:
		print("No student grades available.")
		return
	print("\nAll Student Grades:")
	for name, grade in grades.items():
		print(f"- {name}: {grade}")


def main():
	grades = {}
	while True:
		print_menu()
		choice = input("Choose an option (1-4): ").strip()
		if choice == '1':
			add_student(grades)
		elif choice == '2':
			update_student(grades)
		elif choice == '3':
			print_grades(grades)
		elif choice == '4':
			print("Goodbye.")
			break
		else:
			print("Invalid choice. Please enter 1-4.")


if __name__ == '__main__':
	main()

