from Herencia.ArticuloOne import *
"""Se importa el paquete 'ArticuloOne' con todos los elementos"""
class Electrodomestico(Articulo):
    def __init__(self, peso, altura, color, forma):
        """Se crea la clase 'Electredomestico' que hereda todos los atributos y metodos de la clase
        'Articulo' añadiendo los atributos color y forma y el metodo que se encarga de mostrar el valor del color"""
        Articulo.__init__(self, peso, altura)
        self.color = color
        self.forma = forma

    def mostrarColor(self):
        """Este metodo se encarga de retornar el valor que se guarda en el atributo color"""
        return self.color
