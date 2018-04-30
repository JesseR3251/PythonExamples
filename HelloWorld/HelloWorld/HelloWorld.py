# String Variables
message = "Hello Miguel, did you put on deodorant?"
messageUpperCase = message.upper()
messageLowerCase = message.lower()
messageTitleCase = message.title()
messageWhiteSpace = "    Loads of   White Space "
# List Variable
employeeNames = ['Jesse','Miguel','Richard','Luis']

# Print Messages
print("This is a message in title case: \n" + messageTitleCase + "\n")
print("This is a message in upper case: \n" + messageUpperCase + "\n")
print("This is a message in lower case: \n" + messageLowerCase + "\n")

print("========================================================================= \n")

# White Space Stripping
print("Left Strip: " + messageWhiteSpace.lstrip() + "\n")
print("Right Strip: " + messageWhiteSpace.rstrip() + "\n")
print("Strip: " + messageWhiteSpace.strip() + "\n")

print("========================================================================= \n")

# Printing lists
print('List of employees: ' + str(employeeNames).strip('[]') + "\n")
# Adding to list
employeeNames.append('Richard')
# Printing new addition from the list
print('After appending Richard: ' + str(employeeNames).strip('[]') + "\n")
employeeNames.insert(1,'Kevin')
# Printing after adding Kevin to index 1 of the list.
print('Inserting Kevin to index 1: ' + str(employeeNames).strip('[]') + "\n")
del employeeNames[1]
# Deleting kevin from index 1 of the list
print('Deleting index 1: ' + str(employeeNames).strip('[]') + "\n")
employeeNames.pop()
print('Popping one name from the list: ' + str(employeeNames).strip('[]') + "\n")

print("========================================================================= \n")
# Sorting
print("Employee Names sorted \n")
# Sorted does not permenately change data
print(sorted(employeeNames))
# As shown here
print(employeeNames)
# You can also apply sorted in reverse too
print(sorted(employeeNames, reverse = True))
# The reverse will change the list permenately
employeeNames.reverse()
print(employeeNames)
# Here is the sort that will bring the list to it's original state
employeeNames.sort()
print(employeeNames)
# Sort in reverse
employeeNames.sort(reverse = True)
print(employeeNames)
# Len function will return the length of the list
print("There are " + len(employeeNames) + " in the employeeNames list" )

for employeeNames in 
