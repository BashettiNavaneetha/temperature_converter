import tkinter as tk
from tkinter import messagebox

def convert_temperature():
    try:
        temp = float(entry_temp.get())
        if option_var.get() == "C to F":
            result = (temp * 9/5) + 32
            label_result.config(text=f"{result:.2f} °F")
        elif option_var.get() == "F to C":
            result = (temp - 32) * 5/9
            label_result.config(text=f"{result:.2f} °C")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

# Create the main window
root = tk.Tk()
root.title("Temperature Converter")

# Set window size
root.geometry("400x300")  # Width x Height
root.resizable(False, False) 

# Fonts
font_label = ("Arial", 14)
font_entry = ("Arial", 14)
font_button = ("Arial", 14)

# Entry for temperature
label_temp = tk.Label(root, text="Enter Temperature:")
label_temp.pack()
entry_temp = tk.Entry(root)
entry_temp.pack()

# Dropdown for conversion type
option_var = tk.StringVar(value="C to F")
dropdown = tk.OptionMenu(root, option_var, "C to F", "F to C")
dropdown.pack()

# Button to convert
btn_convert = tk.Button(root, text="Convert", command=convert_temperature)
btn_convert.pack()

# Label to display result
label_result = tk.Label(root, text="Result: ")
label_result.pack()

root.mainloop()
