'''
A pet adoption app where u create a backend with sqlite to add, check availablity and adopt pets.
'''
import sqlite3
from tkinter import *

# Database setup

# Create pets table

# Function to add a new pet to the database
def add_pet():
    # get name, pet_type, age, availability

    # exexcute a insert query to add the pet
    
    # commit
    
    # use result_label.config() to add text
    


# Function to search for available pets based on type
def search_pets():
    # get availabilty
    # exexcute a select query to get the pet by availability and type
    
    # commit
    
    # use result_label.config() to add text
    

# Function to adopt a pet
def adopt_pet():
    # get name, pet_type, age, availability

    # exexcute a delete query to delete the pet
    
    # commit
    
    # use result_label.config() to add text
    

# GUI setup
root = Tk()
root.title("Pet Adoption Center")

# add label and entry field for name

# add label and entry field for type

# add label and entry field for age

# add label and entry field for avialability

# add a button to add_pet with callback to add_pet and pack
add_button = 

# add a button to seacrh pet with callback to search_pet and pack
search_button = 

# add a button to adopt pet with callback to adopt_pet and pack

#add a result label

#run main loop

#close the connection to db
