import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Password Length:").grid(row=0, column=0, padx=10, pady=10)
        self.length_var = tk.IntVar(value=12)
        self.length_entry = tk.Entry(self.root, textvariable=self.length_var, width=5)
        self.length_entry.grid(row=0, column=1, padx=10, pady=10)
        self.generate_button = tk.Button(self.root, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=1, column=0, columnspan=2, pady=10)
        self.password_text = tk.Text(self.root, height=2, width=30)
        self.password_text.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
        self.password_text.config(state=tk.DISABLED)

    def generate_password(self):
        try:
            length = self.length_var.get()
            if length <= 0:
                raise ValueError("Length must be positive")
        except ValueError as e:
            self.show_error_message(f"Error: {e}")
            return
        
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        self.password_text.config(state=tk.NORMAL)
        self.password_text.delete(1.0, tk.END)
        self.password_text.insert(tk.END, password)
        self.password_text.config(state=tk.DISABLED)

    def show_error_message(self, message):
        messagebox.showerror("Error", message)

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()
