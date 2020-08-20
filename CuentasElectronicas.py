##Espacio de clases

class Cuenta:
    def __init__(self, titular):
        self.titular = titular
        self.cantidad = 0
    
    def ingresar(self, cantidad):
        
        if cantidad > 0:
            cantidad = cantidad
            self.cantidad = cantidad + self.cantidad
        else:
            print("Ingrese una cantidad validad")
    
    def retirar(self, cantidad):
        cantidad = cantidad
        self.cantidad -= cantidad
    
    def mostrar(self):
        print("{} {}".format(self.titular, self.cantidad))

    def __repr__(self):
        return ("{} {}".format(self.titular, self.cantidad))

class Cuenta_joven(Cuenta):
    def __init__(self, titular, edad):
        self.titular = titular
        self.edad = edad
        self.cantidad = 0
        self.bonificacion = 0,10
        
    def esTitularValido(self):
        if self.edad >= 18 and self.edad <= 25:
            return True
    
    def retirar(self):
        if self.esTitularValido():
            Cuenta.retirar()
        else:
            print("Usted no puede retirar dinero, su cuenta no es valida")
    
    def mostrar(self):
        print("Cuenta joven, {}, con una bonificacion de 10%".format(self.titular))


##Espacio de funciones
def menu():
    print("*" *30)
    print("     Bienvenido a su cuenta")
    print("*" *30)
    print("-" *30)
    print("-----------Opciones-----------")
    print("-" *30)

    print("1)- Ingresar dinero")
    print("2)- Retirar dinero")
    print("3)- Mostrar cuenta")
    print("4)- salir")
    print("-" *30)

    opcion = 0
    while opcion != 4:
        opcion = (int(input("ingrese una opcion: ")))
        if opcion == 1:
            cuenta.ingresar(float(input("Ingrese cantidad: ")))
        elif opcion == 2:
            cuenta.retirar(float(input("Ingrese cantidad: ")))
        elif opcion == 3:
            cuenta.mostrar()
        elif opcion == 4:
            print("Gracias por usar nuestro servicio")
##Espacio principal

cuenta = Cuenta("Caza Diego")
menu()
