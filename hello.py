import requests

# Testing string outputs
print("\n")
print("Hello World!")
print("This is a test Python file.")

# Testing variables
first_name = "John"     #string
last_name = "Doe"      #string
user_age = 17           #int
is_logged_in = True     #boolean

# Testing functions
# Function to greet a user
def greet(name):
    if name: # check if name is not empty
        print(f"Hello {name}!")
    else: # if name is empty
        print("Hello!")

# Function to count characters in a string
def count_characters(full_name):
    return len(full_name)


def can_drive(age):
    if age >= 18:
        return True
    else:
        return False
    



# Call the function to test as outputs
print("\n")
greet(first_name + " " + last_name + "!")
print(f"Total characters in full name: {count_characters(first_name + ' ' + last_name)}")
print("\n")

# Check driving eligibility
if can_drive(user_age):
    print(f"{first_name} is eligible to drive.")
    print("\n")
else:
    print(f"{first_name} is not eligible to drive.")
    print("\n")