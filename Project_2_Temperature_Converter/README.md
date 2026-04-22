# Temperature Converter

A command-line temperature conversion tool that converts between different temperature scales. This project demonstrates mathematical calculations, user input handling, and conditional logic in Python.

## Features

- Convert between Celsius, Fahrenheit, and Kelvin (basic version)
- Convert between Celsius, Fahrenheit, Kelvin, and Rankine (enhanced version)
- Precise calculations with 2 decimal places
- Input validation for temperature units
- User-friendly command-line interface

## Files

- `main.py` - Basic version supporting Celsius, Fahrenheit, and Kelvin
- `exercise.py` - Enhanced version with additional Rankine scale support
- `README.md` - This documentation file

## Requirements

- Python 3.x

## Temperature Scales Supported

- **Celsius (°C)** - Common metric temperature scale
- **Fahrenheit (°F)** - Imperial temperature scale used in the US
- **Kelvin (K)** - Absolute temperature scale starting from absolute zero
- **Rankine (°R)** - Absolute temperature scale using Fahrenheit degrees (enhanced version only)

## How to Run

### Basic Version (Celsius, Fahrenheit, Kelvin)
```bash
python main.py
```

### Enhanced Version (All four scales)
```bash
python exercise.py
```

## Usage Examples

### Basic Version
```
Enter the temperature value: 25
Enter the initial unit(C/K/F): c
Enter the unit you want to convert it to(C/K/F): f
25.00°C = 77.00°F
```

### Enhanced Version
```
Enter the temperature value: 100
Enter the initial unit(C/K/F/R): c
Enter the unit you want to convert it to(C/K/F/R): r
100.00°C = 671.67R
```

## Conversion Formulas

### Celsius Conversions
- °C to °F: `(°C × 9/5) + 32`
- °C to K: `°C + 273.15`
- °C to °R: `(°C + 273.15) × 9/5`

### Fahrenheit Conversions
- °F to °C: `(°F - 32) × 5/9`
- °F to K: `(°F - 32) × 5/9 + 273.15`
- °F to °R: `°F + 459.67`

### Kelvin Conversions
- K to °C: `K - 273.15`
- K to °F: `(K - 273.15) × 9/5 + 32`
- K to °R: `K × 9/5`

### Rankine Conversions (Enhanced Version Only)
- °R to °C: `(°R × 5/9) - 273.15`
- °R to °F: `°R - 459.67`
- °R to K: `°R × 5/9`

## Learning Objectives

This project demonstrates:
- Mathematical formula implementation
- User input validation and error handling
- Conditional statements (if/elif/else)
- String formatting with f-strings
- Floating-point arithmetic and precision
- Command-line interface design

## Error Handling

The program includes basic input validation:
- Accepts numeric temperature values
- Recognizes unit abbreviations (c, f, k, r)
- Displays "Invalid Input" for unrecognized units
- Handles same-unit conversions (no conversion needed)