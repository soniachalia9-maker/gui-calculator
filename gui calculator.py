import tkinter as tk
from tkinter import messagebox

# ---------------- Functions ----------------
def button_click(value):
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)   # simple for beginners
        clear()
        entry.insert(0, result)
    except:
        messagebox.showerror("Error", "Invalid Calculation")
        clear()

# ---------------- Main Window ----------------
root = tk.Tk()
root.title("GUI Calculator")
root.geometry("320x420")
root.resizable(False, False)

# ---------------- Display ----------------
entry = tk.Entry(
    root,
    font=("Arial", 20),
    borderwidth=5,
    relief="ridge",
    justify="right"
)
entry.pack(fill="both", padx=10, pady=10)

# ---------------- Buttons ----------------
frame = tk.Frame(root)
frame.pack()

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(
            frame, text=text, width=5, height=2,
            font=("Arial", 14), bg="green", fg="white",
            command=calculate
        )
    else:
        btn = tk.Button(
            frame, text=text, width=5, height=2,
            font=("Arial", 14),
            command=lambda t=text: button_click(t)
        )
    btn.grid(row=row, column=col, padx=5, pady=5)

# Clear Button
clear_btn = tk.Button(
    frame, text="C", width=22, height=2,
    font=("Arial", 14), bg="red", fg="white",
    command=clear
)
clear_btn.grid(row=5, column=0, columnspan=4, pady=5)

# ---------------- Run App ----------------
root.mainloop()
