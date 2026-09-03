contact = []
def action(Action):
    match Action:
        case 1:
            print(f"====Contacts List====\n {contact}")
        case 2:
            name = input("Enter the Name: ")
            num = int(input("Enter the number: "))
            add(contact, name, num)
        case 3:
            print("====Search Bar====")
            search_value = input("Enter Name or Number: ")
            ser(contact, search_value)
        case 4:
            print("===Deleting COntact===")
            search_value =input("Enter the Name or Number: ")
            dele(contact, search_value)
        case 5:
            print("===update Contact===")
            search_value = input("Enter the Name or Number: ")
            update = input("What's to change Name or Number: ").lower()
            update_value = input(f"Write new {update}: ")
            if update == "number":
             update_value = int(update_value)
            upd(contact, search_value, update, update_value)

def add(contact, name, num):
    contact.append({"name": name, "number": num})
    return print("Done!")

def ser(contact, search_value):
    for c in contact:
          if c["name"] == search_value or str(c["number"]) == search_value:
               return print(f"Record: {c}")
    return print("NO Record Found!")

def dele(contact, search_value):
    for c in contact:
        if c["name"] == search_value or str(c["number"]) == search_value:
            contact.remove(c)
            return print("Done!")
    return print("No Record Found!")

def upd(contact, search_value, update, update_value):
    for c in contact:
        if c["name"] == search_value or str(c["number"]) == search_value:
            c[update] = update_value
            return print("Done!")
    return print("No Record Found!")

while True:
    print("======Contacts======")
    Action = int(input("1: Show Contacts \n2: Add Contact\n3: Search\n4: Delete Contact\n5: Update Contact\n6: exit\n =="))
    if Action == 6:
        print("====Existing Contacts====")
        break
    else:
        action(Action)