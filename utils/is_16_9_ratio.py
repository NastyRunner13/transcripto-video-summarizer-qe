import math

def is_16_9_ratio(size):
    width, height = size
    gcd = math.gcd(width, height)  # Calculate the greatest common divisor
    reduced_width = width // gcd   # Reduce width by dividing by GCD
    reduced_height = height // gcd # Reduce height by dividing by GCD
    return (reduced_width, reduced_height) == (16, 9)