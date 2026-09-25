from minicas import *

print("--- Divisor de Polinómios ---")
print("Introduzir de Menor potência para a maior.")
print("Exemplo: 2x^2 - 4 é [-4, 0, 2]")

n_input = input("Coeficientes Numerador (sep por espaço): ").split()
num = [float(x) for x in n_input]

d_input = input("Coeficientes Denominador (sep por espaço): ").split()
den = [float(x) for x in d_input]

quot, rem = poly_div(num, den)

print("\n" + "="*20)
print("Quociente:  " + poly_to_str(quot))
print("Resto: " + poly_to_str(rem))
print("="*20)
