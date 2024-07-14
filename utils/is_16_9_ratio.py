import math

def is_16_9_ratio(size):
    width, height = size
    gcd = math.gcd(width, height)
    reduced_width = width // gcd
    reduced_height = height // gcd
    return (reduced_width, reduced_height) == (16, 9)