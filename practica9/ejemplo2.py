#Herencia
class Figura:
    nombre = ""

    def area(self):
        pass

class Triangulo(Figura):
    def __init__(self, nombre, base, altura):
        self.nombre = nombre
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura) / 2
    
triangulo = Triangulo("equilatero", 10,5)
print(triangulo.area())