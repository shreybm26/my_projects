import tkinter as tk
from tkinter import ttk
import random
import string

def generate_password(length, use_uppercase, use_numbers, use_symbols):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_button_clicked():
    length = int(length_var.get())
    use_uppercase = uppercase_var.get()
    use_numbers = numbers_var.get()
    use_symbols = symbols_var.get()

    password = generate_password(length, use_uppercase, use_numbers, use_symbols)
    result_var.set(password)

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create and configure the main frame
main_frame = ttk.Frame(root, padding="10")
main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Length label and entry
length_label = ttk.Label(main_frame, text="Password Length:")
length_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
length_var = tk.StringVar()
length_entry = ttk.Entry(main_frame, textvariable=length_var, width=5)
length_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)
length_var.set("12")

# Complexity options
uppercase_var = tk.BooleanVar(value=True)
uppercase_check = ttk.Checkbutton(main_frame, text="Uppercase", variable=uppercase_var)
uppercase_check.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

numbers_var = tk.BooleanVar(value=True)
numbers_check = ttk.Checkbutton(main_frame, text="Numbers", variable=numbers_var)
numbers_check.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

symbols_var = tk.BooleanVar(value=True)
symbols_check = ttk.Checkbutton(main_frame, text="Symbols", variable=symbols_var)
symbols_check.grid(row=1, column=2, padx=5, pady=5, sticky=tk.W)

# Generate button
generate_button = ttk.Button(main_frame, text="Generate Password", command=generate_button_clicked)
generate_button.grid(row=2, column=0, columnspan=3, pady=10)

# Result label
result_var = tk.StringVar()
result_label = ttk.Label(main_frame, textvariable=result_var, font=("Courier", 12))
result_label.grid(row=3, column=0, columnspan=3, pady=10)

# Start the Tkinter event loop
root.mainloop()
