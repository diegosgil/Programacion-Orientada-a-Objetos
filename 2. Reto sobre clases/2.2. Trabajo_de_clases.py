print("==============Retos cobre clases==============\n")

print("=======Compra=======\n")
class Compra:
    pass

    def __init__(self, precioUnitario, cantidadUnidades, descuento, iva):
        self.precioUnitario = precioUnitario
        self.cantidadUnidades = cantidadUnidades
        self.descuento = descuento
        self.iva = iva

    def pagoComprador(self):
        return self.precioUnitario * self.cantidadUnidades

    def cobroIVA(self):
        valorIva = (self.precioUnitario * self.cantidadUnidades) * self.iva
        #valorIva = ValorIva + (self.precioUnitario * self.cantidadUnidades)
        return valorIva

    def total(self):
        descuento =  (self.precioUnitario * self.cantidadUnidades) * self.iva
        descuento = (self.cantidadUnidades * self.precioUnitario) + descuento
        descuento = descuento * self.descuento
        return descuento

pagoTotal = Compra(1500, 40, 15/100 , 18/100)   #precio, unidades, descuento, iva
print(f"El cliente pago un total de ${pagoTotal.pagoComprador()} por {pagoTotal.cantidadUnidades} unidades")
print(f"El total cobrado por IVA fue de ${pagoTotal.cobroIVA()}")
print("El descuento aplicado fue de {}".format(pagoTotal.total()))
print("--- Gracias por la compra ---")
print("")
print("--"*80)
print("")

print("=======Barcos=======\n")
class Barco:
    pass

    def __init__(self, colorBarco, banderaBarco, tonelajeBarco, velocidadBarco, matriculaBarco):
        self.colorBarco = colorBarco
        self.banderaBarco = banderaBarco
        self.tonelajeBarco = tonelajeBarco
        self.velocidadBarco = velocidadBarco
        self.matriculaBarco = matriculaBarco

    def imprimir(self):
        print("Conozco un barco de color {} con bandera {} de {} toneladas de una velocidad maxima y su matricula es {}".format(self.colorBarco, self.banderaBarco, self.tonelajeBarco, self.velocidadBarco, self.matriculaBarco))

colorBarco = str(input("Ingrese el color del barco: "))
banderaBarco = str(input("Ingrese la bandera del barco: "))
tonelajeBarco = float(input("Ingrese el tonelaje del barco: "))
velocidadBarco = float(input("Ingrese la velocidad maxima del barco: "))
matriculaBarco = str(input("Ingrese la matricula del barco: "))
print("")
barco = Barco(colorBarco, banderaBarco, tonelajeBarco, velocidadBarco, matriculaBarco)
print(barco.imprimir())
print("")
print("--"*80)
print("")

print("=======Tienda en Linea=======\n")
class Tienda:
    def __init__(self, disponible, nombre, precio, descuento):
        self.disponible = disponible
        self.nombre = nombre
        self.precio = precio
        self.descuento = descuento

    def disponibilidad(self):
        if (self.disponible == True):
            print("El producto esta disponible")
        else:
            print("El producto no esta disponible")
        #endif

    def eliminarProductos(self):
        print(f"Ha sido eliminando el producto {pedirProduct}")

    def cambioNombre(self, nombre):
        self.nombre = nombre
        print(f"El nuevo nombre del producto es {self.nombre}")

    def cambioPrecio(self, precio):
        self.precio = precio
        print(f"El nuevo precio del producto es {self.precio}")

    def calculoDescuento(self, descuento):
        bonoDescuento = self.precio * descuento / 100
        return bonoDescuento

    def imprimirProducto(self):
        print(f"Tengo el producto {self.nombre} a {self.precio}")

pedirProduct = input("Ingresa el producto deseado: ")
productor1 = Tienda(True, pedirProduct, 1500, 5)
print("")
productor1.disponibilidad()
productor1.imprimirProducto()
print("")
newNombre = str(input("Ingresa el nuevo nombre del producto: "))
productor1.cambioNombre(newNombre)
productor1.imprimirProducto()
print("")
newPrecio = float(input("Ingresa el nuevo precio del producto: "))
productor1.cambioPrecio((newPrecio))
print("")
newDescuento = int(input("Ingresa el descuento: "))
productor1.imprimirProducto()

bonoDescuento = productor1.calculoDescuento(newDescuento)
if (bonoDescuento == 0):
    print("No tiene descuento")
# return 0o
elif (bonoDescuento > 0 and bonoDescuento <= newPrecio):
    print(f"El descuento es de {bonoDescuento}")
else:
    print("Error al digitar")

productor1.eliminarProductos()
print("Proceso Finalizado")
print("Trabajo realizado por Juan Diego Salazar Gil")




