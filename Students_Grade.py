student = {}
Average = {}
subjects = []
def entries(stre, sub, subjects):
    for i in range(stre):
        name_key = input(f"Enter the name Student {i+1}: ")
        student[name_key] = []
        for j in range(sub):
            sub_marks = input(f"Enter the Marks of {name_key} in {subjects[j]}: ")
            student[name_key].append({"Subject":subjects[j], "Marks": sub_marks})
    return print("Done!")

def average(stre, subjects, student):
    for i in subjects:
        print(f"Calculating Average of: {i}")
        Average[i] = []
        total_sum = 0
        for j in student:
            subject_list = student[j]
            for item in subject_list:
                 if item["Subject"] == i:
                    total_sum += int(item["Marks"])
        Ave = total_sum/stre
        Average[i].append({"Subject": i, "Average_Marks": Ave, "Total_Students": stre})
    return print("Done!")

def highest_and_lowest(stre, subjects, student):
    for i in subjects:
        highest = 0
        highest_student = None
        lowest = 0
        lowest_student = None
        for j in student:
            subject_list = student[j]
            student_list = student[j]
            for item in subject_list:
                student_list = student[j]
                if item["Subject"] == i:
                    current = int(item["Marks"])
                    if highest == 0 or current > highest:
                        highest = current
                        highest_student = j
                    if lowest == 0 or current < lowest:
                       lowest = current
                       lowest_student = j
    print("====Highest====")
    print(f"Highest Marks in {i}:")
    print(f" -{highest} and Student name is \"{highest_student}\"")
    print("====Lowest====")
    print(f"Lowest Marks in {i}:") 
    print(f" -{lowest} and Student name is \"{lowest_student}\"")
    return print("Done!")

school = input("Enter the School Name: ")
print(f"======Welcome to {school}======")
stre = int(input("How many Entries: "))
sub = int(input("HOw many Subject each student is taking: "))
for i in range(sub):
     sub_name = input(f"Enter the Name of subject {i+1}: ")
     subjects.append(sub_name)
entries(stre, sub, subjects)
average(stre, subjects, student)
print("====Records====")
for i, (name, records) in enumerate(student.items()):
    print(f"\nStudent {i+1}: {name}")
    for record in records:
        print(f"  - {record['Subject']}: {record['Marks']} Marks")
print("====Averages====")
for i, (name, records) in enumerate(Average.items()):
    print(f"\nSubject {i+1}: {name}")
    for record in records:
        print(f"  - {record['Subject']}: {record['Average_Marks']} Marks, Total Students {record['Total_Students']}\n")
highest_and_lowest(stre, subjects, student)