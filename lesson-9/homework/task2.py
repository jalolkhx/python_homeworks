import csv

# Step 1: Create grades.csv
with open("grades.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Subject", "Grade"])
    writer.writerows([
        ["Alice", "Math", 85],
        ["Bob", "Science", 78],
        ["Carol", "Math", 92],
        ["Dave", "History", 74]
    ])

# Step 2: Read data from grades.csv
grades = []
with open("grades.csv", mode="r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        row["Grade"] = int(row["Grade"])  # Convert grade to integer
        grades.append(row)

# Step 3: Calculate average grades
subject_grades = {}
for entry in grades:
    subject = entry["Subject"].strip()
    if subject not in subject_grades:
        subject_grades[subject] = []
    subject_grades[subject].append(entry["Grade"])

average_grades = {subject: sum(grades)/len(grades) for subject, grades in subject_grades.items()}

# Step 4: Write average_grades.csv
with open("average_grades.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Subject", "Average Grade"])
    for subject, avg in average_grades.items():
        writer.writerow([subject, round(avg, 1)])

print("average_grades.csv has been created successfully.")
