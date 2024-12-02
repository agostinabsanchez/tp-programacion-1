from configuraciones import *
from funciones_genericas import *
from class_boton import *

def boton_volver_menu_obtener():
    return Boton(
                pygame.transform.scale(IMAGEN_BOTON_GENERICO,(200,70)), 
                (900, 550), 
                obtener_fuente(30), 
                MARRON, 
                BLANCO, 
                "Volver a Menu")

def boton_mutear_obtener():
    return Boton(
                pygame.transform.scale(IMAGEN_BOTON_SOUND_OFF,(50,70)), 
                (1050, 550), 
                None, 
                None, 
                None, 
                None)

def ingresar_nombre(minimo, maximo) -> str:
    texto_input = ""
    ingresando_texto = True
    fuente_titulo = obtener_fuente(70)
    fuente_subtitulo = obtener_fuente(50)
    PANTALLA.fill(CELESTE)
    texto = fuente_titulo.render("INGRESE SU NOMBRE", True, BLANCO)
    texto_rect = texto.get_rect()
    texto_rect.center = (ANCHO_VENTANA // 2 , ALTO_VENTANA // 2 - 100)    
    subtitulo = fuente_subtitulo.render(f"Nombre válido entre {minimo} y {maximo} caracteres", True, BLANCO)
    subtitulo_rect = subtitulo.get_rect()
    subtitulo_rect.center = (ANCHO_VENTANA // 2 , ALTO_VENTANA // 2 - 30) 

    while ingresando_texto:
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ingresando_texto = False
                pygame.quit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    if len(texto_input) >= minimo and len(texto_input) <= maximo:
                        ingresando_texto = False
                elif evento.key == pygame.K_BACKSPACE:
                    texto_input = texto_input[:-1]
                else:
                    if len(texto_input) <= maximo and evento.unicode.isalnum():
                        texto_input += evento.unicode

        if len(texto_input) >= minimo and len(texto_input) <= maximo:
            subtitulo = fuente_subtitulo.render(f"Nombre válido entre {minimo} y {maximo} caracteres", True, VERDE)
        else:
            subtitulo = fuente_subtitulo.render(f"Nombre válido entre {minimo} y {maximo} caracteres", True, ROJO)

        PANTALLA.fill(CELESTE)
        PANTALLA.blit(texto, texto_rect)
        PANTALLA.blit(subtitulo, subtitulo_rect)
        entrada = fuente_titulo.render(texto_input, True, BLANCO)
        entrada_rect = entrada.get_rect()
        entrada_rect.center = (ANCHO_VENTANA // 2 , ALTO_VENTANA // 2 + 30)
        PANTALLA.blit(entrada, entrada_rect)

        pygame.display.flip()
    return texto_input

def calcular_puntaje(puntos, pantalla, fuente_puntaje, evento_incrementar_velocidad):
    puntos += VALOR_INCREMENTO_POR_ITERACION
    if puntos % PUNTOS_PARA_INCREMENTO_VELOCIDAD == 0:
        evento = pygame.event.Event(evento_incrementar_velocidad, {"Cantidad_A_Incrementar": VALOR_INCREMENTO_VELOCIDAD})
        pygame.event.post(evento)
    
    texto = fuente_puntaje.render("Puntos: " + str(puntos), True, (0, 0, 0))
    textoRect = texto.get_rect()
    textoRect.center = (950, 40)
    pantalla.blit(texto, textoRect)

    return puntos

def actualizar_fondo(pantalla, x_pos_fondo, y_pos_fondo, velocidad_juego):
    ancho_imagen = FONDO_JUEGO.get_width()
    pantalla.blit(FONDO_JUEGO, (x_pos_fondo, y_pos_fondo))
    pantalla.blit(FONDO_JUEGO, (ancho_imagen + x_pos_fondo, y_pos_fondo))
    if x_pos_fondo <= -ancho_imagen:
        pantalla.blit(FONDO_JUEGO, (ancho_imagen + x_pos_fondo, y_pos_fondo))
        x_pos_fondo = 0
    x_pos_fondo -= velocidad_juego
    return x_pos_fondo