# Program to get Name, Age, House Number and Street Name from user and print it out in a sentence
# Pseudocode
# Get name from user and assign it to variable name
# Get age from user and assign it to variable age
# Get House number and assign it to House Number
# Get Street Name and assign it to Street Name
# Print out This is <name>. He is <age> years old and lives at <house number> and on <street name>
# Python Code below

#Get name from user and assign it to variable name
name = input("Enter your Name: ")

#Get age from user and assign it to variable age
age = input("Enter your age: ")

#Get house number from user and assign it to variable house_number
house_number = input("Enter your House Number: ")

#Get street name from user and assign it to variable street_name
street_name = input("Enter Street Name: ")

#Print the message This is <name> variable. He is <age> years old and lives at <house_number> on <street_name>
print("This is "+name+". He is "+age+" years old and lives at house number "+house_number+" on "+street_name+".")