class Retiro:
    def __init__(self):
        self.validacionTitular = []
        self.numCuenta = []
        self.valor = []

    def validarIdentificacion(self):
        while (True):
            try:
                titular = int(input("Ingrese la identificacion del titular: "))
                newTitular = int(titular)
                self.validacionTitular.append(id)
                print(f"-Identificacion del Titular: {newTitular}")
                break
            except ValueError:
                print("Incorrecto!, ingresa nuevamente la identificacion, tiene que ser numeros enteros")

    def validarNumeroDeCuenta(self):
        "Este metodo valida el numero de la cuenta"
        while (True):
            try:
                lista = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", " ", ".", "-"]
                numero = input("Ingresa el numero de cuenta: ")
                for num in range(0, len(numero)):
                    validar = False
                    for buscarNum in range(0, len(lista)):
                        if numero[num] == lista[buscarNum]:
                            validar = True
                    if validar == False:
                        raise ValueError
                self.numCuenta.append(numero)
                print(f"-Numero: {numero}")
                break
            except ValueError:
                print("Error!, ingresa nuevamente el numero de cuenta")

    def valorRetiro(self):
        """Este metodo valida que el numero ingresado sea un intere, devolviendo
         el monto retirado y lo que le queda en la cuenta"""
        while (True):
            try:
                retiro = int(input("Ingrese el monto que desea retirar: "))
                montoTotal = 8000000
                if retiro <= montoTotal:
                    Total = montoTotal - retiro
                    self.valor.append(retiro)
                    print(f"-Monto retirado: ${retiro}, te queda un total de ${Total}")
                    break
                else:
                    print("No es posible retirar, fondo insuficiente")
            except ValueError:
                print("Error!, Solamente numeros enteros")

print("••••••Retiro Cuenta de ahorros••••••\n")
rt1 = Retiro()
rt1.validarIdentificacion()
rt1.validarNumeroDeCuenta()
rt1.valorRetiro()