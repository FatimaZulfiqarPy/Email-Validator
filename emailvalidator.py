import re
import tkinter as tk
from tkinter import messagebox

# Regex pattern for email validation
email_condition = r"^[a-zA-Z0-9]+[\._]?[a-zA-Z0-9]+[@]\w+[.]\w{2,}$"

# Function to validate email
def validate_email():
    user_email = entry.get()
    if re.fullmatch(email_condition, user_email):
        messagebox.showinfo("Result ✅", f"Valid Email: {user_email}")
    else:
        messagebox.showerror("Result ❌", f"Invalid Email: {user_email}")

# Tkinter window setup
root = tk.Tk()
root.title("Email Validator")
root.geometry("450x250")
root.config(bg="#f0f0f0")

# Heading label
heading = tk.Label(root, text="📧 Email Validator", font=("Arial", 18, "bold"), bg="#f0f0f0", fg="black")
heading.pack(pady=10)
heading.place(x=120,y=40)

# Input field
entry = tk.Entry(root, font=("Arial", 12), width=30)
entry.pack(pady=10)
entry.place(x=90,y=90)

# Validate button
btn = tk.Button(root, text="Validate Email", command=validate_email, font=("Arial", 14, "bold"), bg="#fbbf24", fg="white")
btn.pack(pady=10)
btn.place(x=150,y=130)

# Run the app
root.mainloop()
