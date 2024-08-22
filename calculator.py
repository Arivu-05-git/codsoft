import tkinter as tk
def click_button(value):
    current = str(entry.get())
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + value)
def clear_entry():
    entry.delete(0, tk.END)
def evaluate_expression():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
root = tk.Tk()
root.title("Simple Calculator")
entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4)
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0, 4) ]
for (text, row, col, *args) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, width=5, height=2, command=evaluate_expression)
    elif text == 'C':
        btn = tk.Button(root, text=text, width=5, height=2, command=clear_entry)
    else:
        btn = tk.Button(root, text=text, width=5, height=2, command=lambda t=text: click_button(t))
    btn.grid(row=row, column=col, columnspan=args[0] if args else 1)
root.mainloop()
