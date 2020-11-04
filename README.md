# Tasks 1 and 2 - Loops
### Task 1 focuses on determining a users age  as well as birthyear. It heavily revolves around using the datetime module.
- Cool, we've used strings to make a program that made a welcome message. Now let's use some numerical types. Create program that calculates the year of birth.
Tasks define the variables age and name make a calculation for the year in which the person was born * print out "OMG <person>, you are <age> years old so you were born in <year>" with the correct values.
For the second part, prompt the user for input and re-assign the variable age and name figure out a way to account for if the persons birthday has already happened this year or not.
Extra go look into the library time print out the amount of hour this person has lived Acceptance Criteria program defines the variable age and name program prints the string "OMG <person>, you are <age> years old so you were born in <year>"

```python
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
# REQUIRES REFINEMENT
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
```

### Task 2 focuses on utilising loops such as if, elif, and while loops to answer different types of questions. Iterating  through sets of lists was a prominent feature
- Make a loop that says hello 10 times
- Create another loop with a range that
asks for names and appends to `list_names`
- Make a lopp that iterated over each name
in `list_names` and format all the names
into lowercase in a new variable 
`list_names_lower`
- Iterate over the list of values to find
if the number of letters within each name
is even or odd

```python
# Task - Loops and Lists
# Make a loop using range that says hello 10 times
for i in range(10):
    print("hello")



# Make a loop with a range that asks for names and appends to list_names
# title() was used to capitalise if name given in lower case
list_names = []
while True:
    name = input("Input your name, otherwise type Stop ").title()
    if name == 'Stop':
        break
    list_names.append(name)
print(list_names)



# Make a loop that iterated over each name in the above list_names and format it
# into lowercase in a new variable called list_names_lower
list_names_lower = []
for name in list_names:
    list_names_lower.append(name.lower())
print("The names in lowercase:", list_names_lower)

# Iterate over the list of names to find if the number of letters is even or odd
even_list = []
for name in list_names_lower:
    if len(name) % 2 == 0:
        print(f"{name} contains an even number of letters")
    else:
        print(f"{name} contains an odd number of letters")
```