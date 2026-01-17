import requests

# Testing string outputs
print("\n")
print("Hello World!")
print("This is a test Python file.")

# Testing variables
first_name = "John"     #string
last_name = "Doe"      #string
user_age = 26           #int
is_logged_in = True     #boolean

# Testing functions
def greet(name):
    if name: # check if name is not empty
        print(f"Hello {name}!")
    else: # if name is empty
        print("Hello!")


def count_characters(full_name):
    return len(full_name)

# Call the function to test as outputs
print("\n")
greet(first_name + " " + last_name)
print(f"Total characters in full name: {count_characters(first_name + ' ' + last_name)}")
print("\n")