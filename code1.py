# Simple To-Do List App (Command Line)
# This program lets a user add tasks, view tasks, and exit.


def add_task(tasks):
	"""Ask the user for a task and add it to the list."""
	task = input("Enter a new task: ").strip()

	# Only add non-empty tasks
	if task:
		tasks.append(task)
		print("Task added successfully.\n")
	else:
		print("Task cannot be empty.\n")


def view_tasks(tasks):
	"""Display all tasks in the list."""
	if not tasks:
		print("No tasks found.\n")
		return

	print("\nYour Tasks:")
	# Show tasks with numbers for easier reading
	for index, task in enumerate(tasks, start=1):
		print(f"{index}. {task}")
	print()  # blank line for clean output


def show_menu():
	"""Display menu options to the user."""
	print("To-Do List Menu")
	print("1. Add a task")
	print("2. View all tasks")
	print("3. Exit")


def main():
	# List used to store tasks
	tasks = []

	# Loop keeps the app running until user chooses Exit
	while True:
		show_menu()
		choice = input("Choose an option (1-3): ").strip()

		if choice == "1":
			add_task(tasks)
		elif choice == "2":
			view_tasks(tasks)
		elif choice == "3":
			print("Goodbye!")
			break
		else:
			print("Invalid choice. Please enter 1, 2, or 3.\n")


# Run the program
if __name__ == "__main__":
	main()

#checked
