import tkinter as tk
from tkinter import ttk
import ttkbootstrap as boot

from PIL import Image, ImageTk


root = boot.Style(theme="darkly").master

# row_0
image = Image.open("key.png").resize((160, 80))
photo = ImageTk.PhotoImage(image)
tk.Label(root, image=photo).grid(row=0, column=1)

# row_1
website = tk.StringVar()
website_label = ttk.Label(root, text="Website_Name")
website_entry = ttk.Entry(root, textvariable=website, width=30)
delete_button = ttk.Button(root, text="Delete", command=root.destroy, style="success.Outline.TButton")

# row_2
user = tk.StringVar()
user_label = ttk.Label(root, text="User_ID")
user_entry = ttk.Entry(root, textvariable=user, width=30)
generate_button = ttk.Button(root, text="Generate", command=root.destroy, style="success.Outline.TButton")

# row_3
length = tk.StringVar()
password_var = tk.StringVar()
password_label = ttk.Label(root, text="Your Password")
password_entry = ttk.Entry(root, textvariable=password_var, width=30)
length_combobox = ttk.Combobox(root, textvariable=length)
length_combobox["values"] = ("8", "10", "15", "20", "22")
length_combobox["state"] = "readonly"

# row_4
show_button = ttk.Button(root, text="Show Database", command=root.destroy)
save_button = ttk.Button(root, text="Save to Database", command=root.destroy, style="success.TButton")

# row_1_grid
website_label.grid(row=1, column=0, pady=10, sticky="w")
website_entry.grid(row=1, column=1, padx=10, pady=10)
length_combobox.grid(row=1, column=2, padx=10, pady=10, sticky="ew")

# row_2_grid
user_label.grid(row=2, column=0, pady=10, sticky="w")
user_entry.grid(row=2, column=1, padx=10, pady=10)
generate_button.grid(row=2, column=2, ipadx=40)

# row_3_grid
password_label.grid(row=3, column=0, sticky="w")
password_entry.grid(row=3, column=1, padx=10, pady=10, sticky="ew")
password_var.set("Password Shows Here")
length.set("Set the password length")

# row_4_grid
show_button.grid(row=4, column=0, ipadx=25, pady=10)
save_button.grid(row=4, column=1, ipadx=10)

root.mainloop()
