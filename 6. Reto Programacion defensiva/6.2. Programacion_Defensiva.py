###############################PUNTO 1###################################
class Registro:
    def __init__(self):
        self.identificacion = []
        self.nombre = []
        self.correo = []
        self.pais = []
        self.ciudad = []
        self.codigoPostal = []

    def validarIdentificacion(self):
        "Ese metodo valida la identificacion que sea de tipo entero"
        while (True):
            try:
                id = int(input("Ingrese su identificacion: "))
                newId = int(id)
                self.identificacion.append(id)
                print(f"-Identificacion: {newId}")
                break
            except ValueError:
                print("Incorrecto!, ingresa nuevamente la identificacion")

    def validarNombre(self):
        "Ese metodo valida el nombre que sea tipo string"
        while (True):
            try:
                lista = ["a", "b", "c", "d", "e", "f","g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q",
                         "r", "s", ",t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F","G", "H", "I",
                         "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " "]
                nombre = str(input("Ingresa su nombre: "))
                for name in range(0, len(nombre)):
                    validar = False
                    for buscarLetra in range(0, len(lista)):
                        if nombre[name] == lista[buscarLetra]:
                            validar = True
                    if validar == False:
                        raise ValueError
                self.nombre.append(nombre)
                print(f"-Nombre: {nombre.title()}")
                break
            except ValueError:
                print("Error!, ingresa nuevamente el nombre")

    def validarCorreo(self):
        "Ese metodo valida el correo electronico"
        while (True):
            try:
                lista = ["a", "b", "c", "d", "e", "f","g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q",
                         "r", "s", ",t", "u", "v", "w", "x", "y", "z", ".", "-", "_", "@", "1", "2", "3", "4", "5",
                         "6", "7", "8", "9", "0", "A", "B", "C", "D", "E", "F","G", "H", "I", "J", "K", "L", "M", "N",
                         "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "hotmail", "gmail", "yahoo",
                         "msn", "outlook"]
                correo = str(input("Ingrese su correo electronico: "))
                if "@" in correo:
                    for recorreCorreo in range(0, len(correo)):
                        validar = False
                        for buscarLetras in range(0, len(lista)):
                            if correo[recorreCorreo] == lista[buscarLetras]:
                                validar = True
                        if validar == False:
                            raise ValueError
                    self.correo.append(correo)
                    print(f"-Correo: {correo.lower()}")
                    break
                else:
                    print("No se encontro el '@' ")
            except ValueError:
                print("Error!, ingresa nuevamente el correo")

    def validarPais(self):
        "Ese metodo valida el pais"
        while (True):
            try:
                lista = ["a", "b", "c", "d", "e", "f","g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q",
                         "r", "s", ",t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F","G", "H", "I",
                         "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " "]
                pais = str(input("Ingrese el pais: "))
                for recorrerPais in range (0, len(pais)):
                    validar = False
                    for buscarLetras in range (0, len(lista)):
                        if pais[recorrerPais] == lista[buscarLetras]:
                            validar =True
                    if validar == False:
                        raise ValueError
                self.pais.append(pais)
                print(f"-Pais: {pais.capitalize()}")
                break
            except ValueError:
                print("Error!, ingresa nuevamente el pais")

    def validarCiudad(self):
        "Este metodo valida la ciudad"
        while (True):
            try:
                lista = ["a", "b", "c", "d", "e", "f","g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q",
                         "r", "s", ",t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F","G", "H", "I",
                         "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " "
                         "á", "é", "í", "ó", "ú"]
                ciudad = str(input("Ingrese la ciudad: "))
                for recorrerCiudad in range (0, len(ciudad)):
                    validar = False
                    for buscarLetras in range (0, len(lista)):
                        if ciudad[recorrerCiudad] == lista[buscarLetras]:
                            validar =True
                    if validar == False:
                        raise ValueError
                self.ciudad.append(ciudad)
                print(f"-Ciudad: {ciudad.capitalize()}")
                break
            except ValueError:
                print("Error!, ingresa nuevamente la ciudad")

    def validarCodigoPostal(self):
        "Este metodo valida el codigo postal de Colombia"
        try:
            codigoPostal = int(input("Ingrese el codigo postal de Colombia: "))
            while codigoPostal != 57:
                codigoPostal = int(input("Ingrese el codigo postal de Colombia: "))
            self.codigoPostal.append(codigoPostal)
            print(f"-Codigo postal: +{codigoPostal}")
        except ValueError:
            print("Error!, el codigo postal para Colombia no coincide")

print("••••••Registrar pagina en internet••••••\n")
r1 = Registro()
r1.validarIdentificacion()
r1.validarNombre()
r1.validarCorreo()
r1.validarPais()
r1.validarCiudad()
r1.validarCodigoPostal()



#######################################PUNTO 2#############################################
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


###################################PUNTO 3########################################

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