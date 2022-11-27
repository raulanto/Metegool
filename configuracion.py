"""
    configuracion: clase que nos permite tener un mejor control al momento de instanciar nuestra ventana
"""



import pygame
import os
import sys

# fotogramas
fotogramas = 60
reloj = pygame.time.Clock()

# rutas
carpeta_juego = os.path.dirname(__file__)
carpeta_recursos = os.path.join(carpeta_juego, "recursos")
carpeta_personajes = os.path.join(carpeta_recursos, "pelota")
carpeta_portero = os.path.join(carpeta_recursos, "portero")
carpeta_fomdo = os.path.join(carpeta_recursos, "fondo")
carpeta_copa = os.path.join(carpeta_recursos, "copa")
carpeta_musica=os.path.join(carpeta_recursos,"musica")

# fondo de la ventana
fondo = pygame.transform.scale(pygame.image.load(os.path.join(carpeta_fomdo, "fondo.jpg")), (1000, 500))

#icono de la imagen
icono=pygame.image.load(os.path.join(carpeta_personajes,"pelota.tif"))

# tipografia
CONSOLA = pygame.font.match_font("04B_30")

#Colores
NEGRO=(0,0,0)
BLANCO=(255,255,255)

#musica fondo
pygame.mixer.init()
musica_fondo=pygame.mixer.Sound(os.path.join(carpeta_musica,"wakawaka.wav"))
musica_fondo.set_volume(0.1)


# mostrar texto en pantalla
def muestra_texto(pantalla, texto, color, dimensiones, x, y):
    tipo_letra = pygame.font.Font(CONSOLA, dimensiones)
    superficie = tipo_letra.render(texto, True, color)
    rectangulo = superficie.get_rect()
    rectangulo.center = (x, y)
    pantalla.blit(superficie, rectangulo)


# Cerrar ventana
def cerrar():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
