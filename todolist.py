# To-Do List Application in Python

def display_tasks(tasks):
    print("\nTo-Do List:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

# Function to add a task to the list
def add_task(tasks):
    task = input("Enter the task you want to add: ")
    tasks.append(task)
    print("Task added.")

# Function to delete a task from the list
def delete_task(tasks):
    display_tasks(tasks)
    try:
        task_index = int(input("Enter the task number you want to delete: "))
        if 1 <= task_index <= len(tasks):
            removed_task = tasks.pop(task_index - 1)
            print(f"Task removed: {removed_task}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main function
def main():
    tasks = []  # List to store tasks

    while True:
         print("\nOptions:")
         print("1. Add a task")
         print("2. View tasks")
         print("3. Delete a task")
         print("4. Exit")

         choice = input("Enter your choice: ")

         if choice == '1':
             add_task(tasks)
         elif choice == '2':
             display_tasks(tasks)
         elif choice == '3':
             delete_task(tasks)
         elif choice == '4':
             print("Exiting the To-Do List application.")
             break
         else:
             print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
