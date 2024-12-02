class Fantasma: 
    def __init__(self, imagenes, tipo, ancho_ventana):
        self.imagenes = imagenes
        self.imagen = imagenes[0]
        self.index = 0
        self.tipo = tipo
        self.rect = self.imagen.get_rect()
        self.rect.x = ancho_ventana
        if self.tipo == 1:
            self.rect.y = 240
        else:
            self.rect.y = 190

    def update(self, velocidad_juego : int, fantasmas : list):
        self.rect.x -= velocidad_juego
        if self.rect.x < -self.rect.width:
            fantasmas.pop()

    def draw(self, pantalla):
        if self.tipo == 2:
            if self.index >= 9:
                self.index = 0
            pantalla.blit(self.imagenes[self.index//5], self.rect)
            self.index += 1
        else:
            pantalla.blit(self.imagen, self.rect)