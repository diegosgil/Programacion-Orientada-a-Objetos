class Articulo:
    def __init__(self, peso, altura):
        """Este es el metodo inicializador de la clase de Articulo, recibe los parametros
        peso: contiene el peso del articulo
        altura: contiene la altura del articulo"""
        self.peso = peso
        self.altura = altura

    def cambiarPeso(self, newPeso):
        """Este metodo permite cambiar el peso al articulo"""
        self.peso = newPeso

    def mostrarPeso(self):
        """Este metodo permite mostrar el peso del articulo"""
        return self.peso