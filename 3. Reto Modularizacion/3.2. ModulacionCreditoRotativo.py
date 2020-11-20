print("\n•••••••>Credito Rotativo<•••••••")
class Tomador:
    def __init__(self, identificacion, nombre, direccion, correo, cupo, cuotas):
        self.identificacion = identificacion
        self.nombre = nombre
        self.direccion = direccion
        self.correo = correo
        self.cupo = cupo
        self.cuotas = cuotas

    def imprimirUsuario(self):
        print(f"-Identificacion {self.identificacion}")
        print(f"-Nombre: {self.nombre}")
        print(f"-Direccion: {self.direccion}")
        print(f"-Correo: {self.correo}")
        print(f"-Cupo Disponible: ${self.cupo}")
        print(f"-Numero de Cuotas: {self.cuotas}")

    def getCupo(self):
        return self.cupo
    def getCuota(self):
        return self.cuotas


class Credito:
    def __init__(self, credito, Ncupo):
        self.credito = credito
        self.Ncupo = Ncupo

    def imprimirCupoCredito(self):
        print(f"El cupo disponible es de ${self.Ncupo.getCupo()}")
        if self.credito > self.Ncupo.getCupo():
            print(f"Compra rechazada, el cupo disponible no es suficiente")
        else:
            print(f"Compra Realizada por ${self.credito}, cupo restante ${self.Ncupo.getCupo() - self.credito}")

    def getCredito(self):
        return self.credito


class Compra:
    def __init__(self, Ccredito, Ccuota, Ccupo):
        self.Ccredito = Ccredito
        self.Ccuota = Ccuota
        self.Ccupo = Ccupo

    def imprimirCompra(self):
        print(f"El numero de cuotas son {self.Ccuota.getCuota()}")
        valorCredito = self.Ccredito.getCredito() / self.Ccuota.getCuota()
        if self.Ccredito.getCredito() > self.Ccupo.getCupo():
            print(f"Saldo insuficiente")
        elif self.Ccredito.getCredito() < self.Ccupo.getCupo():
            print(f"La compra de ${self.Ccredito.getCredito()}, se difiere en {self.Ccuota.getCuota()} cuotas de ${round(valorCredito, 2)}")


print("\n•••••••Datos del tomador•••••••")
tomador1 = Tomador("1011254659", "Pepito Perez", "Calle 10 sur 80A", "PepitoPerez@gmail.com", 1000, 7)
tomador1.imprimirUsuario()
print("••••••••••••••")
credito1 = Credito(900, tomador1)
credito1.imprimirCupoCredito()
print("••••••••••••••")
compra1 = Compra(credito1, tomador1, tomador1)
compra1.imprimirCompra()


print("\n Trabajo realizado por Juan Diego Salazar Gil")
