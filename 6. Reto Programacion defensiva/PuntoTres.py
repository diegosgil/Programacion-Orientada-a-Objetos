class Encuesta:
    def __init__(self):
        self.placa = []
        self.tipo = []
        self.capKilos = []
        self.velocidad = []
        self.dia = []

    def validarPlaca(self):
        "Este metodo valida la placa"
        while (True):
            try:
                lista = ["a", "b", "c", "d", "e", "f","g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q",
                         "r", "s", ",t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F","G", "H", "I",
                         "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
                          "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-"]
                numPlaca = str(input("Ingresa la placa: "))
                for placa in range(0, len(numPlaca)):
                    validar = False
                    for buscarLetraNum in range(0, len(lista)):
                        if numPlaca[placa] == lista[buscarLetraNum]:
                            validar = True
                    if validar == False:
                        raise ValueError
                self.placa.append(numPlaca)
                print(f"-Placa: {numPlaca.upper()}")
                break
            except ValueError:
                print("Error!, ingresa correctamente la placa. ")

    def validarTipo(self):
        "Este metodo valida el tipo de vehiculo"
        while (True):
            try:
                lista = ["a", "b", "c", "d", "e", "f","g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q",
                         "r", "s", ",t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F","G", "H", "I",
                         "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
                          "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-"]
                tipoVehiculo = input("Ingrese el tipo de vehiculo: ")
                for tipo in range(0, len(tipoVehiculo)):
                    validar = False
                    for buscarLetras in range(0, len(lista)):
                        if tipoVehiculo[tipo] == lista[buscarLetras]:
                            validar = True
                    if validar == False:
                        raise ValueError
                self.tipo.append(tipoVehiculo)
                print(f"-Tipo: {tipoVehiculo.capitalize()}")
                break
            except ValueError:
                print("Error!, ingresa el tipo de vehiculo correctamente.")

    def validarCapacidadVehicular(self):
        "Este metodo valida el numero de la cuenta"
        while (True):
            try:
                lista = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ",", "."]
                cargaKilos = str(input("Ingresa la capacidad del vehiculo: "))
                for kilos in range(0, len(cargaKilos)):
                    validar = False
                    for buscarNum in range(0, len(lista)):
                        if cargaKilos[kilos] == lista[buscarNum]:
                            validar = True
                    if validar == False:
                        raise ValueError
                self.capKilos.append(cargaKilos)
                print(f"-Capacidad de carga: {cargaKilos} kilos")
                break
            except ValueError:
                print("Error!, ingresa nuevamente la capacidad vehicular")

    def validarVelocidad(self):
        "Este metodo valida la velocidad del vehiculo"
        while (True):
            try:
                velocidad = float(input("Ingrese el promedio de velocidad con el que conduces: "))
                if velocidad <= 90:
                    print("Velocidad moderada")
                elif velocidad >90 and velocidad <140:
                    print("Alta velocidad")
                else:
                    print("Exceso de velocidad")
                print(f"-Velocidad: {round(velocidad)} k/h")
                break
            except ValueError:
                print("Error!, ingresa nuevamente la velocidad promedio (solamente numeros)")

    def validarDia(self):
        """Este metodo valida que el dia ingresado exista"""
        while (True):
            try:
                lista = ["lunes" ,"Lunes" ,"martes" ,"Martes" ,"miércoles" ,"Miércoles" ,
                         "miercoles" ,"Miercoles" ,"jueves" ,"Jueves" ,"viernes" ,"Viernes" ,
                         "sabado" ,"Sabado" ,"sábado" ,"Sábado" ,"domingo" ,"Domingo"]
                diaIngresar = input("Ingrese el dia presente: ")
                if diaIngresar in lista:
                    self.dia.append((diaIngresar))
                    print(f"Dia: {diaIngresar.capitalize()}")
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Error!, el dia ingresado no existe.")

print("••••••Encuesta de movilidad••••••\n")
e1 = Encuesta()
e1.validarPlaca()
e1.validarTipo()
e1.validarCapacidadVehicular()
e1.validarVelocidad()
e1.validarDia()


