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