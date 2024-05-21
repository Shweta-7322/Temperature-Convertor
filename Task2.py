# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

temperature = float(input("Enter the temperature value: "))

unit = input("Enter the unit of measurement (C for Celsius, F for Fahrenheit): ").strip().upper()

# Converting and displaying the temperature based on the unit
if unit == 'C':
    converted_temperature = celsius_to_fahrenheit(temperature)
    print(f"{temperature}°C is equal to {converted_temperature:.2f}°F")
elif unit == 'F':
    converted_temperature = fahrenheit_to_celsius(temperature)
    print(f"{temperature}°F is equal to {converted_temperature:.2f}°C")
else:
    print("Invalid unit of measurement. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
