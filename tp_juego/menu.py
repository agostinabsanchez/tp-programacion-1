from funciones_genericas import *
from class_boton import *
from configuraciones import *

def fondo_menu_mostrar():
    imagen = obtener_imagen_escala(FONDO_MENU, ANCHO_VENTANA, ALTO_VENTANA)
    PANTALLA.blit(imagen,(0,0))

def boton_menu_jugar_obtener():
    return Boton(
                pygame.transform.scale(IMAGEN_BOTON_GENERICO,(400,70)), 
                (550, 200), 
                obtener_fuente(50), 
                MARRON, 
                BLANCO, 
                "JUGAR")

def boton_menu_instrucciones_obtener():
    return Boton(
                pygame.transform.scale(IMAGEN_BOTON_GENERICO,(400,70)),
                (550, 280), 
                obtener_fuente(50),
                MARRON, 
                BLANCO, 
                "INSTRUCCIONES")

def boton_menu_ranking_obtener():
    return Boton(
                pygame.transform.scale(IMAGEN_BOTON_GENERICO,(400,70)), 
                (550, 360), 
                obtener_fuente(50), 
                MARRON, 
                BLANCO, 
                "RANKING")

def boton_menu_ultimas_partidas_obtener():
    return Boton(
                pygame.transform.scale(IMAGEN_BOTON_GENERICO,(400,70)), 
                (550, 440), 
                obtener_fuente(45), 
                MARRON, 
                BLANCO, 
                "ULTIMAS PARTIDAS")

def boton_menu_salir_obtener():
    return Boton(
                pygame.transform.scale(IMAGEN_BOTON_GENERICO,(400,70)), 
                (550, 520), 
                obtener_fuente(50),
                MARRON, 
                BLANCO, 
                "SALIR")