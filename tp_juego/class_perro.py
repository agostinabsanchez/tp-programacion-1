class Perro:
    X_POS = 80
    Y_POS = 250
    Y_POS_AGACHAR = 260
    SALTO_VEL = 8.5

    def __init__(self, fotos_correr, foto_saltar, foto_agachar, tecla_saltar, tecla_agachar):
        self.agachar_img = foto_agachar
        self.correr_img = fotos_correr
        self.saltar_img = foto_saltar


        self.perro_agachar = False
        self.perro_correr = True
        self.perro_saltar = False

        self.step_index = 0
        self.salto_vel = self.SALTO_VEL
        self.imagen = self.correr_img[0]
        self.perro_rect = self.imagen.get_rect()
        self.perro_rect.x = self.X_POS
        self.perro_rect.y = self.Y_POS

        self.tecla_saltar = tecla_saltar
        self.tecla_agachar = tecla_agachar
    
    def update(self, input_usuario):
        if self.perro_agachar:
            self.agachar()
        elif self.perro_correr:
            self.correr()
        elif self.perro_saltar:
            self.saltar()

        if self.step_index >= 10:
            self.step_index = 0

        if input_usuario[self.tecla_saltar] and not self.perro_saltar:
            self.perro_agachar = False
            self.perro_correr = False
            self.perro_saltar = True
        elif input_usuario[self.tecla_agachar] and not self.perro_saltar:
            self.perro_agachar = True
            self.perro_correr = False
            self.perro_saltar = False
        elif not (self.perro_saltar or input_usuario[self.tecla_agachar]):
            self.perro_agachar = False
            self.perro_correr = True
            self.perro_saltar = False

    def agachar(self):
        self.imagen = self.agachar_img
        self.perro_rect = self.imagen.get_rect()
        self.perro_rect.x = self.X_POS
        self.perro_rect.y = self.Y_POS_AGACHAR

    def correr(self):
        self.imagen = self.correr_img[self.step_index // 5]
        self.perro_rect = self.imagen.get_rect()
        self.perro_rect.x = self.X_POS
        self.perro_rect.y = self.Y_POS
        self.step_index += 1

    def saltar(self):
        self.imagen = self.saltar_img
        if self.perro_saltar:
            self.perro_rect.y -= self.salto_vel * 4
            self.salto_vel -= 0.8
        if self.salto_vel < - self.SALTO_VEL:
            self.perro_saltar = False
            self.salto_vel = self.SALTO_VEL

    def draw(self, PANTALLA):
        PANTALLA.blit(self.imagen, (self.perro_rect.x, self.perro_rect.y))