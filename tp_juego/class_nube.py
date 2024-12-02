import random 

class Nube:
    def __init__(self, ancho_ventana, foto_nube):
        self.x = ancho_ventana + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.imagen = foto_nube
        self.ancho = self.imagen.get_width()

    def update(self,velocidad_juego, ancho_ventana):
        self.x -=  velocidad_juego
        if self.x < -self.ancho:
            self.x = ancho_ventana + random.randint(2500, 3000)
            self.y = random.randint(50, 100)

    def draw(self, pantalla):
        pantalla.blit(self.imagen, (self.x, self.y))