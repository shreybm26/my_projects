import tkinter as tk

def update_display(value):
    current = display_var.get()
    if current == "0":
        display_var.set(value)
    else:
        display_var.set(current + value)

def perform_calculation():
    try:
        result = str(eval(display_var.get()))
        display_var.set(result)
    except:
        display_var.set("Error")

def clear_display():
    display_var.set("0")

# Create main window
root = tk.Tk()
root.title("Beautiful Calculator")

# Display
display_var = tk.StringVar()
display_var.set("0")
display = tk.Label(root, textvariable=display_var, font=("Helvetica", 24), anchor="e", padx=20, pady=20)
display.grid(row=0, column=0, columnspan=4)

# Button layout
button_texts = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

row_offset = 1
for text, row, col in button_texts:
    button = tk.Button(root, text=text, font=("Helvetica", 16), padx=20, pady=20, command=lambda t=text: update_display(t))
    button.grid(row=row + row_offset, column=col, sticky="nsew")

# Clear button
clear_button = tk.Button(root, text="C", font=("Helvetica", 16), padx=20, pady=20, command=clear_display)
clear_button.grid(row=5, column=0, sticky="nsew")

# Plus button
plus_button = tk.Button(root, text="+", font=("Helvetica", 16), padx=20, pady=20, command=lambda: update_display("+"))
plus_button.grid(row=5, column=1, sticky="nsew")

# Equal button
equal_button = tk.Button(root, text="=", font=("Helvetica", 16), padx=20, pady=20, command=perform_calculation)
equal_button.grid(row=5, column=2, columnspan=2, sticky="nsew")

# Configure grid rows and columns
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

# Start the GUI event loop
root.mainloop()
