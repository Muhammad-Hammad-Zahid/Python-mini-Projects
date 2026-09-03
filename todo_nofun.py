tasks = []

# Step 2: Main loop to keep the program running
while True:
    print("\n--- TO-DO LIST ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")

    # Step 3: Handle execution logic based on user choice
    if choice == "1":
        if not tasks:
            print("\nYour to-do list is empty!")
        else:
            print("\nYour Tasks:")
            # enumerate() numbers the items automatically starting from 1
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")
                
    elif choice == "2":
        new_task = input("\nEnter the task: ")
        if new_task.strip() != "":
            tasks.append(new_task)
            print(f"'{new_task}' has been added successfully!")
        else:
            print("Task cannot be empty.")
            
    elif choice == "3":
        if not tasks:
            print("\nNo tasks available to delete.")
        else:
            try:
                task_num = int(input("\nEnter the number of the task to delete: "))
                # Validate if the entered number matches an actual item in the list
                if 1 <= task_num <= len(tasks):
                    removed = tasks.pop(task_num - 1)
                    print(f"'{removed}' has been removed.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
                
    elif choice == "4":
        print("\nGoodbye! Have a productive day.")
        break
        
    else:
        print("Invalid option. Please choose a number between 1 and 4.")