import math

try:
    number = float(input("Enter a number: "))

    if number >= 0:
        sqrt_result = math.sqrt(number)
    else:
        sqrt_result = "Square root is not defined for negative numbers."

    if number > 0:
        log_result = math.log(number)
    else:
        log_result = "Logarithm is only defined for positive numbers."

    sine_result = math.sin(number)

    print(f"Square Root: {sqrt_result}")
    print(f"Logarithm: {log_result}")
    print(f"Sine: {sine_result}")

except ValueError:
    print("Invalid input. Please enter a numeric value.")
