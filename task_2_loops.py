
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
for i in list_names:
    list_names_lower.append(i.lower())
print(list_names_lower)

# Iterate over the list of names to find if the number of letters is even or odd