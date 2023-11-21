import tkinter as tk
from tkinter import ttk

# Temperature conversions
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def celsius_to_kelvin(celsius):
    return celsius + 273.15

# Length conversions
def meters_to_feet(meters):
    return meters * 3.28084

def feet_to_meters(feet):
    return feet / 3.28084

def miles_to_kilometers(miles):
    return miles * 1.60934

def kilometers_to_miles(kilometers):
    return kilometers / 1.60934

def meters_to_centimeters(meters):
    return meters * 100

def centimeters_to_meters(centimeters):
    return centimeters / 100

# Weight conversions
def kilograms_to_pounds(kilograms):
    return kilograms * 2.20462

def pounds_to_kilograms(pounds):
    return pounds / 2.20462

def ounces_to_grams(ounces):
    return ounces * 28.3495

def grams_to_ounces(grams):
    return grams / 28.3495

def kilograms_to_grams(kilograms):
    return kilograms * 1000

def grams_to_kilograms(grams):
    return grams / 1000

class UnitConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Unit Converter")
        self.root.geometry("400x300")

        self.create_widgets()

    def create_widgets(self):
        # Title
        title_label = ttk.Label(self.root, text="Unit Converter", font=("Helvetica", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=10)

        # Conversion Category
        category_label = ttk.Label(self.root, text="Choose a conversion category:")
        category_label.grid(row=1, column=0, columnspan=2, pady=5)

        self.category_var = tk.StringVar()
        category_combobox = ttk.Combobox(self.root, textvariable=self.category_var,
                                         values=["Temperature", "Length", "Weight"],
                                         state="readonly")
        category_combobox.grid(row=2, column=0, columnspan=2, pady=5)
        category_combobox.set("Temperature")
        category_combobox.bind("<<ComboboxSelected>>", self.update_units)

        # Value
        value_label = ttk.Label(self.root, text="Enter the value:")
        value_label.grid(row=3, column=0, pady=5)

        self.value_var = tk.StringVar()
        self.value_entry = ttk.Entry(self.root, textvariable=self.value_var)
        self.value_entry.grid(row=3, column=1, pady=5)
        self.value_var.set("")

        # Source Unit
        source_label = ttk.Label(self.root, text="Source unit:")
        source_label.grid(row=4, column=0, pady=5)

        self.source_var = tk.StringVar()
        self.source_combobox = ttk.Combobox(self.root, textvariable=self.source_var, values=[], state="readonly")
        self.source_combobox.grid(row=4, column=1, pady=5)

        # Target Unit
        target_label = ttk.Label(self.root, text="Target unit:")
        target_label.grid(row=5, column=0, pady=5)

        self.target_var = tk.StringVar()
        self.target_combobox = ttk.Combobox(self.root, textvariable=self.target_var, values=[], state="readonly")
        self.target_combobox.grid(row=5, column=1, pady=5)

        # Convert Button
        convert_button = ttk.Button(self.root, text="Convert", command=self.convert)
        convert_button.grid(row=6, column=0, columnspan=2, pady=10)
        
        # Result
        self.result_var = tk.StringVar()
        result_label = ttk.Label(self.root, textvariable=self.result_var, font=("Helvetica", 12))
        result_label.grid(row=7, column=0, columnspan=2, pady=10)

        # Set focus to the value entry field
        self.value_entry.focus()

        # Initialize units based on the default category
        self.update_units(None)

    def update_units(self, event):
        category = self.category_var.get()

        if category == "Temperature":
            units = ["Celsius", "Fahrenheit", "Kelvin"]
        elif category == "Length":
            units = ["Meters", "Centimeters", "Feet", "Miles", "Kilometers"]
        elif category == "Weight":
            units = ["Kilograms", "Grams", "Pounds", "Ounces"]
        else:
            units = []

        self.source_var.set(units[0] if units else "")
        self.target_var.set(units[1] if len(units) > 1 else "")

        self.source_combobox["values"] = units
        self.target_combobox["values"] = units

        if units:
            self.source_combobox.set(units[0])
            self.target_combobox.set(units[1] if len(units) > 1 else "")

    def convert(self):
        try:
            value = float(self.value_var.get())
            source_unit = self.source_var.get()
            target_unit = self.target_var.get()

            conversion_function_name = f"{source_unit.lower()}_to_{target_unit.lower()}"
            conversion_function = globals().get(conversion_function_name)

            if conversion_function:
                result = conversion_function(value)
                self.result_var.set(f"{value} {source_unit} is equal to {result:.2f} {target_unit}.")
            else:
                self.result_var.set("Unsupported units.")

        except ValueError:
            self.result_var.set("Invalid input. Please enter a numeric value for the conversion.")

if __name__ == "__main__":
    root = tk.Tk()
    app = UnitConverterApp(root)
    root.mainloop()
