import datetime

age = 22
name = 'Matt Sokol'
current_date = datetime.datetime.now()
year_of_birth = current_date.year - 22


print(f"OMG {name}, you are {age} years old so you were born in {year_of_birth}")

# Extension, prompt user for age, name etc. Take into account if the persons birthday
# has already happened this year or not

user_age = int(input("Please input your age. "))
user_name = input("Please input your full name. ")
user_year_of_birth = current_date.year - user_age


birthday = input("Enter your date of birth in the format dd/mm/yyyy. ")
bday = datetime.datetime.strptime(birthday, '%d/%m/%Y')
# user_age_hours = current_date.hour - 15

print(f'Day: {bday.day}')
print(f'Month: {bday.month}')
print(f'Year: {bday.year}')

# This only takes the month into account
if current_date.month > bday.month:
    print("Hope your birthday this year was amazing!! ")
else:
    print("Only a couple of months left until your birthday! ")