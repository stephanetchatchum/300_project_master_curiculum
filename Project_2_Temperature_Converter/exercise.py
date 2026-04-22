# Get the temperature value from the user and convert it to a float
temp = float(input("Enter the temperature value"))

# Get the original unit and normalize to lowercase (c, f, k, or r)
OG_unit = input("Enter the initial unit(C/K/F/R)").lower()

# Get the target unit and normalize to lowercase (c, f, k, or r)
FN_unit = input("Enter the unit you want to convert it to(C/K/F/R)").lower()

# --- Conversions from Celsius ---
if OG_unit == 'c':
    if FN_unit == 'f':
        FN_temp = temp * (9/5) + 32              # Celsius to Fahrenheit formula
        print(f"{temp:.2f}°C = {FN_temp:.2f}°F")
    elif FN_unit == 'k':
        FN_temp = temp + 273.15                  # Celsius to Kelvin: add 273.15
        print(f"{temp:.2f}°C = {FN_temp:.2f}K")
    elif FN_unit == 'r':
        FN_temp = (temp + 273.15) * (9/5)        # Celsius to Rankine: convert to Kelvin first, then scale
        print(f"{temp:.2f}°C = {FN_temp:.2f}R")
    elif FN_unit == 'c':
        FN_temp = temp                           # Same unit, no conversion needed
        print(f"{temp:.2f}°C = {FN_temp:.2f}°C")

# --- Conversions from Fahrenheit ---
elif OG_unit == 'f':
    if FN_unit == 'c':
        FN_temp = (temp - 32) * (5/9)            # Fahrenheit to Celsius formula
        print(f"{temp:.2f}°F = {FN_temp:.2f}°C")
    elif FN_unit == 'k':
        FN_temp = (temp - 32) * (5/9) + 273.15  # Fahrenheit to Kelvin: convert to Celsius first, then add 273.15
        print(f"{temp:.2f}°F = {FN_temp:.2f}K")
    elif FN_unit == 'r':
        FN_temp = temp + 459.67                  # Fahrenheit to Rankine: add 459.67
        print(f"{temp:.2f}°F = {FN_temp:.2f}R")
    elif FN_unit == 'f':
        FN_temp = temp                           # Same unit, no conversion needed
        print(f"{temp:.2f}°F = {FN_temp:.2f}°F")

# --- Conversions from Kelvin ---
elif OG_unit == 'k':
    if FN_unit == 'c':
        FN_temp = temp - 273.15                  # Kelvin to Celsius: subtract 273.15
        print(f"{temp:.2f}K = {FN_temp:.2f}°C")
    elif FN_unit == 'f':
        FN_temp = (temp - 273.15) * (9/5) + 32  # Kelvin to Fahrenheit: convert to Celsius first, then scale
        print(f"{temp:.2f}K = {FN_temp:.2f}°F")
    elif FN_unit == 'r':
        FN_temp = temp * (9/5)                   # Kelvin to Rankine: multiply by 9/5
        print(f"{temp:.2f}K = {FN_temp:.2f}R")
    elif FN_unit == 'k':
        FN_temp = temp                           # Same unit, no conversion needed
        print(f"{temp:.2f}K = {FN_temp:.2f}K")

# --- Conversions from Rankine ---
elif OG_unit == 'r':
    if FN_unit == 'c':
        FN_temp = (temp * (5/9)) - 273.15        # Rankine to Celsius: scale to Kelvin first, then subtract 273.15
        print(f"{temp:.2f}R = {FN_temp:.2f}°C")
    elif FN_unit == 'f':
        FN_temp = temp - 459.67                  # Rankine to Fahrenheit: subtract 459.67
        print(f"{temp:.2f}R = {FN_temp:.2f}°F")
    elif FN_unit == 'k':
        FN_temp = temp * (5/9)                   # Rankine to Kelvin: multiply by 5/9
        print(f"{temp:.2f}R = {FN_temp:.2f}K")
    elif FN_unit == 'r':
        FN_temp = temp                           # Same unit, no conversion needed
        print(f"{temp:.2f}R = {FN_temp:.2f}R")

# --- Handle any unrecognized unit input ---
else:
    print("Invalid Input")