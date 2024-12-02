import pygame
from Paquete_utilidades.Archivos import *
from datetime import datetime
from funciones_genericas import *
from class_perro import *
from class_nube import *
from class_fantasma import *
from class_boton import *
from configuraciones import *
from menu import *
from opcion_jugar import *
from opcion_game_over import *

#Registro de partidas
partidas = leer_list_diccionarios(RUTA_ARCHIVO_PARTIDAS, SEPARADOR_ARCHIVO)

global mute
mute = False 

pygame.init()
pygame.mixer.init()

def menu_principal_mostrar():
    global mute
    fuente = obtener_fuente(120)
    ejecutar = True
    texto_menu = fuente.render("SALCHI RACE", True, BLANCO_PURO)
    menu_rect = texto_menu.get_rect(center=(550, 80))
    pygame.display.set_caption("Salchi Race")
    
    boton_jugar = boton_menu_jugar_obtener()
    boton_instrucciones= boton_menu_instrucciones_obtener()
    boton_ranking = boton_menu_ranking_obtener()
    boton_ultimas_partidas = boton_menu_ultimas_partidas_obtener()
    boton_salir = boton_menu_salir_obtener()
    botones = [boton_jugar, boton_instrucciones, boton_ranking, boton_ultimas_partidas, boton_salir]

    while ejecutar:
        pos_mouse = pygame.mouse.get_pos()

        fondo_menu_mostrar()
        pygame.draw.rect(PANTALLA, MARRON, menu_rect)
        PANTALLA.blit(texto_menu,menu_rect)

        for boton in botones:
            boton.cambiar_color(pos_mouse)
            boton.update(PANTALLA)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutar = False
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if boton_jugar.chequear_input_usuario(pos_mouse):
                    mute = False
                    jugar(None)
                elif boton_instrucciones.chequear_input_usuario(pos_mouse):
                    instrucciones_mostrar()
                elif boton_ranking.chequear_input_usuario(pos_mouse):
                    partidas_mostrar("Top 5 Jugadores", funcion_criterio_desc_numerico, "Puntaje")
                elif boton_ultimas_partidas.chequear_input_usuario(pos_mouse):
                    partidas_mostrar("Ultimas partidas", funcion_criterio_desc_texto, "Fecha")
                elif boton_salir.chequear_input_usuario(pos_mouse):
                    ejecutar = False

        pygame.display.update()

    pygame.quit()

def jugar(nombre_anterior):
    if nombre_anterior is None:
        nombre = ingresar_nombre(MINIMO_NOMBRE, MAXIMO_NOMBRE)
    else:
        nombre = nombre_anterior

    ejecutar = True
    reloj = pygame.time.Clock()
    personaje = Perro(FOTO_CORRER, FOTO_SALTAR, FOTO_AGACHAR, TECLA_SALTAR, TECLA_AGACHAR)
    nube = Nube(ANCHO_VENTANA, FOTO_NUBE)
    puntos = PUNTAJE_INICIAL 
    velocidad_juego = VELOCIDAD_INICIAL
    x_pos_fondo = 0
    y_pos_fondo = 0
    fuente_puntaje = obtener_fuente(40)
    fantasmas = []
    evento_incrementar_velocidad = pygame.USEREVENT + 1
    pygame.display.set_caption("Salchi Race")

    #Registro partida 
    fecha_actual = datetime.now()
    partida = {"Nombre": nombre, "Puntaje" : puntos, "Fecha": fecha_actual.strftime("%Y-%m-%d %H:%M:%S")}

    partidas.append(partida)

    pygame.mixer.music.load("tp_juego/sounds/cancion_bkgrnd.mp3")
    pygame.mixer.music.play(-1)
    if mute:
        pygame.mixer.music.pause()
        

    while ejecutar:

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutar = False
            elif evento.type == evento_incrementar_velocidad:
                velocidad_juego += evento.dict["Cantidad_A_Incrementar"]
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    pausar_juego(puntos) 

        PANTALLA.fill(VERDE)
        input_usuario = pygame.key.get_pressed()

        x_pos_fondo = actualizar_fondo(PANTALLA, x_pos_fondo, y_pos_fondo, velocidad_juego)

        personaje.draw(PANTALLA)
        personaje.update(input_usuario)

        nube.draw(PANTALLA)
        nube.update(velocidad_juego, ANCHO_VENTANA)

        if len(fantasmas) == 0:
            random_int =  random.randint(0, 1)
            if random_int == 0:
                fantasmas.append(Fantasma([FOTO_FANTASMA], 1, ANCHO_VENTANA))
            else: 
                fantasmas.append(Fantasma(FOTO_FANTASMA_VOLADOR, 2,  ANCHO_VENTANA))

        for fantasma in fantasmas: 
            fantasma.draw(PANTALLA)
            fantasma.update(velocidad_juego, fantasmas)
            if personaje.perro_rect.colliderect(fantasma.rect):
                pygame.mixer.stop()
                pygame.mixer.music.load("tp_juego/sounds/game_over_1.mp3")
                pygame.mixer.music.play()
                pygame.time.delay(1000)
                gameover_mostrar(puntos, nombre)

        puntos = calcular_puntaje(puntos, PANTALLA, fuente_puntaje, evento_incrementar_velocidad)
        
        reloj.tick(30)
        pygame.display.update()
    pygame.quit()

def pausar_juego(puntos):
    global mute
    ejecutar = True

    BOTON_VOLVER_MENU = boton_volver_menu_obtener()

    BOTON_MUTEAR = boton_mutear_obtener()

    while ejecutar:
        pos_mouse = pygame.mouse.get_pos()

        BOTON_VOLVER_MENU.cambiar_color(pos_mouse)
        BOTON_VOLVER_MENU.update(PANTALLA)
        
        if mute: 
            BOTON_MUTEAR.imagen = obtener_imagen_escala(IMAGEN_BOTON_SOUND_OFF, 50, 70)
        else:
            BOTON_MUTEAR.imagen = obtener_imagen_escala(IMAGEN_BOTON_SOUND_ON, 50, 70)

        BOTON_MUTEAR.update(PANTALLA)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if BOTON_VOLVER_MENU.chequear_input_usuario(pos_mouse):
                    guardar_partida(puntos)
                    pygame.mixer.music.pause()
                    menu_principal_mostrar()
                elif BOTON_MUTEAR.chequear_input_usuario(pos_mouse):
                    mute = not mute
                    if mute:
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.unpause()
            elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_ESCAPE:
                        ejecutar = False

        pygame.display.update()

def instrucciones_mostrar():
    ejecutar = True
    PANTALLA.fill(CELESTE)

    titulo_texto = obtener_fuente(100).render("INSTRUCCIONES", True, BLANCO)
    titulo_rect = titulo_texto.get_rect(center=(550, 70))

    texto1 = obtener_fuente(40).render("- Usa las flechas del teclado para moverte", True, AZUL)
    texto2 =  obtener_fuente(40).render("- Salta o agachate para seguir en carrera", True, AZUL)
    texto3 = obtener_fuente(40).render("- Evita chocarte con los fantasmas!", True, AZUL)
    texto4 = obtener_fuente(40).render("- Pulsa 'ESC' para pausar el juego.", True, AZUL)

    PANTALLA.blit(titulo_texto, titulo_rect)
    PANTALLA.blit(texto1, texto1.get_rect(center=(550, 170)))
    PANTALLA.blit(texto2, texto2.get_rect(center=(550, 220)))
    PANTALLA.blit(texto3, texto3.get_rect(center=(550, 270)))
    PANTALLA.blit(texto4, texto4.get_rect(center=(550, 320)))

    opcion_atras = Boton(
                        None, 
                        (550, 500), 
                        obtener_fuente(75),
                        AZUL, 
                        BLANCO, 
                        "ATRAS")

    while ejecutar:
        pos_mouse = pygame.mouse.get_pos()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutar = False
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if opcion_atras.chequear_input_usuario(pos_mouse):
                    menu_principal_mostrar()

        opcion_atras.cambiar_color(pos_mouse)
        opcion_atras.update(PANTALLA)
        pygame.display.flip()
    pygame.quit()

def gameover_mostrar(puntos, nombre):
    ejecutar = True
    guardar_partida(puntos)

    mostrar_pantalla_game_over(puntos, nombre)

    BOTON_JUGAR_DE_NUEVO = boton_jugar_de_nuevo_obtener()
    BOTON_MENU_PRINCIPAL = boton_menu_principal_gameover_obtener()
    botones = [BOTON_JUGAR_DE_NUEVO, BOTON_MENU_PRINCIPAL]

    while ejecutar:
        pos_mouse = pygame.mouse.get_pos()

        for boton in botones:
            boton.cambiar_color(pos_mouse)
            boton.update(PANTALLA)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                ejecutar = False
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if BOTON_JUGAR_DE_NUEVO.chequear_input_usuario(pos_mouse):
                    jugar(nombre)
                elif BOTON_MENU_PRINCIPAL.chequear_input_usuario(pos_mouse):
                    menu_principal_mostrar()

        pygame.display.update()
    pygame.quit()

def partidas_mostrar(titulo, criterio, clave):

    ordenar_por_criterio(partidas, criterio, clave)

    partidas_top_5 = partidas[:5]

    mostrar_ranking(titulo, partidas_top_5)

def mostrar_ranking(titulo, partidas):
    ejecutar = True
    
    PANTALLA.fill(CELESTE)
    titulo_texto = obtener_fuente(100).render(titulo, True, BLANCO)
    titulo_rect = titulo_texto.get_rect(center=(550, 70))
    PANTALLA.blit(titulo_texto, titulo_rect)

    fuente_partida = obtener_fuente(30)

    if len(partidas) == 0: 
        texto = obtener_fuente(70).render("No hay partidas registradas aún", True, BLANCO)
        texto_rect = texto.get_rect(center=(550, 330))
        PANTALLA.blit(texto, texto_rect)
    else:
        y_separador = 150
        for indice, partida in enumerate(partidas):
            texto = fuente_partida.render(f"{indice + 1}. {partida["Nombre"]} - {partida["Puntaje"]} pts - {partida["Fecha"]}", True, BLANCO)
            texto_rect = texto.get_rect(center=(ANCHO_VENTANA // 2, y_separador))
            pygame.draw.rect(PANTALLA, AZUL, texto_rect)
            PANTALLA.blit(texto, texto_rect)
            y_separador += 70 

    opcion_atras = Boton(
                        None, 
                        (550, 500), 
                        obtener_fuente(75),
                        AZUL, 
                        BLANCO, 
                        "ATRAS")

    while ejecutar:
        pos_mouse = pygame.mouse.get_pos()

        opcion_atras.cambiar_color(pos_mouse)
        opcion_atras.update(PANTALLA)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutar = False
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if opcion_atras.chequear_input_usuario(pos_mouse):
                    menu_principal_mostrar()

        pygame.display.flip()
    pygame.quit()

def guardar_partida(puntos):
    partida_actual = partidas[len(partidas) - 1]
    modificar_puntaje(partida_actual , "Puntaje", puntos)
    escribir_diccionario(RUTA_ARCHIVO_PARTIDAS, partida_actual, SEPARADOR_ARCHIVO)

menu_principal_mostrar()