'''
An Expense Tracker application using Tkinter, a Python GUI library, and SQLite for database management.
How it works:

Database Initialization and Table Creation:

The code connects to an SQLite database file named expenses.db and creates a cursor to execute SQL queries.
It checks if the expenses table exists. If not, it creates the table with columns for id, date, category, description, and amount.
Tkinter Window Setup:

A Tkinter window is created with the title "Expense Tracker" and a size of 500x400 pixels. The background color is set to white.
Expense Entry Fields:

Several Tkinter labels and entry fields are created for entering expense details, including date, category, description, and amount.
Add Expense Function (add_expense()):

This function is called when the "Add Expense" button is clicked.
It retrieves the input values from the entry fields and inserts the expense into the expenses table in the database.
The input fields are cleared after adding the expense, and the expenses list is updated.
Delete Expense Function (delete_expense()):

This function is called when the "Delete Expense" button is clicked.
It retrieves the selected expense ID from the listbox or the id_entry field and deletes the corresponding expense from the database.
The input fields are cleared, and the expenses list is updated.
View Expenses Function (view_expenses()):

This function retrieves all expenses from the expenses table and displays them in the listbox.
The listbox is first cleared, and then each expense is inserted into the listbox as a formatted string.
Listbox and Buttons:

A listbox widget (expenses_list) is created to display the expenses.
Two buttons are created: "Add Expense" and "Delete Expense" to trigger the respective functions.
Application Execution:

The expenses list is initially set to display "No expenses".
The view_expenses() function is called to populate the listbox with existing expenses from the database.
The Tkinter event loop (window.mainloop()) starts, enabling the GUI to be interactive.
Database Connection Closing:

After the event loop ends, the database connection is closed.

'''

# import
import tkinter as tk
import sqlite3

def add_expense():
    # Get the input values
    
    # Insert the expense into the database using insert query
    
    # Clear the input fields


    # Update the expenses list


def delete_expense():
    # Get the selected expense ID from the listbox uncomment
    # selected_index = expenses_list.curselection()
    # if selected_index:
    #     selected_id = expenses_list.get(selected_index).split(" | ")[0]
    # else get it by id u can list
    # else:
    #     selected_id =id_entry.get()

    # Delete the expense from the database
    
    # also clear the entry field
    
    conn.commit()

        # Update the expenses list
    view_expenses()

def view_expenses():
    # Clear the expenses list

    # Retrieve all expenses from the database and fetch all

    # Display each expense in the listbox
    
# Create the main window

# Connect to the SQLite database

# Create the expenses table if it doesn't exist

conn.commit()

# Create the label and entry fields for adding expenses
# date_label = tk.Label(window, text="Date:", bg="white")
# date_label.pack()
# date_entry = tk.Entry(window)
# date_entry.pack()

# category_label = tk.Label(window, text="Category:", bg="white")
# category_label.pack()
# category_entry = tk.Entry(window)
# category_entry.pack()

# description_label = tk.Label(window, text="Description:", bg="white")
# description_label.pack()
# description_entry = tk.Entry(window)
# description_entry.pack()

# amount_label = tk.Label(window, text="Amount:", bg="white")
# amount_label.pack()
# amount_entry = tk.Entry(window)
# amount_entry.pack()

# # Create the button to add expenses
# add_button = tk.Button(window, text="Add Expense", command=add_expense, bg="green", fg="white")
# add_button.pack()

# id = tk.Label(window, text="Amount:", bg="white")
# id.pack()
# id_entry = tk.Entry(window)
# id_entry.pack()

# # Create the button to delete expenses
# delete_button = tk.Button(window, text="Delete Expense", command=delete_expense, bg="red", fg="white")
# delete_button.pack()

# # Create the listbox to display expenses
# expenses_list = tk.Listbox(window, width=50, height=15)
# expenses_list.pack(pady=20)

# # Center align the expenses list
# expenses_list.configure(justify=tk.CENTER)

# # Start with the expenses list empty
# expenses_list.insert(tk.END, "No expenses")

# Update the expenses list with the view_expense() call


# Start the Tkinter event loop

# Close the database connection
