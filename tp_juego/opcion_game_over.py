from configuraciones import *
from funciones_genericas import *
from class_boton import *

def mostrar_pantalla_game_over(puntos, nombre):
    PANTALLA.fill(CELESTE)
    fuente = obtener_fuente(70)
    texto = fuente.render("GAME OVER", True, AZUL)
    puntaje_final = fuente.render(f"{nombre} tu puntaje es: " + str(puntos), True, AZUL)
    puntaje_rect = puntaje_final.get_rect()
    puntaje_rect.center = (ANCHO_VENTANA // 2, ALTO_VENTANA // 2 - 180)
    PANTALLA.blit(puntaje_final, puntaje_rect)
    texto_rect = texto.get_rect()
    texto_rect.center = (ANCHO_VENTANA // 2, ALTO_VENTANA // 2 - 250)
    foto_perro = obtener_imagen_escala(FOTO_CORRER[0], 150, 100)
    PANTALLA.blit(texto, texto_rect)
    PANTALLA.blit(foto_perro, (ANCHO_VENTANA // 2 - 60, ALTO_VENTANA // 2 - 70))

def boton_jugar_de_nuevo_obtener():
    return Boton(
                pygame.transform.scale(IMAGEN_BOTON_GENERICO,(400,70)), 
                (550, 400), 
                obtener_fuente(50), 
                MARRON, 
                BLANCO, 
                "Jugar de nuevo")

def boton_menu_principal_gameover_obtener():
    return Boton(
                pygame.transform.scale(IMAGEN_BOTON_GENERICO,(400,70)), 
                (550, 500), 
                obtener_fuente(50), 
                MARRON, 
                BLANCO, 
                "Menu principal")