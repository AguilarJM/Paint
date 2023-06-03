'''
Codigo con funcionamiento de paint a traves de comandos
'''
import math
import pygame

# Crear una superficie de 800x600 píxeles
WIDTH = 800
HEIGHT = 600
SURFACE = pygame.display.set_mode((WIDTH, HEIGHT))
BACKGROUND_COLOR = (0,0,0)
SURFACE.fill(BACKGROUND_COLOR)
pygame.display.flip()

# Color predeteminado de la pantalla
color = (0, 0, 0)

# Colores intercambiables para el fondo
colors = {
    'rojo': (255, 0, 0),
    'verde': (0, 255, 0),
    'azul': (0, 0, 255),
    'amarillo': (255, 255, 0),
    'blanco': (255, 255, 255),
    'negro': (0, 0, 0),
    'rosa': (255, 192, 203),
    'naranja': (255, 165, 0),
    'morado': (128, 0, 128),
    'gris': (128, 128, 128),
    'celeste': (0, 255, 255)
}

TAMANO_PIXEL = 1
trazos = []

# Objetos y sus metodos
class Triangulos:

    def dibujar_triangulo_equilatero(tex, tey, te_lado):
        '''
        Variables de triangulo equilatero
        '''
        fon = int(te_lado * math.sqrt(3) / 2)
        teuno = (tex, tey)
        tedos = (tex + te_lado, tey)
        tetres = (tex + te_lado // 2, tey - fon)
        pygame.draw.polygon(SURFACE, color, [teuno, tedos, tetres], TAMANO_PIXEL)
        pygame.display.flip()

    def dibujar_triangulo_isoceles(tix, tiy, ti_base, ti_altura):
        '''
        Variables de triangulo isoceles
        '''
        tiuno = (tix, tiy)
        tidos = (tix + ti_base, tiy)
        titres = (tix + ti_base // 2, tiy - ti_altura)
        pygame.draw.polygon(SURFACE, color, [tiuno, tidos, titres], TAMANO_PIXEL)
        pygame.display.flip()

    def dibujar_triangulo_escaleno(te_x1, te_y1, te_x2, te_y2, te_x3, te_y3):
        '''
        Variables de triangulo escaleno
        '''
        teuno = (te_x1, te_y1)
        tedos = (te_x2, te_y2)
        tetres = (te_x3, te_y3)
        pygame.draw.polygon(SURFACE, color, [teuno, tedos, tetres], TAMANO_PIXEL)
        pygame.display.flip()

# Funciones
def help():
    '''
    Lista de comando que se pueden realizar
    '''
    print ("--Bienvenidos a Paint--\n"
           "*Los Comandos que se pueden utilizar son los siguientes:\n\n"
           "*exit; con este cierras el programa\n"
           "*linea -h; puedes dibujar una linea horizontal, te pedira ingresar los valores\n"
           "*linea -v; puedes dibujar una linea vertical, te pedira ingresar los valores\n"
           "*cambiar color; modifica el color del dibujo, Puedes elejir entre:rojo,verde,azul,amarillo y cian\n"
           "*linea;Podras hacer una linea de un punto A a un punto B\n"
           "*configurar_tamano_pixel;Te permite cambiar el grosor de las lineas\n"
           "*cuadrado; podras hacer un cuadrado, te pedira ingresar los valores\n"
           "*circulo; puedes hacer un circulo, te pedira ingresar los valores\n"
           "*rectangulo; dibujara un rectangulo, le tendras que ingresar los valores\n"
           "*color_fondo; puedes cambiar el fondo de la ventana, Puedes elejir entre: rojo,verde,azul,amarillo,blanco y negro\n"
           "*equilatero; dibujara un triangulo equilatero, te pedira ingresar los valores\n"
           "*isoceles; dibujara un triangulo isoceles, te pedira ingresar los valores\n"
           "*escaleno; dibujara un triangulo escaleno, te pedira ingresar los valores\n")

def color_fondo():
    '''
    Funcion para seleccionar color de fondo
    '''
    color_name = input("Ingrese el nombre del color de fondo: ")
    color = colors.get(color_name.lower())
    if color is None:
        print("Color no válido")
        return
    SURFACE.fill(color)
    pygame.display.flip()

def cambiar_color(nombre_color):
    '''
    Variables de triangulo equilatero
    '''
    global color
    if nombre_color == "rojo":
        color = (255, 0, 0)
    elif nombre_color == "verde":
        color = (0, 255, 0)
    elif nombre_color == "azul":
        color = (0, 0, 255)
    elif nombre_color == "amarillo":
        color = (255, 255, 0)
    elif nombre_color == "cian":
        color = (0, 255, 255)
    else:
        print("Color no válido")

def linea_h(i, desplazamiento):
    '''
    Funcion para dibujar linea horizontal
    '''
    for j in range(0, 100):
        for k in range(TAMANO_PIXEL):
            SURFACE.set_at((100 + desplazamiento + j, 200 + i + k), color)
    pygame.display.flip()

def linea_v(i, desplazamiento):
    '''
    Funcion para dibujar linea vertical
    '''
    for j in range(0, 100):
        for k in range(TAMANO_PIXEL):
            SURFACE.set_at((100 + i + k, 200 + desplazamiento + j), color)
    pygame.display.flip()

def dibujar_linea(lin_a, lin_b):
    '''
    Funcion para dibujar una linea en cualquier direccion
    '''
    pygame.draw.line(SURFACE, color, lin_a, lin_b, TAMANO_PIXEL)
    pygame.display.flip()
    trazos.append((lin_a, lin_b))

def dibujar_cuadrado(cua_x, cua_y, cua_lado):
    '''
    Funcion para dibujar un cuadrado
    '''
    for i in range(cua_x, cua_x + cua_lado):
        for j in range(cua_y, cua_y + cua_lado):
            SURFACE.set_at((i, j), color)
    pygame.display.flip()
    configurar_tamano_pixel(TAMANO_PIXEL)

def dibujar_rectangulo(x, y, width, height):
    '''
    Funcion para dibujar un rectangulo
    '''
    pygame.draw.rect(SURFACE, color, pygame.Rect(x, y, width * TAMANO_PIXEL, height * TAMANO_PIXEL))
    pygame.display.flip()

def circulo(x_centro, y_centro, radio):
    '''
    Funciones para dibujar circulo
    '''
    for i in range(360):
        angulo_rad = math.radians(i)
        x = int(x_centro + radio * math.cos(angulo_rad))
        y = int(y_centro + radio * math.sin(angulo_rad))
        SURFACE.set_at((x, y), color)
    pygame.display.flip()
    configurar_tamano_pixel(TAMANO_PIXEL)

def configurar_tamano_pixel(nuevo_tamano):
    '''
    Funcion para cambiar el tamano de pixel
    '''
    global TAMANO_PIXEL
    TAMANO_PIXEL = max(1, nuevo_tamano)

# Loop principal
while True:
    cmd = input("cmd> ")
    if cmd == "exit":
        pygame.quit()

    elif cmd == "help":
        help()

    elif cmd.startswith("linea -h"):
        params = cmd.split(" ")
        if len(params) >= 4:
            try:
                i = int(params[2])
                desplazamiento = int(params[3])
                linea_h(i, desplazamiento)
            except ValueError:
                print("Comando incorrecto. Uso: linea -h <valor_i> <desplazamiento>")
        else:
            print("Comando incorrecto. Uso: linea -h <valor_i> <desplazamiento>")
    elif cmd.startswith("linea -v"):
        params = cmd.split(" ")
        if len(params) >= 4:
            try:
                i = int(params[2])
                desplazamiento = int(params[3])
                linea_v(i, desplazamiento)
            except ValueError:
                print("Comando incorrecto. Uso: linea -v <valor_i> <desplazamiento>")
        else:
            print("Comando incorrecto. Uso: linea -v <valor_i> <desplazamiento>")

    elif cmd.startswith("cambiar color"):
        params = cmd.split(" ")
        if len(params) >= 2:
            nombre_color = params[2]
            cambiar_color(nombre_color)
        else:
            print("Comando incorrecto. Uso: cambiar color <nombre_color>")

    elif cmd.startswith("linea"):
        params = cmd.split(" ")
        if len(params) >= 5:
            try:
                tunox = int(params[1])
                tunoy = int(params[2])
                tdosx = int(params[3])
                tdosy = int(params[4])
                lin_a = (tunox, tunoy)
                lin_b = (tdosx, tdosy)
                dibujar_linea(lin_a, lin_b)
            except ValueError:
                print("Comando incorrecto. Uso: linea <x1> <y1> <x2> <y2>")
        else:
            print("Comando incorrecto. Uso: linea <x1> <y1> <x2> <y2>")

    elif cmd.startswith("configurar_tamano_pixel"):
        params = cmd.split(" ")
        if len(params) == 2:
            try:
                nuevo_tamano = int(params[1])
                configurar_tamano_pixel(nuevo_tamano)
                print("Tamaño de píxel configurado:", TAMANO_PIXEL)
            except ValueError:
                print("Comando incorrecto. Uso: configurar_tamano_pixel <tamano>")
        else:
            print("Comando incorrecto. Uso: configurar_tamano_pixel <tamano>")

    elif cmd.startswith("cuadrado"):
        params = cmd.split(" ")
        if len(params) == 4:
            try:
                tex = int(params[1])
                tey = int(params[2])
                te_lado = int(params[3])
                dibujar_cuadrado(tex, tey, te_lado)
            except ValueError:
                print("Comando incorrecto. Uso: cuadrado <x> <y> <lado>")
        else:
            print("Comando incorrecto. Uso: cuadrado <x> <y> <lado>")

    elif cmd.startswith("circulo"):
        params = cmd.split(" ")
        if len(params) == 4:
            try:
                x_centro = int(params[1])
                y_centro = int(params[2])
                radio = int(params[3])
                circulo(x_centro, y_centro, radio)
            except ValueError:
                print("Comando incorrecto. Uso: circulo <x_centro> <y_centro> <radio>")
        else:
            print("Comando incorrecto. Uso: circulo <x_centro> <y_centro> <radio>")

    elif cmd.startswith("rectangulo"):
        params = cmd.split(" ")
        if len(params) >= 5:
            try:
                tex = int(params[1])
                tey = int(params[2])
                WIDTH = int(params[3])
                HEIGHT = int(params[4])
                dibujar_rectangulo(tex, tey, WIDTH, HEIGHT)
            except ValueError:
                print("Comando incorrecto. Uso: rectangulo <x> <y> <width> <height>")
        else:
            print("Comando incorrecto. Uso: rectangulo <x> <y> <width> <height>")

    elif cmd == "color_fondo":
        color_fondo()

    # Comandos de los objeto
    elif cmd == "equilatero":
        tex = int(input("Ingrese la coordenada x: "))
        tey = int(input("Ingrese la coordenada y: "))
        te_lado = int(input("Ingrese el tamaño del lado: "))
        Triangulos.dibujar_triangulo_equilatero(tex, tey, te_lado)

    elif cmd == "isoceles":
        tix = int(input("Ingrese la coordenada x: "))
        tiy = int(input("Ingrese la coordenada y: "))
        te_base= int(input("Ingrese el tamaño de la base: "))
        te_lado = int(input("Ingrese la altura: "))
        Triangulos.dibujar_triangulo_isoceles(tex, tey, te_base, te_lado)

    elif cmd == "escaleno":
        tunox = int(input("Ingrese la coordenada x1: "))
        tunoy = int(input("Ingrese la coordenada y1: "))
        tdosx = int(input("Ingrese la coordenada x2: "))
        tdosy = int(input("Ingrese la coordenada y2: "))
        ttresx = int(input("Ingrese la coordenada x3: "))
        ttresy = int(input("Ingrese la coordenada y3: "))
        Triangulos.dibujar_triangulo_escaleno(tunox, tunoy, tdosx, tdosy, ttresx, ttresy)
