import random
import tkinter as tk
import math
import secrets

root = tk.Tk()


bag = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$"
def roll_again():
    new_gen = secrets.choice(bag)
    for i in range(40):
        new_gen = new_gen + secrets.choice(bag)
        
    
    label.config(text=f"{new_gen}")
def copy_paste():
    current_password = label.cget("text")
    root.clipboard_clear()          
    root.clipboard_append(f"{current_password}")




label = tk.Label(root, text=f"Press reroll to be given 40 digit code")
button = tk.Button(root, text=f"Reroll", command=roll_again)
button_paste = tk.Button(root, text=f"Copy", command=copy_paste)
label.pack()
button.pack()
button_paste.pack()


root.mainloop()