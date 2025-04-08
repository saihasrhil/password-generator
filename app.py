import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

def generate_password():
    length = int(length_entry.get())
    include_upper = upper_var.get()
    include_digits = digit_var.get()
    include_symbols = symbol_var.get()

    chars = string.ascii_lowercase
    if include_upper:
        chars += string.ascii_uppercase
    if include_digits:
        chars += string.digits
    if include_symbols:
        chars += string.punctuation

    if not chars:
        messagebox.showwarning("Warning", "Select at least one character type!")
        return

    password = ''.join(random.choice(chars) for _ in range(length))
    result_label.config(text=password)

def copy_password():
    password = result_label.cget("text")
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

# GUI setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.resizable(False, False)

tk.Label(root, text="Password Length:").pack(pady=5)
length_entry = tk.Entry(root)
length_entry.pack()
length_entry.insert(0, "12")

# Options
upper_var = tk.BooleanVar()
digit_var = tk.BooleanVar()
symbol_var = tk.BooleanVar()

tk.Checkbutton(root, text="Include Uppercase", variable=upper_var).pack()
tk.Checkbutton(root, text="Include Digits", variable=digit_var).pack()
tk.Checkbutton(root, text="Include Symbols", variable=symbol_var).pack()

tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)
result_label = tk.Label(root, text="", font=("Helvetica", 14))
result_label.pack(pady=5)

tk.Button(root, text="Copy to Clipboard", command=copy_password).pack(pady=10)

root.mainloop()
