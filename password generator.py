import tkinter as tk
from tkinter import ttk
import random
import string

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Password Length:")
        self.label.pack(pady=5)
        self.length_entry = tk.Entry(self.root, width=5)
        self.length_entry.pack(pady=5)
        self.length_entry.insert(0, "12")
        self.generate_button = tk.Button(self.root, text="Generate Password", command=self.generate_password)
        self.generate_button.pack(pady=10)
        self.password_text = tk.Text(self.root, height=2, width=30)
        self.password_text.pack(pady=5)
    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length <= 0:
                raise ValueError("Length must be positive")
        except ValueError as e:
            self.password_text.delete(1.0, tk.END)
            self.password_text.insert(tk.END, f"Error: {e}")
            return
        
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        
        self.password_text.delete(1.0, tk.END)
        self.password_text.insert(tk.END, password)

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()
