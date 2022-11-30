"""
 Metegol: El juego consiste en lanzar una pelota y dar en la porteria
"""
import sys
import pygame
import configuracion
import pelota
import portero
import porteria
import copa

valor = 0

pygame.init()
#tamaño de la ventana
ventana = pygame.display.set_mode((1000, 500))
#titulo de la ventana
pygame.display.set_caption("MeteGool")
#icono de la ventana
pygame.display.set_icon(configuracion.icono)

# grupos
grupo_pelota = pygame.sprite.Group()
grupo_portero = pygame.sprite.Group()
grupo_porteria = pygame.sprite.Group()


def entrada():
    a = 0
    b = 0
    copa1 = copa.Copa()
    grupo = pygame.sprite.Group()
    grupo.add(copa1)
    inicio = True
    while inicio:
        configuracion.reloj.tick(configuracion.fotogramas)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                inicio = False
        x1_relativa = a % configuracion.fondo.get_rect().width
        ventana.blit(configuracion.fondo, (x1_relativa - configuracion.fondo.get_rect().width, b))
        if x1_relativa < 1000:
            ventana.blit(configuracion.fondo, (x1_relativa, 0))
        a -= 1
        grupo.update()
        grupo.draw(ventana)
        configuracion.muestra_texto(ventana, "-METEGOOL-", configuracion.BLANCO, 80, 500, 200)
        configuracion.muestra_texto(ventana, "-presiona cualquier tecla-", configuracion.NEGRO, 30, 500, 250)
        pygame.display.update()


def juego(puntuacion):
    #pelota
    pelota1 = pelota.Pelota()
    grupo_pelota.add(pelota1)
    #portero
    portero1 = portero.Portero()
    grupo_portero.add(portero1)
    #porteria
    porteria1 = porteria.Porteria()
    grupo_porteria.add(porteria1)
    #animacion gol
    grupoGol = pygame.sprite.Group()
    tiempo=0
    a = 0
    b = 0
    juego = True
    while juego:
        #fps
        configuracion.reloj.tick(configuracion.fotogramas)
        tiempo +=10
        configuracion.cerrar()
        # actulizacion
        grupo_pelota.update()
        grupo_porteria.update()
        grupo_portero.update()
        grupoGol.update()
        # fondo
        x1_relativa = a % configuracion.fondo.get_rect().width
        ventana.blit(configuracion.fondo, (x1_relativa - configuracion.fondo.get_rect().width, b))
        if x1_relativa < 1000:
            ventana.blit(configuracion.fondo, (x1_relativa, 0))
        a -= 1
        # grupos de colision
        grupos_gol = pygame.sprite.groupcollide(grupo_pelota, grupo_porteria, True, False, pygame.sprite.collide_rect_ratio(0.7))
        grupos_portero = pygame.sprite.groupcollide(grupo_pelota, grupo_portero, True, False,
                                                    pygame.sprite.collide_circle)
        if grupos_gol:
            puntuacion += 1
            pelota1 = pelota.Pelota()
            grupo_pelota.add(pelota1)
            gol = copa.Gool()
            grupoGol.add(gol)
        if grupos_portero:
            if puntuacion >= 1:
                puntuacion -= 1
            pelota1 = pelota.Pelota()
            grupo_pelota.add(pelota1)
        # dibujar
        grupo_porteria.draw(ventana)
        grupo_portero.draw(ventana)
        grupo_pelota.draw(ventana)
        grupoGol.draw(ventana)
        configuracion.muestra_texto(ventana, "Goles: "+str(puntuacion).zfill(2), configuracion.BLANCO, 25, 890, 15)
        configuracion.muestra_texto(ventana, "Tiempo: "+str(round(tiempo/1000,1)).zfill(4), configuracion.BLANCO, 20, 100, 15)
        pygame.display.update()
        #termina el juego por tiempo
        if tiempo >=60000:
            juego=False
    grupo_porteria.empty()
    grupo_portero.empty()
    grupo_pelota.empty()
    pygame.display.update()

    #cuadno se acaba el tiempo
    fin_Juego(puntuacion)

def fin_Juego(puntuacion):

    a=0
    b=0
    fin=True
    while fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                fin = False
        x1_relativa = a % configuracion.fondo.get_rect().width
        ventana.blit(configuracion.fondo, (x1_relativa - configuracion.fondo.get_rect().width, b))
        if x1_relativa < 1000:
            ventana.blit(configuracion.fondo, (x1_relativa, 0))
        a -= 1
        configuracion.muestra_texto(ventana, "PUNTUACION="+str(puntuacion), configuracion.BLANCO, 60, 500, 200)
        configuracion.muestra_texto(ventana, "-presiona cualquier tecla-", configuracion.NEGRO, 30, 500, 250)
        pygame.display.update()


# musica play
configuracion.musica_fondo.play(-1)
while True:
    configuracion.reloj.tick(configuracion.fotogramas)
    configuracion.cerrar()
    entrada()
    juego(valor)
    pygame.display.update()
