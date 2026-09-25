import math 

a = float(input("Valor de a: "))
b = float(input("Valor de b: "))
c = float(input("Valor de c: "))


Rt = math.sqrt(b**2 -4*a*c)

if Rt >0 :
    x1 = (-b + Rt) / 2*a 
    x2 = (-b - Rt) / 2*a
    print("x=",x1, "ou x=",x2)
else:
    print("Não tem nenhum zero")