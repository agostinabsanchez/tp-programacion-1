
class Boton:
    def __init__(self, imagen, posicion, fuente, color_base, color_activo, texto):
        self.imagen = imagen
        self.x_pos = posicion[0]
        self.y_pos = posicion[1]
        self.fuente = fuente
        self.texto_string = texto
        if self.texto_string is not None:
            self.color_base = color_base
            self.color_activo = color_activo
            self.texto = self.fuente.render(self.texto_string, True, (244, 244, 247))
            self.texto_rect = self.texto.get_rect(center=(self.x_pos, self.y_pos))
        if self.imagen is None:
            self.imagen = self.texto
        self.rect = self.imagen.get_rect(center=(self.x_pos, self.y_pos + 5))

    def update(self, pantalla):
        pantalla.blit(self.imagen, self.rect)
        if self.texto_string is not None:
            pantalla.blit(self.texto, self.texto_rect)

    def chequear_input_usuario(self, posicion):
        return posicion[0] in range(self.rect.left, self.rect.right) and posicion[1] in range(self.rect.top, self.rect.bottom)

    def cambiar_color(self, posicion):
        color = self.color_base
        if posicion[0] in range(self.rect.left, self.rect.right) and posicion[1] in range(self.rect.top, self.rect.bottom):
            color = self.color_activo
        
        self.texto = self.fuente.render(self.texto_string, True, color)