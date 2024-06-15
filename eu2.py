import tkinter as tk
from tkinter import ttk

def kg_to_lbs(kg):
    return kg * 2.20462

# Define the conversion functions
def convert_kg_to_lbs():
    try:
        kg = float(entry_weight.get())
        lbs = kg_to_lbs(kg)
        label_result.config(text=f"{kg} kg is equal to {lbs:.2f} lbs")
    except ValueError:
        label_result.config(text="Please enter a valid number")

def convert_pounds_to_kg():
    try:
        pounds = float(entry_weight.get())
        kg = pounds / 2.20462
        label_result.config(text=f"{pounds} pounds is equal to {kg:.2f} kilograms")
    except ValueError:
        label_result.config(text="Please enter a valid number")

def convert_dollar_to_euro():
    try:
        dollar = float(entry_weight.get())
        euro = dollar * 0.93
        label_result.config(text=f"{dollar} dollars is equal to {euro:.2f} euros")
    except ValueError:
        label_result.config(text="Please enter a valid number")

def convert_euro_to_dollar():
    try:
        euro = float(entry_weight.get())
        dollar = euro / 0.93
        label_result.config(text=f"{euro} euros is equal to {dollar:.2f} dollars")
    except ValueError:
        label_result.config(text="Please enter a valid number")

def convert_leu_to_dollar():
    try:
        leu = float(entry_weight.get())
        dollar = leu / 17.76
        label_result.config(text=f"{leu} leu is equal to {dollar:.2f} dollars")
    except ValueError:
        label_result.config(text="Please enter a valid number")

def convert_dollar_to_leu():
    try:
        dollar = float(entry_weight.get())
        leu = dollar * 17.76
        label_result.config(text=f"{dollar} dollars is equal to {leu:.2f} leu")
    except ValueError:
        label_result.config(text="Please enter a valid number")

root = tk.Tk()
root.title("American to European Converter")
root.geometry("1366x768")

style = ttk.Style()
style.configure("TButton", font=("Helvetica", 16), background="lightblue")  # Change the font and background color of the button
style.configure("TCombobox", font=("Helvetica", 16))  # Change the font of the combobox
style.configure("TLabel", font=("Helvetica", 16))  # Change the font of the label


# Create and place the components in the window
frame = ttk.Frame(root, padding="10")
frame_width = 475  # Set this to the width of the frame
frame_height = 250  # Set this to the height of the frame
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (frame_width / 2)
y = (screen_height / 2) - (frame_height / 2)

# Place the frame
frame.place(x=x, y=y)

# Create and place the components in the window
label_weight = ttk.Label(frame, text="Enter the number:")
label_weight.grid(row=0, column=0, padx=5, pady=5)

entry_weight = ttk.Entry(frame, width=20)
entry_weight.grid(row=0, column=1, padx=5, pady=5)

# Create a dropdown menu for selecting the conversion type
conversion_types = ["Kilograms to Pounds", "Pounds to Kilograms", "Dollars to Euros","Euros to Dollars", "Leu to Dollars", "Dollars to Leu"]
combobox_conversion_type = ttk.Combobox(frame, values=conversion_types)
combobox_conversion_type.grid(row=1, column=0, columnspan=2, pady=10)

def convert():
    conversion_type = combobox_conversion_type.get()
    if conversion_type == "Kilograms to Pounds":
        convert_kg_to_lbs()
    elif conversion_type == "Pounds to Kilograms":
        convert_pounds_to_kg()
    elif conversion_type == "Euros to Dollars":
        convert_euro_to_dollar()
    elif conversion_type == "Dollars to Euros":
        convert_dollar_to_euro()
    elif conversion_type == "Leu to Dollars":
        convert_leu_to_dollar()
    elif conversion_type == "Dollars to Leu":
        convert_dollar_to_leu()

button_convert = ttk.Button(frame, text="Convert", command=convert)
button_convert.grid(row=2, column=0, columnspan=2, pady=10)

label_result = ttk.Label(frame, text="")
label_result.grid(row=3, column=0, columnspan=2, pady=5)

root.mainloop()
#