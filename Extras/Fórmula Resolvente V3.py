import math

abc = input("Valores de a, b e c (a b c)")
a, b, c = map(float, abc.split()) 

d= b**2 - 4*a*c
den = 2 * a

if d < 0:
    print("Sem raizes")
elif d == 0:
    x = -b / den
    print("x =", x)
else:
    Rt_d= int(math.sqrt(d))
    
    if Rt_d**2 == d:
        x1 = (-b + Rt_d) / den
        x2 = (-b - Rt_d) / den
        print("x1 =", x1)
        print("x2 =", x2)
    else:
        print("x1 = (" + str(-b) + " + √" + str(d) + ") / " + str(den))
        print("x2 = (" + str(-b) + " - √" + str(d) + ") / " + str(den))