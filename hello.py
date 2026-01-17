import requests as req
import pandas as pd
import beautifulsoup4 as bs4
import openai as ai
import python-dotenv as dotenv
import math
import numpy
import datetime

########################################## Basic Tests ##########################################

# Testing string outputs
print("\n")
print("Hello World!")
print("This is a test Python file.")

# Testing variables
first_name = "John"     #string
last_name = "Doe"      #string
user_age = 17           #int
is_logged_in = True     #boolean

# Testing data structures
# List of favorite agents in Valorant
favorite_agents = ["Jett", "Sage", "Phoenix", "Raze"]

# Dictionary of Valorant agent profile
agent_dictionary = {}

agent_profile = {
    "agent_name": "Jett",
    "role": "Duelist",
    "type": "Radiant",
    "best_with": ["Operator", "Vandal", "Sheriff"],
    "abilities": ["Cloudburst", "Updraft", "Tailwind", "Blade Storm"]
}

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

# Function to check if user can drive
def can_drive(age):
    if age >= 18:
        return True
    else:
        return False
    
# Function to test loops
def loop_test():
    for i in range(5):
        print(f"Loop iteration {i}")
    print("\n")

# Function to test data structure: list
def list_test(agents):
    print("Favorite Valorant Agents:")
    for agent in agents: # "agents" replaces range() method here
        print(f"- {agent}")
    print("\n")


########################################## Running tests ##########################################


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

# Test loop function
loop_test()

# Test list function
list_test(favorite_agents)