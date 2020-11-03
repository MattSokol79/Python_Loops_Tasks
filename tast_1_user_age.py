import datetime
from datetime import date

# Ask user for details and calculate
age = int(input("What is your age? "))
name = input("What is your full name? ").title()
birthday = input("What is your birthday?\nFormat: dd/mm/yyyy. ")
bday = datetime.datetime.strptime(birthday, '%d/%m/%Y')
birth_year = date.today().year - age

print(f"Omg {name}, you are {age} years old so you were born in {birth_year}.")


# Extension - determining whether the user has already celebrated their birthday
today = date.today()
months_left = bday.month - today.month
days_left =  bday.day - today.day

if bday.month - today.month < 0 and bday.day - today.day < 0:
    print(f"{name}, hope you had a great birthday this year!")
else:
    print(f"{name} you only have {days_left} days and {months_left} months left until your birthday")

# Hours alive - difference between the current date and birthdate in seconds divided by 3600
age_hours = (today - bday.date()).total_seconds() / 3600
print(f"{name}, you are {int(age_hours)} hours old!!")