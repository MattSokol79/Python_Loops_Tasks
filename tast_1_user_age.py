import datetime

# Asks for users age and calculates year of birth
age = int(input("Please input your age. "))
name = input("Please input your full name. ").title()
year_of_birth = datetime.datetime.now().year - age

print(f"Omg {name} you are {age} years old so you were born in {year_of_birth}")

birthday = input("Enter your date of birth in the format dd/mm/yyyy. ")
bday = datetime.datetime.strptime(birthday, '%d/%m/%Y')

# Fetches their age
real_age = datetime.datetime.now() - bday
real_age_hours = real_age * 24

print(real_age)
print(f"In hours, you are in fact {real_age_hours} hours long")
# print(f'Day: {bday.day}')
# print(f'Month: {bday.month}')
# print(f'Year: {bday.year}')

# This only takes the month into account
if datetime.datetime.now().month > bday.month:
    print("Hope your birthday this year was amazing!! ")
else:
    print("Only a couple of months left until your birthday! ")