from datetime import datetime

dob = input("Enter your date of birth (DD-MM-YYYY): ")
dob_date = datetime.strptime(dob, "%d-%m-%Y")

today = datetime.today()

age = today.year - dob_date.year

if (today.month, today.day) < (dob_date.month, dob_date.day):
    age -= 1

print("Your age is:", age)