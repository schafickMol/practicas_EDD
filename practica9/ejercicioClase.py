class Biblioteca:
    def __init__(self, lista_libros):
        self.libros=lista_libros
    
    def mostrarLibros(self):
        for libro in self.libros:
            print(f"-{libro}")
        
    def prestarLibros(self,libro):
        if libro in self.libros:
            print(f"se presto el libro {libro}")
            self.libros.remove(libro)
        else:
            print(f"No se encontro el libro {libro}")
    
    def agregarLibro(self, libro):
        if libro not in self.libros:
            print(f"se ha agregado el libro {libro}")
            self.libros.append(libro)
        else:
            print("El libro ya esta en el inventario")

lista_libros = ["Aprender Python", "50 sombras de gray", "La biblia","El Alquimista"]

biblioteca = Biblioteca(lista_libros)    

while True:
    print(".::MENU::.")
    print("1) Mostas Libros")
    print("2) Prestar Libros")
    print("3) Agregar Libros")
    print("4) Salir")
    opcion = int(input("Que accion desea realizar: "))

    if opcion == 1 :
        print(".:: Lista de libros ::.")
        biblioteca.mostrarLibros()
    elif opcion == 2:
        libro_prestar = input("Digite el nombre del libro: ")
        biblioteca.prestarLibros(libro_prestar)
    elif opcion == 3:
        libro_agregar= input("Digite el nombre del libro para agregarlo: ")
        biblioteca.agregarLibro(libro_agregar)
    elif opcion == 4:
        break