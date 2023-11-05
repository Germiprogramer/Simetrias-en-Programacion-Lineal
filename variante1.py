#Variante general

# Importar el módulo SymPy
import sympy as sym
from sympy import symbols
from sympy.plotting import plot

f1 = "8-x" 
f2 = "18-3*x"

#las z son las funciones objetivo, despejamos la diversion y damos los valores que queramos a la z
Z1 = "(12-2*x)"


x = symbols('x')

p = plot(f1, f2, Z1,(x, -15, 15))