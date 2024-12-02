import pygame

#PANTALLA
ANCHO_VENTANA = 1100
#ALTO_VENTANA = 660
ALTO_VENTANA=630
PANTALLA = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
IMAGEN_BOTON_GENERICO = pygame.image.load("tp_juego/Imagenes/BotonDefault.png")
IMAGEN_BOTON_SOUND_OFF = pygame.image.load("tp_juego/Imagenes/SoundOff.png")
IMAGEN_BOTON_SOUND_ON = pygame.image.load("tp_juego/Imagenes/SoundOn.png")

#COLORES 
BLANCO  = (242, 233, 216)
BLANCO_PURO = (255,255,255)
MARRON = (117, 81, 18)
ROJO = (224, 67, 49)
AZUL = (37, 12, 237)
AZUL_OSCURO = (0, 150, 255)
AMARILLO = (237, 235, 12)
CELESTE = (2, 218, 247)
VERDE = (56, 212, 12)

#IMAGENES
FOTO_CORRER = [pygame.image.load("tp_juego/Imagenes/Dog_Run_1.png"),
                pygame.image.load("tp_juego/Imagenes/Dog_Run_2.png")]
FOTO_SALTAR = pygame.image.load("tp_juego/Imagenes/Dog_Run_1.png")
FOTO_AGACHAR = pygame.image.load("tp_juego/Imagenes/Dog_Duck.png")
FOTO_FANTASMA = pygame.image.load("tp_juego/Imagenes/Ghost.png")
FOTO_FANTASMA_VOLADOR = [pygame.image.load("tp_juego/Imagenes/Flying_Ghost_1.png"),
                        pygame.image.load("tp_juego/Imagenes/Flying_Ghost_2.png")]
FOTO_NUBE = pygame.image.load("tp_juego/Imagenes/Cloud.png")
FONDO_JUEGO = pygame.image.load("tp_juego/Imagenes/Background_2.png")
FONDO_MENU = pygame.image.load("tp_juego/Imagenes/Fondo_menu.jpg")

#TECLAS
TECLA_SALTAR = pygame.K_UP
TECLA_AGACHAR = pygame.K_DOWN

#CONFIGURACION
MINIMO_NOMBRE = 3
MAXIMO_NOMBRE = 10
VELOCIDAD_INICIAL = 14
PUNTAJE_INICIAL = 0 
VALOR_INCREMENTO_POR_ITERACION = 1
VALOR_INCREMENTO_VELOCIDAD = 1
PUNTOS_PARA_INCREMENTO_VELOCIDAD = 50
SEPARADOR_ARCHIVO = ","
RUTA_ARCHIVO_PARTIDAS = "tp_juego/partidas.csv"