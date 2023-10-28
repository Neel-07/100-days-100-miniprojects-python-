import os
import tkinter as tk
from tkinter import filedialog

def rename_files():
    selected_dir = filedialog.askdirectory(title="Select Directory")
    if selected_dir:
        new_prefix = prefix_entry.get()
        new_suffix = suffix_entry.get()

        for filename in os.listdir(selected_dir):
            if filename.startswith(new_prefix) and filename.endswith(new_suffix):
                continue  # Skip already renamed files
            file_path = os.path.join(selected_dir, filename)
            new_name = f"{new_prefix}{filename}{new_suffix}"
            new_path = os.path.join(selected_dir, new_name)
            os.rename(file_path, new_path)

        result_label.config(text="Files successfully renamed!")

# Create the main window
root = tk.Tk()
root.title("File Renamer Tool")

# Create and pack GUI elements
frame = tk.Frame(root, padx=10, pady=10)
frame.pack(padx=10, pady=10)

prefix_label = tk.Label(frame, text="Prefix:")
prefix_label.grid(row=0, column=0, sticky="w")

prefix_entry = tk.Entry(frame)
prefix_entry.grid(row=0, column=1)

suffix_label = tk.Label(frame, text="Suffix:")
suffix_label.grid(row=1, column=0, sticky="w")

suffix_entry = tk.Entry(frame)
suffix_entry.grid(row=1, column=1)

rename_button = tk.Button(frame, text="Rename Files", command=rename_files)
rename_button.grid(row=2, column=0, columnspan=2)

result_label = tk.Label(frame, text="")
result_label.grid(row=3, column=0, columnspan=2)

root.mainloop()
