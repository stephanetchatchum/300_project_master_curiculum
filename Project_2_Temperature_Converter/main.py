# Get the temperature value from the user and convert it to a float
temp = float(input("Enter the temperature value"))

# Get the original unit and normalize to lowercase (c, f, or k)
OG_unit = input("Enter the initial unit(C/K/F)").lower()

# Get the target unit and normalize to lowercase (c, f, or k)
FN_unit = input("Enter the unit you want to convert it to(C/K/F)").lower()

# --- Conversions from Celsius ---
if OG_unit == 'c':
    if FN_unit == 'f':
        FN_temp = temp * (9/5) + 32          # Celsius to Fahrenheit formula
        print(f"{temp:.2f}°C = {FN_temp:.2f}°F")
    elif FN_unit == 'k':
        FN_temp = temp + 273.15              # Celsius to Kelvin formula
        print(f"{temp:.2f}°C = {FN_temp:.2f}K")
    elif FN_unit == 'c':
        FN_temp = temp                       # Same unit, no conversion needed
        print(f"{temp:.2f}°C = {FN_temp:.2f}°C")

# --- Conversions from Fahrenheit ---
elif OG_unit == 'f':
    if FN_unit == 'c':
        FN_temp = (temp - 32) * (5/9)       # Fahrenheit to Celsius formula
        print(f"{temp:.2f}°F = {FN_temp:.2f}°C")
    elif FN_unit == 'k':
        FN_temp = (temp - 32) * (5/9) + 273.15  # Fahrenheit to Kelvin (via Celsius)
        print(f"{temp:.2f}°F = {FN_temp:.2f}K")
    elif FN_unit == 'f':
        FN_temp = temp                       # Same unit, no conversion needed
        print(f"{temp:.2f}°F = {FN_temp:.2f}°F")

# --- Conversions from Kelvin ---
elif OG_unit == 'k':
    if FN_unit == 'c':
        FN_temp = temp - 273.15             # Kelvin to Celsius formula
        print(f"{temp:.2f}°K = {FN_temp:.2f}°C")
    elif FN_unit == 'f':
        FN_temp = (temp - 273.15) * (9/5) + 32  # Kelvin to Fahrenheit (via Celsius)
        print(f"{temp:.2f}°K = {FN_temp:.2f}°F")
    elif FN_unit == 'k':
        FN_temp = temp                      # Same unit, no conversion needed
        print(f"{temp:.2f}K = {FN_temp:.2f}K")

# --- Handle any unrecognized unit input ---
else:
    print("Invalid Input")