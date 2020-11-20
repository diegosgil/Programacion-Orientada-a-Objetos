from Herencia.ElectrodomesticoOne import *
"""Se importa el paquete 'ElectrodomesticoOne' con todos los elementos"""

class Nevera(Electrodomestico):
    def __init__(self, peso, altura, color, forma, litros, marca):
        """Se cre la clase 'Nevera' que hereda todos los atributos y metodos de la clase
        'Electrodomestico' añadiendo los atributos lietros y marca, y el metodo que se encarga
        de retornar los valores de litros y marca. Ademas de cambiar el valor de litros"""
        super().__init__(peso, altura, color, forma)
        self.litros = litros
        self.marca = marca

    def cambiarLitros(self, newLitros):
        """Metodo encargado de cambiar el litro"""
        self.litros = newLitros

    def mostrarLitros(self):
        """Metodo encargado de retornar los litros"""
        return self.litros

    def mostrarMarca(self):
        """Metodo encargado de retornar la marca"""
        return self.marca