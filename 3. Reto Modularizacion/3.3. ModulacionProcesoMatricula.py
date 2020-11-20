print("\n•••••••>Proceso de Matricula<•••••••")
class Matricula:
    def __init__(self, identificacion, nombre, edad, direccion, telefono, correo, estado):
        self.identificacion = identificacion
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.estado = estado

    def imprimirEstudiante(self):
        print("••••Datos del estudiante••••")
        print(f"-Identificacion: {self.identificacion}")
        print(f"-Nombre: {self.nombre}")
        print(f"-edad: {self.edad} anios")
        print(f"-direccion: {self.direccion}")
        print(f"-telefono: {self.telefono}")
        print(f"-correo: {self.correo}")
        print(f"-Estado: {self.estado}")

    def getNombre(self):
        return self.nombre
    def getEstado(self):
        return self.estado


class Cursos:
    def __init__(self, idCarrera, pregrado, cursosProg, horario, estado):
        self.idCarrera = idCarrera
        self.pregrado = pregrado
        self.cursosProg = cursosProg
        self.horario = horario
        self.estado = estado

    def imprimirCurso(self):
        print("••••Datos del Curso••••")
        print(f"-idCarrera: {self.idCarrera}")
        print(f"-pregrado: {self.pregrado}")
        print(f"-Cursos del programa: {self.cursosProg}")
        print(f"-horario: {self.horario}")
        print(f"-Estado del curso: {self.estado}")

    def activo(self,ActivoInactivo):
        self.ActivoInactivo = ActivoInactivo
        if self.ActivoInactivo.getEstado() == "Activo":
            print("Estudiante activo, puede matricular el curso")
        elif self.ActivoInactivo.getEstado() == "Inactivo":
            print("Estudiante Inactivo, no puede matricular el curso")
        else:
            print("Error, ingresa Activo/Inactivo")

    def cambiarCurso(self, newCurso, oldCurso):
        self.newCurso = newCurso
        self.oldCurso = oldCurso
        for x in range(len(cursosProg)):
            if cursosProg[x] == self.oldCurso:
                cursosProg[x] = newCurso
        print(f"Se cambiara el curso de '{oldCurso}' por '{newCurso}'")
        print(f"Cursos del programa actualizado :{cursosProg}")

    def cambiarHorario(self, newHorario):
        self.horario = newHorario
        print(f"El nuevo horario actualizado es a las {newHorario}")

    def cancelarCurso(self, cursoCancelado, Cnombre):
        self.cursoCancelado = cursoCancelado
        self.Cnombre = Cnombre
        print(f"El estudiante {self.Cnombre.getNombre()} ha cancelado el curso {self.cursoCancelado}")

    def inactivarSistema(self, InacNombre):
        self.InacNombre = InacNombre
        print(f"El estudiante {self.InacNombre.getNombre()} ha sido inhabilitado del sistema")


#•••••••Datos del estudiante•••••••")
matricula1 = Matricula(1554892, "Juanito Molina", 22, "Carre 10 sur 98", "3125489958", "Juanito@gmail.com", "Activo")
matricula1.imprimirEstudiante()
print("\n")
#•••••••Datos del CURSO•••••••")
cursosProg = (["Calculo Diferencial", "Programacion", "Analisis Geometrico"])
curso1 = Cursos("IM00198", "Ingenieria de Sistemas", cursosProg, "6:00am", "Activo")
#curso1.imprimirCurso()

print("••••••••••••••••••••••••••••")
curso1.activo(matricula1)
print("••••••••••••••••••••••••••••")
curso1.cambiarCurso("Fisica 1", "Calculo Diferencial")
print("••••••••••••••••••••••••••••")
curso1.cambiarHorario("8:00am")
print("••••••••••••••••••••••••••••")
curso1.cancelarCurso("Programacion", matricula1)
print("••••••••••••••••••••••••••••")
curso1.inactivarSistema(matricula1)
print("••••••••••••••••••••••••••••")

print("••••••••••••••••••••••••••••")
curso1.imprimirCurso()

print("\n Trabajo realizado por Juan Diego Salazar Gil")




