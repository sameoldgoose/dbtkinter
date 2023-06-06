# A PYTHON TYPING GAME WHERE U WORDS COME UP ON SCREEN AND YOU HAVE TO TYPE THEM AND PRESS ENTER AFTER TYPING. IF YOU TYPE THE RIGHT WORD U GET A POINT. Run the game and press start game to start playing.
import tkinter as tk
import random
import time
import string

def start_game():
    global score, end_time
    score = 0
    end_time = time.time() + duration
    next_word()

def next_word():
    entry.delete(0, tk.END)
    if time.time() < end_time:
        word = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(random.randint(3,10)))
        label.config(text=word)

def check_word(event):
    global score
    if time.time() < end_time:
        user_input = entry.get().strip()
        if user_input.lower() == label.cget("text").lower():
            score += 1
        next_word()

root = tk.Tk()
root.title("Typing Game")

words = ["apple", "banana", "cherry", "orange", "watermelon"]
duration = 30

score = 0
end_time = 0

label = tk.Label(root, text="", font=("Arial", 24))
label.pack(pady=20)

entry = tk.Entry(root, font=("Arial", 18))
entry.bind("<Return>", check_word)
entry.pack()

start_button = tk.Button(root, text="Start Game", font=("Arial", 16), command=start_game)
start_button.pack(pady=20)

score_label = tk.Label(root, text="Score: 0", font=("Arial", 16))
score_label.pack()

def update_score():
    score_label.config(text=f"Score: {score}")
    score_label.after(100, update_score)

update_score()

root.mainloop()
