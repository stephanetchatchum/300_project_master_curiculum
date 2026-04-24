import json  # import json module to save and load tasks from a file

# -------------------------
# LOAD & SAVE FUNCTIONS
# -------------------------

def load_todo_list():
    # Try to open the todo list file and read it
    try:
        # Open todo_list.json in read mode
        with open("todo_list.json", "r") as f:
            return json.load(f)  # convert the JSON file contents back into a Python list and return it
    except FileNotFoundError:
        return []  # if the file doesn't exist yet, return an empty list to start fresh

def save_todo_list():
    # Open todo_list.json in write mode (creates the file if it doesn't exist)
    with open("todo_list.json", "w") as f:
        json.dump(todo_list, f)  # convert the todo_list into JSON format and write it to the file

# -------------------------
# LOAD TASKS AT START
# -------------------------

# Call load_todo_list() once at the start so we don't lose data from previous sessions
todo_list = load_todo_list()

# -------------------------
# MAIN LOOP
# -------------------------

# Loop forever until the user chooses to quit
while True:
    try:
        # Show the menu options and get the user's choice, converting it to an integer
        choice = int(input("Todo list Menu:\n1. Add Task\n2. View All\n3. Mark Complete\n4. Delete Task\n5. Stats\n6. Quit\n"))

        # Check that the choice is within the valid range 1-6
        if choice >= 1 and choice <= 6:

            # ---- ADD TASK ----
            if choice == 1:
                # Ask the user for the task details
                title = input("Enter task title:\n")
                description = input("Enter task description:\n")

                # Append a new task dict to the list with status defaulting to pending
                # e.g. {"title": "Learn Python", "description": "Do 50 projects", "status": "pending"}
                todo_list.append({"title": title, "description": description, "status": "pending"})

                # Save immediately so the new task isn't lost if the program closes
                save_todo_list()
                print("Task Added!")

            # ---- VIEW ALL TASKS ----
            elif choice == 2:
                # Check if there are any tasks to display
                if len(todo_list) == 0:
                    print("No task yet.")
                else:
                    print("\n--- All Tasks ---")

                    # Loop through every task in the list with a 1-based index
                    # enumerate(todo_list, 1) gives us (1, task), (2, task) etc.
                    for i, task in enumerate(todo_list, 1):

                        # Print the task number, status icon, title and description
                        # ✓ if completed, ⭘ if still pending
                        print(f"{i}. {'[✓]' if task['status'] == 'completed' else '[⭘]'} Task Title: {task['title']} - Task description: {task['description']}")

            # ---- MARK COMPLETE ----
            elif choice == 3:
                try:
                    # Ask for the task number and subtract 1 to convert to a 0-based list index
                    # e.g. task number 1 is at index 0 in the list
                    task_num = int(input("Enter the task number you want to mark completed."))-1

                    # Update the status of that task to completed
                    todo_list[task_num]['status'] = 'completed'

                    # Save immediately so the update is reflected in the file
                    save_todo_list()
                    print("Task Updated!")

                except IndexError:
                    # IndexError means the number the user entered doesn't match any task
                    print("Task number doesn't exist. Try again")

            # ---- DELETE TASK ----
            elif choice == 4:
                try:
                    # Ask for the task number and subtract 1 to convert to a 0-based list index
                    task_num = int(input("Enter the task number you want to delete."))-1

                    # Remove the task from the list at that index
                    # .pop() removes the item and shifts all items after it up by one
                    todo_list.pop(task_num)

                    # Save immediately so the deletion is reflected in the file
                    save_todo_list()
                    print("Task Deleted!")

                except IndexError:
                    # IndexError means the number the user entered doesn't match any task
                    print("Task number doesn't exist. Try again")

            # ---- STATS ----
            elif choice == 5:
                # Count how many tasks have status "pending"
                # sum() adds 1 for every task where the condition is True
                num_pend = sum(1 for task in todo_list if task['status'] == 'pending')

                # Count how many tasks have status "completed"
                num_comp = sum(1 for task in todo_list if task['status'] == 'completed')

                # Print the total, pending and completed counts
                # len(todo_list) gives the total number of tasks
                print(f"Total: {len(todo_list)} | Pending: {num_pend} | Completed: {num_comp}")

            # ---- QUIT ----
            elif choice == 6:
                print("Goodbye!")
                break  # exit the while loop, ending the program

        # If the number typed is outside the range 1-6, let the user know
        else:
            print("Invalid Input, enter a number between 1 and 6")

    except ValueError:
        # ValueError is raised when int() receives something that isn't a number e.g. "abc"
        print("Invalid Input. Try again")