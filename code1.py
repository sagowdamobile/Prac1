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


def delete_task(tasks):
	"""Delete a task using its task number."""
	if not tasks:
		print("No tasks to delete.\n")
		return

	# Show current tasks so user can choose a valid number
	view_tasks(tasks)

	number_text = input("Enter task number to delete: ").strip()

	if not number_text.isdigit():
		print("Please enter a valid number.\n")
		return

	index = int(number_text) - 1

	if 0 <= index < len(tasks):
		removed_task = tasks.pop(index)
		print(f"Deleted task: {removed_task}\n")
	else:
		print("Task number out of range.\n")


def show_menu():
	"""Display menu options to the user."""
	print("To-Do List Menu")
	print("1. Add a task")
	print("2. View all tasks")
	print("3. Delete a task")
	print("4. Exit")


def main():
	# List used to store tasks
	tasks = []

	# Loop keeps the app running until user chooses Exit
	while True:
		show_menu()
		choice = input("Choose an option (1-4): ").strip()

		if choice == "1":
			add_task(tasks)
		elif choice == "2":
			view_tasks(tasks)
		elif choice == "3":
			delete_task(tasks)
		elif choice == "4":
			print("Goodbye!")
			break
		else:
			print("Invalid choice. Please enter 1, 2, 3, or 4.\n")


# Run the program
if __name__ == "__main__":
	main()

#checked
