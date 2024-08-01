# importing the library
import tkinter as tk
# UI
root = tk.Tk()
root.title("Temperature Converter")

# FIRST READINGS IN FAHRENHEIT
label_fahrenheit = tk.Label(root, text="Fahrenheit:")
label_fahrenheit.pack()
entry_fahrenheit = tk.Entry(root, width=20)
entry_fahrenheit.pack()

# inaunda lable ta Celcius
label_celsius = tk.Label(root, text="Celsius:")
label_celsius.pack()
entry_celsius = tk.Entry(root, width=20)
entry_celsius.pack()

# FUNCTION TO CONVERT FAHRENHEIT TO CELCIUS
def convert_fahrenheit_to_celsius():
    fahrenheit = float(entry_fahrenheit.get())
    celsius = (fahrenheit - 32) * 5/9
    entry_celsius.delete(0, tk.END)
    entry_celsius.insert(0, str(round(celsius, 2)))

# CREATING TKINTER BUTTON
button_convert = tk.Button(root, text="Convert to Celsius", command=convert_fahrenheit_to_celsius)
button_convert.pack()

# CREATING MAIN LOOP
root.mainloop()