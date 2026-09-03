To_Do = {}

def view(To_Do):
    for i, (name, values) in enumerate(To_Do.items()):
        print(f"({i+1}): {name}")
        for data in values:
          for key, values2 in data.items():
            print(f"\t{key}: {values2}")          
    return print("END")

def add(To_Do):
    print("Add new Task: ")
    typ = int(input("Select the type: \n(1): Yes/No \n(2): Measurable \n Enter the value: "))
    task = input("Title: ")
    To_Do[task] = []
    if typ == 2:
        unit = input("Unit \"e.g., Minutes, Hours, Days \": ")
        dura = int(input("Duration: "))
        status = "Pending"
        To_Do[task].append({'Type': typ, 'Unit': unit, 'Duration': dura, 'Status': status})
    else:
        status = "Pending"
        To_Do[task].append({'Type': typ, 'Status': status})
    return print("\"New Task is Created!\"")

def dele(To_Do):
    if not To_Do:
                print("\nNo tasks available to delete.")
    else:
        try:
            for i, name in enumerate(To_Do.keys()):
                    print(f"({i+1}): {name}")
            task_num = int(input("\nEnter the number of the task to delete: "))

            # Validate if the entered number matches an actual item in the list
            keys_list = list(To_Do.keys())
            if 1 <= task_num <= len(To_Do):
                key_to_delete = keys_list[task_num - 1]
                To_Do.pop(key_to_delete)
                print(f"'{key_to_delete}' has been removed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
    print("Done!")
    return To_Do

def updatestatus(To_Do):
    if not To_Do:
                    print("\nNo tasks available.")
    else:
        try:
            for i, name in enumerate(To_Do.keys()):
                print(f"({i+1}): {name}") 
            task_num = int(input("\nEnter the number of the task: "))
            # Validate if the entered number matches an actual item in the list
            keys_list = list(To_Do.keys())
            if 1 <= task_num <= len(To_Do):
                task = keys_list[task_num - 1]
                key_to_update = To_Do[task][0]
                if key_to_update['Type'] == 2:
                    New_status = float(input("Enter duration (acording to the describe unit): "))
                    if key_to_update['Duration'] > New_status:
                        key_to_update['Status'] = "Partial"
                    else:
                        key_to_update['Status'] = "Completed" 
                else:
                    New_status = input(f"Are you done with '{task}' task? ('(y)Yes'/(n)'No'): ")
                    if New_status == 'y' or New_status == 'Y':
                         key_to_update['Status'] = "Complete"
                    elif New_status == 'N' or New_status == 'n':
                         print("Keep Working Hard")
                    else:
                         print("Invalid input")
                print(f"{task}'s status has been Updated.")
            else:
                print("Invalid task number.")
        except ValueError:
                print("Please enter a valid number.")
    print("Done!")
    return To_Do

def updatetask(To_Do):
    def rename_key(d, old_key, new_key):
        new_dict = {}
        for k, v in d.items():
            if k == old_key:
                new_dict[new_key] = v
            else:
                new_dict[k] = v
        return new_dict
    if not To_Do:
                        print("\nNo tasks available.")
    else:
        try:
            for i, name in enumerate(To_Do.keys()):
                print(f"({i+1}): {name}")
            task_num = int(input("\nEnter the number of the task (\"Type can't be change\"): "))
            # Validate if the entered number matches an actual item in the list
            keys_list = list(To_Do.keys())
            if 1 <= task_num <= len(To_Do):
                task = keys_list[task_num - 1]
                key_to_update = To_Do[task][0]
                field_to_change = input("Enter the Entity you want to update \n\"(1). Title\n(2). Unit\n(3). Duration\")\nEntitie: ")
                field_map = {'1': 'Title', '2': 'Unit', '3': 'Duration'}
                change = field_map.get(field_to_change)
                if change is None:
                    print("Invalid choice.")
                    print("Done!")
                    return To_Do
                new = input(f"Enter New {change}: ")
                if change == 'Title':
                   To_Do = rename_key(To_Do, task, new)
                   print(f"'{task}' has been renamed to '{new}'.")  
                else:
                    if change not in key_to_update:
                        print(f"'{change}' doesn't apply to this task type.")
                    else:
                        if change == 'Unit':
                            new_duration = int(input("Enter new Duration \" e.g., Minutes, Hours, Days \": "))
                            key_to_update['Duration'] = new_duration
                            print("New Duration has been set")
                        if change == 'Duration':
                            new = int(new)
                        key_to_update[change] = new
                        print(f"{task}'s {change} has been Updated {new}.")
            else:
                print("Invalid task number.")
        except ValueError:
                    print("Please enter a valid number.")
    print("Done!")
    return To_Do


print("====Welcome to To_Do List Application====")
while True:
    print("\n--- TO-DO LIST ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Update Task Status")
    print("5. Update Task")
    print("6. Exit")
    
    choice = input("Enter your choice (1-6): ")
    if choice == '1':
          view(To_Do)
    elif choice == '2':
          add(To_Do)
    elif choice == '3':
          To_Do = dele(To_Do)
    elif choice == '4':
          To_Do = updatestatus(To_Do)
    elif choice == '5':
          To_Do = updatetask(To_Do)
    elif choice == '6':
          print("\nGoodbye! Have a productive day.")
          break
    else:
            print("Invalid option. Please choose a number between 1 and 6.")