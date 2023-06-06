# A python script to connect to a db abd create a table and perform CRUD operations. Modify the script and call the functions accordingly to make changes to the db.
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Create a table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT
    )
''')
conn.commit()

# Function to insert a new user
def create_user(id, name, email):
    cursor.execute('INSERT INTO users (id, name, email) VALUES (?, ?, ?)', (id, name, email))
    conn.commit()
    print("User created successfully!")

# Function to retrieve all users
def read_users():
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    for user in users:
        print(user)

# Function to retrieve a user by ID
def search_user(id):
    cursor.execute('SELECT * FROM users WHERE id = ?', (id,))
    user = cursor.fetchone()
    if user:
        print(user)
    else:
        print("User not found!")

# Function to update a user by ID
def update_user(id, name, email):
    cursor.execute('UPDATE users SET name = ?, email = ? WHERE id = ?', (name, email, id))
    conn.commit()
    print("User updated successfully!")

# Function to delete a user by ID
def delete_user(id):
    cursor.execute('DELETE FROM users WHERE id = ?', (id,))
    conn.commit()
    print("User deleted successfully!")

# Example usage
create_user(1, "John Doe", "john@example.com")
create_user(2, "Jane Smith", "jane@example.com")
read_users()
search_user(1)
update_user(2, "Jane Johnson", "jane.johnson@example.com")
delete_user(1)
read_users()

# Close the database connection
conn.close()
