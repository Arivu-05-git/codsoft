import tkinter as tk
from tkinter import ttk, messagebox

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")

        # Initialize the contact dictionary
        self.contacts = {}

        # Create and place the widgets
        self.create_widgets()

    def create_widgets(self):
        # Labels and entries for contact details
        tk.Label(self.root, text="Name:").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(self.root, text="Phone:").grid(row=1, column=0, padx=10, pady=5)
        tk.Label(self.root, text="Email:").grid(row=2, column=0, padx=10, pady=5)
        tk.Label(self.root, text="Address:").grid(row=3, column=0, padx=10, pady=5)

        self.name_var = tk.StringVar()
        self.phone_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.address_var = tk.StringVar()

        self.name_entry = tk.Entry(self.root, textvariable=self.name_var, width=40)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)
        
        self.phone_entry = tk.Entry(self.root, textvariable=self.phone_var, width=40)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5)
        
        self.email_entry = tk.Entry(self.root, textvariable=self.email_var, width=40)
        self.email_entry.grid(row=2, column=1, padx=10, pady=5)
        
        self.address_entry = tk.Entry(self.root, textvariable=self.address_var, width=40)
        self.address_entry.grid(row=3, column=1, padx=10, pady=5)

        # Buttons
        tk.Button(self.root, text="Add Contact", command=self.add_contact).grid(row=4, column=0, padx=10, pady=10)
        tk.Button(self.root, text="Update Contact", command=self.update_contact).grid(row=4, column=1, padx=10, pady=10)
        tk.Button(self.root, text="Delete Contact", command=self.delete_contact).grid(row=5, column=0, padx=10, pady=10)
        tk.Button(self.root, text="Search Contact", command=self.search_contact).grid(row=5, column=1, padx=10, pady=10)
        
        # Search bar
        tk.Label(self.root, text="Search by name or phone:").grid(row=6, column=0, padx=10, pady=5)
        self.search_var = tk.StringVar()
        self.search_entry = tk.Entry(self.root, textvariable=self.search_var, width=40)
        self.search_entry.grid(row=6, column=1, padx=10, pady=5)
        tk.Button(self.root, text="Search", command=self.search_contact).grid(row=6, column=2, padx=10, pady=10)

        # Listbox to display contacts
        self.contact_listbox = tk.Listbox(self.root, width=60, height=15)
        self.contact_listbox.grid(row=7, column=0, columnspan=3, padx=10, pady=10)
        self.contact_listbox.bind('<<ListboxSelect>>', self.on_listbox_select)

    def add_contact(self):
        name = self.name_var.get()
        phone = self.phone_var.get()
        email = self.email_var.get()
        address = self.address_var.get()
        
        if not name or not phone or not email or not address:
            messagebox.showwarning("Input Error", "All fields must be filled out.")
            return

        if name in self.contacts:
            messagebox.showwarning("Duplicate Contact", "Contact with this name already exists.")
            return

        self.contacts[name] = {"phone": phone, "email": email, "address": address}
        self.update_contact_list()
        self.clear_entries()

    def update_contact(self):
        name = self.name_var.get()
        phone = self.phone_var.get()
        email = self.email_var.get()
        address = self.address_var.get()
        
        if not name or not phone or not email or not address:
            messagebox.showwarning("Input Error", "All fields must be filled out.")
            return

        if name not in self.contacts:
            messagebox.showwarning("Contact Not Found", "Contact with this name does not exist.")
            return

        self.contacts[name] = {"phone": phone, "email": email, "address": address}
        self.update_contact_list()
        self.clear_entries()

    def delete_contact(self):
        selected = self.contact_listbox.curselection()
        if not selected:
            messagebox.showwarning("Selection Error", "No contact selected.")
            return

        name = self.contact_listbox.get(selected[0])
        del self.contacts[name]
        self.update_contact_list()
        self.clear_entries()

    def search_contact(self):
        search_query = self.search_var.get().lower()
        if not search_query:
            messagebox.showwarning("Input Error", "Search query cannot be empty.")
            return

        search_results = [name for name in self.contacts if search_query in name.lower() or search_query in self.contacts[name]["phone"].lower()]
        
        if not search_results:
            messagebox.showinfo("No Results", "No contacts found matching the search query.")
            return
        
        self.contact_listbox.delete(0, tk.END)
        for name in search_results:
            self.contact_listbox.insert(tk.END, name)

    def on_listbox_select(self, event):
        selected = self.contact_listbox.curselection()
        if selected:
            name = self.contact_listbox.get(selected[0])
            contact = self.contacts[name]

            self.name_var.set(name)
            self.phone_var.set(contact["phone"])
            self.email_var.set(contact["email"])
            self.address_var.set(contact["address"])

    def update_contact_list(self):
        self.contact_listbox.delete(0, tk.END)
        for name in self.contacts:
            self.contact_listbox.insert(tk.END, name)

    def clear_entries(self):
        self.name_var.set("")
        self.phone_var.set("")
        self.email_var.set("")
        self.address_var.set("")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()

