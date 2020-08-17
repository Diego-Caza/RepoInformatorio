##ESPACIO DE CLASES

class Libro:
    def __init__ (self, titulo, autor, num_pag, calificacion=0):
        self.titulo = titulo
        self.autor = autor
        self.num_pag = num_pag
        self.calificacion = calificacion
        
    def modificar(self, libro):
        self.titulo = self.titulo
        self.autor = self.autor
        self.num_pag = self.num_pag
        self.calificacion = self.calificacion
    
    def mostrar(self):
        print("{} {} {} {}".format(self.titulo, self.autor, self.num_pag, self.calificacion))
       
    def __repr__(self):
        return("{} {} {} {}".format(self.titulo, self.autor, self.num_pag, self.calificacion))
    
    def __gt__(self, libro):
        return self.calificacion > libro.calificacion


class ConjuntoLibros:
    def __init__(self):
        self.listado = list()
        
    
    def agregar_libro(self, libro):
        self.listado.append(libro)
    
        
    def mostrar_lista(self):
        print(self.listado)
    
    def eliminar(self, forma):
        for i in self.listado:
            if i.titulo == forma or i.autor == forma:
                self.listado.remove(i)


##ESPACIO DE FUNCIONES

def insertar_libro():
    
    titulo = (input("Ingresar titulo del libro: ")) 
    autor = (input("Ingrese el nombre del autor: "))
    num_pag = (input("Ingrese el numero de paginas del libro: "))
    calificacion = (int(input("Ingrese el puntaje que le da al libro, escala de 0 a 10")))
    conjunto.agregar_libro(Libro(titulo, autor,num_pag, calificacion))

    


def menu():
    print("*" *30)
    print("     Mis libros favoritos")
    print("*" *30)
    print("-" *30)
    print("-----------Opciones-----------")
    print("-" *30)

    print("1)- Agregar un libro")
    print("2)- Modificar un libro")
    print("3)- Eliminar un libro")
    print("4)- Listar todos los libros")
    print("5)- salir")
    print("-" *30)

    opcion = 0
    while opcion != 5:
        opcion = (int(input("ingrese una opcion: ")))
        if opcion == 1:
            insertar_libro()
        elif opcion == 2:
            modificar_libro()
        elif opcion == 3:
            conjunto.eliminar()
        elif opcion == 4:
            conjunto.mostrar_lista()
        elif opcion == 5:
            print("Gracias por usar nuestro servicio")


                
        

   

##CODIGO PRINCIPAL
conjunto = ConjuntoLibros()
#conjunto.agregar_libro(Libro("El principito", "Yo", "200", 10))
#conjunto.agregar_libro(Libro("Orgullo y prejuicio", "Jane Austin", "240", 9))
#conjunto.agregar_libro(Libro("Rebelion en la granja", "George Orwel", "100", 6))
#conjunto.agregar_libro(Libro("Desde mi cielo", "Alice Sebold", "390", 2))
#conjunto.agregar_libro(Libro("Harry Potter y la piedra filosofal", "J.K. Rowlin", "800", 10))
#conjunto.agregar_libro(Libro("Cincuenta sombras de Grey", "E.L. James", "200", 10))



print(conjunto.listado[0: ])

#conjunto.eliminar("Harry Potter y la piedra filosofal")
menu()



