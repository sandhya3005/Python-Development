import tkinter as tk
from tkinter import messagebox

# Function to display a message box with form data
def submit_form():
    name = entry_name.get()
    email = entry_email.get()
    age = entry_age.get()
    
    if name and email and age:
        messagebox.showinfo("Form Submission", f"Name: {name}\nEmail: {email}\nAge: {age}")
    else:
        messagebox.showwarning("Input Error", "All fields are required!")

# Create the main window
root = tk.Tk()
root.title("Registration Form")

# Create and place labels and entry widgets for the form
tk.Label(root, text="Name").grid(row=0, column=0, padx=10, pady=5)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Email").grid(row=1, column=0, padx=10, pady=5)
entry_email = tk.Entry(root)
entry_email.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Age").grid(row=2, column=0, padx=10, pady=5)
entry_age = tk.Entry(root)
entry_age.grid(row=2, column=1, padx=10, pady=5)

# Create and place the submit button
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=3, columnspan=2, pady=10)

# Run the application
root.mainloop()