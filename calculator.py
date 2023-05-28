import tkinter as tk

def button_click(number):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(tk.END, current + str(number))

def button_clear():
    display.delete(0, tk.END)

def button_equal():
    try:
        expression = display.get()
        result = eval(expression)
        display.delete(0, tk.END)
        display.insert(tk.END, result)
    except Exception:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create the display
display = tk.Entry(root, width=25, justify=tk.RIGHT, font=("Arial", 12))
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create the number buttons
for i in range(9):
    button = tk.Button(root, text=str(i+1), padx=15, pady=10, font=("Arial", 12), command=lambda i=i: button_click(i+1))
    button.grid(row=i//3+1, column=i%3, padx=5, pady=5)

# Create the operator buttons
operators = ['+', '-', '*', '/']
for i, operator in enumerate(operators):
    button = tk.Button(root, text=operator, padx=15, pady=10, font=("Arial", 12), command=lambda operator=operator: button_click(operator))
    button.grid(row=i+1, column=3, padx=5, pady=5)

# Create the other buttons
button_zero = tk.Button(root, text='0', padx=15, pady=10, font=("Arial", 12), command=lambda: button_click(0))
button_zero.grid(row=4, column=0, padx=5, pady=5)

button_clear = tk.Button(root, text='C', padx=15, pady=10, font=("Arial", 12), command=button_clear)
button_clear.grid(row=4, column=1, padx=5, pady=5)

button_equal = tk.Button(root, text='=', padx=15, pady=10, font=("Arial", 12), command=button_equal)
button_equal.grid(row=4, column=2, padx=5, pady=5)

root.mainloop()
