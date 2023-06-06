'''
A pet adoption app where u create a backend with sqlite to add, check availablity and adopt pets. Run the app and interact with the gui.
'''
import tkinter as tk
from tkinter import ttk
import sqlite3
from tkinter import messagebox

# Create SQLite database connection
conn = sqlite3.connect("pets.db")
c = conn.cursor()

# Create pets table if it doesn't exist
c.execute("""
    CREATE TABLE IF NOT EXISTS pets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        type TEXT
    )
""")
conn.commit()

def add_pet():
    name = pet_name.get()
    age = pet_age.get()
    pet_type_value = pet_type.get()

    c.execute("INSERT INTO pets (name, age, type) VALUES (?, ?, ?)", (name, age, pet_type_value))
    conn.commit()

    pet_name.delete(0, tk.END)
    pet_age.delete(0, tk.END)
    pet_type.delete(0, tk.END)

    messagebox.showinfo("Congratulations!", "Pet added successfully!")

def adopt_pet():
    c.execute("SELECT * FROM pets")
    pets = c.fetchall()
    try:
        if len(pets) > 0:
            name = pet_name.get()
            c.execute('SELECT * from pets where name=?',(name,))
            curr = c.fetchone()
            age = curr[3]
            p_type = curr[2]
            c.execute("DELETE FROM pets WHERE name=?", (name,))
            conn.commit()

            available_pets.delete(0, tk.END)
            available_pets.insert(tk.END, f"Name: {name}, Age: {age}, Type: {p_type}")

            messagebox.showinfo("Congratulations!", "Pet adopted successfully!")
        else:
            available_pets.delete(0, tk.END)
            available_pets.insert(tk.END, "No pets available")
    except:
        available_pets.insert(tk.END, "Please enter the correct name")


def show_available_pets():
    c.execute("SELECT * FROM pets")
    pets = c.fetchall()

    available_pets.delete(0, tk.END)
    if len(pets) > 0:
        for pet in pets:
            pet_id = pet[0]
            pet_name = pet[1]
            pet_age = pet[2]
            pet_type = pet[3]
            available_pets.insert(tk.END, f"Name: {pet_name}, Age: {pet_age}, Type: {pet_type}")
    else:
        available_pets.insert(tk.END, "No pets available")

# Create the main window
root = tk.Tk()
root.title("Pet Adoption Center")
root.geometry("400x400")

# Create pet input fields
pet_name_label = ttk.Label(root, text="Pet Name:")
pet_name_label.pack()
pet_name = ttk.Entry(root)
pet_name.pack()

pet_age_label = ttk.Label(root, text="Pet Age:")
pet_age_label.pack()
pet_age = ttk.Entry(root)
pet_age.pack()

pet_type_label = ttk.Label(root, text="Pet Type:")
pet_type_label.pack()
pet_type = ttk.Combobox(root, values=["Dog", "Cat", "Rabbit"])
pet_type.pack()

add_pet_button = ttk.Button(root, text="Add Pet", command=add_pet)
add_pet_button.pack()

# Create available pets display
available_pets_label = ttk.Label(root, text="Available Pets:")
available_pets_label.pack()
available_pets = tk.Listbox(root, width=50, height=10)
available_pets.pack()

adopt_pet_button = ttk.Button(root, text="Adopt Pet", command=adopt_pet)
adopt_pet_button.pack()

show_available_pets_button = ttk.Button(root, text="Show Available Pets", command=show_available_pets)
show_available_pets_button.pack()

root.mainloop()

# Close the SQLite database connection
conn.close()
