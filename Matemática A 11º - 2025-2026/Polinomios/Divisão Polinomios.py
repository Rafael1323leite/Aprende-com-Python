from minicas import *

print("--- Polynomial Divider ---")
print("Enter coefficients from LOWEST power to HIGHEST.")
print("Example: 2x^2 - 4 is [-4, 0, 2]")

n_input = input("Numerator coeffs (sep by space): ").split()
num = [float(x) for x in n_input]

d_input = input("Denominator coeffs (sep by space): ").split()
den = [float(x) for x in d_input]

quot, rem = poly_div(num, den)

print("\n" + "="*20)
print("Quotient:  " + poly_to_str(quot))
print("Remainder: " + poly_to_str(rem))
print("="*20)