class Perro:
    def sonido(self):
        print("guaauuu!!!")

class Gato:
    def sonido(self):
        print("miaauuuuu!!!")

class Vaca:
    def sonido(self):
        print("muuuuu!!!")

perro = Perro()
gato = Gato()
vaca = Vaca()

animales = [perro , gato, vaca, gato ,perro ,vaca]

for animal in animales:
    animal.sonido()


