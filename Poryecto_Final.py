import pygame
import sys #Gestiona la salida del programa.
import math #Funciones matemáticas.
import time #Herramientas de medición de tiempo y manipulación de fechas.
import random #Genera números pseudoaleatorios.
import os #Da interfaz para interactuar con el sistema operativo, Acceder a archivos y directorios.

pygame.init() #Inicializa procesos.
pygame.font.init() #trabaja con texto y fuentes.
pygame.mixer.init() #trabaja con sonidos y música.

ALTURA_BOTON = 40
MEDIDA_CUADRO = 165
NOMBRE_IMAGEN_OCULTA = ".\\Material\\Ocultaa.png"
SEGUNDOS_MOSTRAR_PIEZA = 1

class Cuadro:
    def __init__(self, fuente_imagen):
        #Este atributo se utiliza para determinar si el cuadro debe mostrarse en la pantalla o no.
        self.mostrar = True
        self.descubierto = False
        self.fuente_imagen = fuente_imagen
        self.imagen_real = pygame.image.load(fuente_imagen)
# Rutas de las imágenes
image_paths = [
    ["C++.png", "C++.png", "chat.png", "chat.png"],
    ["chrome.png", "chrome.png", "Github.png", "Github.png"],
    ["phyton.png", "phyton.png", "Turtle.png", "Turtle.png"],
    ["Wifi.png", "Wifi.png", "Visual_Code.png", "Visual_Code.png"]
]

# Directorio base
base_directory = os.path.dirname(__file__)
material_directory = "Material"

full_image_paths = [
    [os.path.join(base_directory, material_directory, image) for image in row] for row in image_paths
]

# Crear cuadros
cuadros = [[Cuadro(image_path) for image_path in row] for row in full_image_paths]
color_blanco = (255, 255, 255)
color_negro = (0, 0, 0)
color_rojo = (255, 0, 0)
color_gris = (206, 206, 206)
color_azul = (30, 136, 229)


SONIDO_FONDO = pygame.mixer.Sound(os.path.join("Material", "FondoPerfect.wav"))
SONIDO_CLIC = pygame.mixer.Sound(os.path.join("Material", "correcta.wav"))
SONIDO_EXITO = pygame.mixer.Sound(os.path.join("Material", "ganador .wav"))
SONIDO_FRACASO = pygame.mixer.Sound(os.path.join("Material", "equivocado .wav"))
SONIDO_VOLTEAR = pygame.mixer.Sound(os.path.join("Material", "voltear.wav"))

#Calcula la anchura total de la pantalla multiplicando la cantidad de columnas de cuadros por el tamaño de cada cuadro.
ANCHURA_PANTALLA = len(cuadros[0]) * MEDIDA_CUADRO 
#Calcula la altura total de la pantalla sumando la altura de todas las filas de cuadros y luego sumando la altura del botón.
ALTURA_PANTALLA = (len(cuadros) * MEDIDA_CUADRO) + ALTURA_BOTON


#Fuente de letras y posicion del boton de iniciar
tamanio_fuente = 20
fuente = pygame.font.SysFont("Arial black", tamanio_fuente)
xFuente = int((ANCHURA_PANTALLA / 2) - (tamanio_fuente / 2))
yFuente = int(ALTURA_PANTALLA - ALTURA_BOTON)
boton = pygame.Rect(0, ALTURA_PANTALLA - ALTURA_BOTON, ANCHURA_PANTALLA, ALTURA_PANTALLA)


#Son booleanas que determinan el estado del juego
puede_jugar = True
juego_iniciado = False
#Son variables que almacenan las coordenadas de las dos cartas que ha seleccionado el jugador.
x1, y1, x2, y2 = None, None, None, None #significa que el jugador aún no ha seleccionado ninguna carta.


# Variables para almacenar el tiempo de inicio del juego y del cronómetro
tiempo_inicio_juego = None
tiempo_inicio_cronometro = None

# Duración del juego en segundos
DURACION_JUEGO = 180
def ocultar_todos_los_cuadros():
    for fila in cuadros:
        for cuadro in fila:
            cuadro.mostrar = False
            cuadro.descubierto = False

def aleatorizar_cuadros():
    cantidad_filas = len(cuadros)
    cantidad_columnas = len(cuadros[0])
    for y in range(cantidad_filas):
        for x in range(cantidad_columnas): #Lista de indices
            x_aleatorio = random.randint(0, cantidad_columnas - 1) # 0 es posicion inicial.
            y_aleatorio = random.randint(0, cantidad_filas - 1) # -1 accedería al último elemento de la lista.
            cuadro_temporal = cuadros[y][x] #Se guarda temporalmente el valor
            cuadros[y][x] = cuadros[y_aleatorio][x_aleatorio]
            cuadros[y_aleatorio][x_aleatorio] = cuadro_temporal


def comprobar_si_gana():
    if gana():
        pygame.mixer.Sound.play(SONIDO_EXITO)
        mostrar_mensaje1()
        
#Condicion para verificar si gana el juego o no
def gana():
    for fila in cuadros:
        for cuadro in fila:
            if not cuadro.descubierto:
                return False
    return True

def reiniciar_juego():
    global juego_iniciado, tiempo_inicio_juego, tiempo_inicio_cronometro
    juego_iniciado = False #el juego no está en curso.
    tiempo_inicio_juego = None #no se ha iniciado el cronómetro del juego.
    tiempo_inicio_cronometro = None #no se ha iniciado el cronómetro general del juego.

def iniciar_juego():
    global juego_iniciado, tiempo_inicio_juego, tiempo_inicio_cronometro
    pygame.mixer.Sound.play(SONIDO_CLIC)
    for i in range(3):
        aleatorizar_cuadros()
    ocultar_todos_los_cuadros()
    juego_iniciado = True
    tiempo_inicio_juego = time.time()
    tiempo_inicio_cronometro = time.time()

def mostrar_mensaje1():
    mensaje = fuente.render("Ganaste Brother", True, color_rojo)
    xFuenteVictoria = 10  # Ajusta la posición en el eje x
    yFuenteVictoria = ALTURA_PANTALLA - 50  # Ajusta la posición en el eje y
    pantalla_juego.blit(mensaje, (xFuenteVictoria, yFuenteVictoria))
    pygame.display.update()
    pygame.time.delay(4000)  # Mostrar el mensaje durante 4 segundos
    reiniciar_juego()
    
    
    
def mostrar_mensaje2():
    mensaje = fuente.render("Game Over Brother", True, color_rojo)
    xFuenteGameOver = 10  # Ajusta la posición en el eje x
    yFuenteGameOver = ALTURA_PANTALLA - 50  # Ajusta la posición en el eje y
    pantalla_juego.blit(mensaje, (xFuenteGameOver, yFuenteGameOver))
    pygame.display.update()
    pygame.time.delay(4000)  # Mostrar el mensaje durante 3 segundos
    reiniciar_juego()


def ocultar_cartas_incorrectas():
    cuadros[y1][x1].mostrar = False
    cuadros[y2][x2].mostrar = False

pantalla_juego = pygame.display.set_mode((ANCHURA_PANTALLA, ALTURA_PANTALLA))
pygame.display.set_caption('Memorama en Python - By Parzibyte')
pygame.mixer.Sound.play(SONIDO_FONDO, -1)


#BUCLE PRINCIPAL INFINITO
while True:
    for event in pygame.event.get(): #para iterar sobre los eventos capturados por Pygame.
        if event.type == pygame.QUIT: #para el cierre
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and puede_jugar: #Clic del mousse
            xAbsoluto, yAbsoluto = event.pos #posicion
            if boton.collidepoint(event.pos): #colision del area del clic
                if not juego_iniciado: #no se inicio
                    iniciar_juego()
                    
                    
                    
#verifica si el juego ya ha iniciado. Si no ha iniciado, el bucle continúa sin ejecutar el resto del código en este bloque.
            else:
                
                if not juego_iniciado:
                    continue
                x = math.floor(xAbsoluto / MEDIDA_CUADRO)
                y = math.floor(yAbsoluto / MEDIDA_CUADRO)
                cuadro = cuadros[y][x]
                #Nunca se ejecuta si la primera carta ya se está mostrando. MOTIVO DE UNA SOLA CARTA
                if cuadro.mostrar or cuadro.descubierto: #Si el cuadro se está mostrando 
                    continue
                if x1 is None and y1 is None: #Lo que significa que no hay una carta previamente seleccionada, se asignan las coordenadas
                    x1, y1 = x, y
                    cuadros[y1][x1].mostrar = True
                    pygame.mixer.Sound.play(SONIDO_VOLTEAR)
                    
                else:
                    #Cartas seleccionadas
                    x2, y2 = x, y
                    cuadros[y2][x2].mostrar = True
                    cuadro1, cuadro2 = cuadros[y1][x1], cuadros[y2][x2]
                    if cuadro1.fuente_imagen == cuadro2.fuente_imagen:  #Si son iguales
                        cuadros[y1][x1].descubierto = True
                        cuadros[y2][x2].descubierto = True
                        x1, x2, y1, y2 = None, None, None, None
                        pygame.mixer.Sound.play(SONIDO_CLIC)
                        comprobar_si_gana()
                    else:
                        pygame.mixer.Sound.play(SONIDO_FRACASO)
                        pygame.time.delay(int(SEGUNDOS_MOSTRAR_PIEZA * 1000)) #No son iguales 
                        ocultar_cartas_incorrectas()
                        x1, x2, y1, y2 = None, None, None, None


#Tiempo de juego al cerrar
    ahora = int(time.time())
    tiempo_transcurrido = ahora - tiempo_inicio_cronometro if tiempo_inicio_cronometro is not None else 0  
    tiempo_restante = max(DURACION_JUEGO - tiempo_transcurrido, 0)
    if tiempo_restante == 0:
        mostrar_mensaje2()
        reiniciar_juego()
        


#Relleno del color de pantalla no usada
    pantalla_juego.fill(color_blanco)
    x, y = 0, 0
    
    
    for fila in cuadros:
        x = 0 #Reinicia las coordenadas
        for cuadro in fila:
            if cuadro.descubierto or cuadro.mostrar:
                pantalla_juego.blit(cuadro.imagen_real, (x, y)) #se utiliza la imagen real del cuadro en la posición
            else:
                pantalla_juego.blit(pygame.transform.scale(pygame.image.load(NOMBRE_IMAGEN_OCULTA), (MEDIDA_CUADRO, MEDIDA_CUADRO)), (x, y))
            x += MEDIDA_CUADRO #se utiliza una imagen oculta
        y += MEDIDA_CUADRO
        
        
    #JUEGO INICIADO 
    if juego_iniciado:
        pygame.draw.rect(pantalla_juego, color_blanco, boton) #PANTALLA PRINCIPAL
        #SISTEMA DE PUNTAJE, frase para imprimir
        mensaje = f"Cantidad de puntacion: {sum(cuadro.descubierto for fila in cuadros for cuadro in fila) * 10}" 
        pantalla_juego.blit(fuente.render(mensaje, True, color_rojo), (xFuente, yFuente))
        
    #JUEGO NO INICIADO
    else:
        pygame.draw.rect(pantalla_juego, color_azul, boton)
        pantalla_juego.blit(fuente.render("Iniciar juego", True, color_blanco), (xFuente, yFuente))

    #Mostrar el cronómetro en la pantalla
    tiempo_mostrar = time.strftime("%M:%S", time.gmtime(tiempo_restante)) 
    cronometro = fuente.render(tiempo_mostrar, True, color_rojo)
    pantalla_juego.blit(cronometro, (10, 10))

    pygame.display.update()
