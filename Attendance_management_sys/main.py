import datetime

students = {
    "1": "Monika",
    "2": "nikita",
    "3": "Gita",
    "4": "Samu",
    "5": "Renuka",
    "6": "Akanksha",
    "7": "Mayuri",
    "8": "Tanu",
    "9": "Pratiksha",
    "10": "Pratiksha",
    "11": "Rutuja",
    "12": "Nikita",
    "13": "Aarti",
    "14": "Ishwari",
    "15": "Payal",
    "16": "Apurva",
    "17": "Bhakti",
    "18": "Sakshi",
    "19": "Gitanjali"
}

attendance = {}

def mark_attendance(roll_no):
    if roll_no in students:
        if roll_no in attendance:
            print("Attendance Already marked")
        else:
            now = datetime.datetime.now()
            date_time = now.strftime("%d-%m-%y %I:%M %p")

            attendance[roll_no] = {
                "name": students[roll_no],
                "time": date_time
            }

            print("Attendance is marked for", students[roll_no])
    else:
        print("Invalid roll number")

while True:
    print("\n--- Attendance Management System ---")
    roll = input("Enter roll number: ")
    mark_attendance(roll)

    choice = input("Do you want to mark another attendance? (yes/no): ")
    if choice.lower() == "no":
        break

print("\n=== Final Attendance List ===")
for roll_no, data in attendance.items():
    print(
        "Roll No:", roll_no, 
        "Student Name:",  data["name"], 
        "Date & Time:", data["time"]
    )

print("\nTotal Present Students:", len(attendance))
 
