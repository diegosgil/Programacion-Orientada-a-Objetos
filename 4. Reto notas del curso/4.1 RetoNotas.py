class NotasCurso:
    def __init__(self ,estudiante ,notas ,cantidad ,promedio):
        self.estudiante = estudiante
        self.notas = notas
        self.cantidad = cantidad
        self.promedio = promedio

    def llenarIdentificacion(self):
        for i in range(1 ,self.cantidad + 1):
            posicionId = "E" + str(i)
            self.estudiante[posicionId] = str(input(f"Ingresa el ID del estudiante {posicionId}: "))

    def llenarNotas(self):
        for i in range(1 ,self.cantidad + 1):
            posicionNota = "E" + (str(i))
            self.notas[posicionNota] = float(input(f"Ingresa la nota del estudiante {posicionNota}: "))

    def cambiarNotas(self ,diccNotas):
        changeNota = False
        while changeNota == False:
            changeNota = str(input("-Deseas cambiar alguna nota?. Oprime 'Y' en caso contrario oprime 'N': "))
            if changeNota == "Y" or changeNota == "y":
                posicionNota = str(input("Ingresa 'E' y el numero de estudiante --> 'E#': "))
                newNota = float(input("Ingrese la nueva nota: "))
                diccNotas[posicionNota] = newNota
                changeNota = True
            elif changeNota == "N" or changeNota == "n":
                print("••No deseo cambiar la nota••")
            else:
                print("Error al digitar, ingresa 'Y' o 'N' ")
            # endif
        # endwhile

    def promedioCurso(self):
        sumaNotas = 0
        prom = iter(self.notas)
        for i in (prom):
            sumaNotas = sumaNotas + self.notas[i]
        self.promedio = sumaNotas / self.cantidad
        print(f"El promedio del curso es: {self.promedio}")

    def existeIdentificacion(self ,idEstudiante):
        return idEstudiante in self.estudiante.values()

    def agregar(self):
        registrarnewEstudiante = False
        while registrarnewEstudiante == False:
            registrarnewEstudiante = str(input("-Deseas ingresar estudiante, oprime 'Y' en caso contrario oprime 'N': "))
            if registrarnewEstudiante == "Y" or registrarnewEstudiante == "y":
                registrarnewEstudiante = True
                print("••INGRESANDO ESTUDIANTE NUEVO••")
                if self.cantidad <= 50:
                    print(f"Actualmente hay {self.cantidad} estudiantes")
                    newEstudiante = "E" + str(self.cantidad + 1)
                    registrado = False
                    while registrado == False:
                        id = str(input(f"-Ingresa el ID del nuevo estudiante: "))
                        if not self.existeIdentificacion(id):
                            self.estudiante[newEstudiante] = id
                            print(f"Se agrego el estudiante Numero {newEstudiante}")
                            registrado = True
                            self.notas[newEstudiante] = float(input(f"-Ingresa la nota del nuevo estudiante: "))
                            self.cantidad = self.cantidad + 1
                        else:
                            print("ID ya se encuentra registrado, intenta nuevamente")
                        # endif
                else:
                    print(f"No se puede agregar un nuevo estudiante")
                # endif
            elif registrarnewEstudiante == "N" or registrarnewEstudiante == "n":
                print("••NO INGRESAR ESTUDIANTE NUEVO••")
            else:
                print("Error al digitar, ingresa 'Y' o 'N' ")
            # endif
        # endwhile

    def contadorEstudiantes(self):
        cantidad = iter(self.notas)
        mayores = 0
        for i in (cantidad):
            if self.notas[i] > self.promedio:
                mayores = mayores + 1
            # endif
        # endfor
        print(f"La cantidad de estudiantes que estan por encima del promedio son: {mayores}")

    def notaMayor(self):
        notaMay = 0
        mayor = iter(self.notas)
        for i in (mayor):
            if self.notas[i] > notaMay:
                notaMay = self.notas[i]
                posicionNota = i
            # endif
        # endfor
        print(f"La nota mayor es {self.notas[posicionNota]} del estudiante {posicionNota}")

    def getEstudiantes(self):
        return self.estudiante

    def getNotas(self):
        return self.notas


print("=========================================================")
print("••••••••••••••Informacion••••••••••••••")

ingresoEstudiante = False
while ingresoEstudiante == False:
    cantidadEstudiantes = int(input("Ingrese la cantidad de estudiantes: "))
    if cantidadEstudiantes <= 50:
        ingresoEstudiante = True
        print(f"El numero de estudiantes son {cantidadEstudiantes}")
    else:
        print(f"Sobrepasa el limite, maximo 50")

diccEstudiantes = {}
diccNotas = {}
promCurso = 0

n1 = NotasCurso(diccEstudiantes ,diccNotas ,cantidadEstudiantes ,promCurso)
n1.llenarIdentificacion()
n1.llenarNotas()

print("••••••••••••••••••••••••••••")
n1.cambiarNotas(diccNotas)
print("••••••••••••••••••••••••••••")
print(n1.getNotas())
n1.promedioCurso()
print("••••••••••••••••••")
n1.agregar()
print("••••••••••••••••••••••••••••")
n1.contadorEstudiantes()
print("••••••••••••••••••••••••••••")
n1.notaMayor()
print("•••••••••••••Resultado final•••••••••••••••")
print(n1.getNotas())
print("••••••••••••••••••••••••••••")
print(n1.getEstudiantes())

print("Trabajo presentado por Juan Diego Salazar Gil")