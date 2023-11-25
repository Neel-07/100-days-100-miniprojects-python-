import tkinter as tk
from tkinter import messagebox

def convert_to_decimal():
    roman = entry_roman.get().upper()
    try:
        decimal = roman_to_decimal(roman)
        label_decimal.config(text=f"Decimal: {decimal}")
    except ValueError:
        messagebox.showerror("Error", "Invalid Roman numeral!")

def convert_to_roman():
    decimal = int(entry_decimal.get())
    try:
        roman = decimal_to_roman(decimal)
        label_roman.config(text=f"Roman: {roman}")
    except ValueError:
        messagebox.showerror("Error", "Invalid decimal number!")

def roman_to_decimal(roman):
    roman_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    decimal = 0
    prev_value = 0

    for numeral in reversed(roman):
        current_value = roman_dict[numeral]
        if current_value >= prev_value:
            decimal += current_value
        else:
            decimal -= current_value
        prev_value = current_value

    return decimal

def decimal_to_roman(decimal):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4, 1
    ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman_num = ''
    i = 0
    while decimal > 0:
        for _ in range(decimal // val[i]):
            roman_num += syb[i]
            decimal -= val[i]
        i += 1
    return roman_num

# Create GUI
root = tk.Tk()
root.title("Roman <-> Decimal Converter")

label_roman = tk.Label(root, text="Enter Roman Numeral:")
entry_roman = tk.Entry(root)
convert_button = tk.Button(root, text="Convert to Decimal", command=convert_to_decimal)
label_decimal = tk.Label(root, text="Decimal: ")

label_decimal_res = tk.Label(root, text="Enter Decimal Number:")
entry_decimal = tk.Entry(root)
convert_button_res = tk.Button(root, text="Convert to Roman", command=convert_to_roman)
label_roman_res = tk.Label(root, text="Roman: ")

label_roman.grid(row=0, column=0, padx=5, pady=5)
entry_roman.grid(row=0, column=1, padx=5, pady=5)
convert_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
label_decimal.grid(row=2, column=0, columnspan=2)

label_roman_res.grid(row=3, column=0, padx=5, pady=5)
entry_decimal.grid(row=3, column=1, padx=5, pady=5)
convert_button_res.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
label_decimal_res.grid(row=5, column=0, columnspan=2)

root.mainloop()
