"""Se importa desde el archi 'NeveraOne' todos sus elementos"""

from Herencia.NeveraOne import *

"Se crea el objeto de la clase Nevera y se ingresa todos sus atributos"
n1 = Nevera(60, 1.70, "blanco", "Ovalada", 80, "Icasa")

print("••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••")
"Se imprime los valores que retorna el metodo 'MostrarPeso', 'MostrarColor', 'MostrarListros', 'MostrarMarca' "
print(f"Tengo una nevera {n1.mostrarMarca()}, color {n1.mostrarColor()} de {n1.mostrarLitros()} litros que pesa {n1.mostrarPeso()} kilos")

print("\n••••••••••••••••••••••••••••••Datos Actualizados••••••••••••••••••••••••••••••")
"Se cambio el valor del litro y del peso"
n1.cambiarLitros(60)
n1.cambiarPeso(50)

"Se imprime los valores actualizados que retornara el metodo mostrarLitros y mostrarPeso"
print(f"Tengo una nevera {n1.mostrarMarca()}, color {n1.mostrarColor()} de {n1.mostrarLitros()} litros que pesa {n1.mostrarPeso()} kilos")