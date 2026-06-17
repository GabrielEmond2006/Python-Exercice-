import sympy as sp

x = sp.symbols("x")
primitive = sp.integrate(x**3, x)

print("La primitive est :", primitive)