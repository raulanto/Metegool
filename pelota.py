"""
    Pelota
"""


import configuracion
import pygame
import os

NIVEL_SUELO = 500


class Pelota(pygame.sprite.Sprite):
    def __init__(self):
        # Heredamos el init de la clase Sprite de Pygame
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(os.path.join(configuracion.carpeta_personajes, "pelota.tif")), (40, 40))
        self.image.set_colorkey(configuracion.NEGRO)
        self.rect = self.image.get_rect()
        self.radius = 20
        self.rect.x = 500
        self.rect.y = 250
        self.velocidad_inicial = 0
        self.velocidad_aleatoria_x = 5
        self.velocidad_aleatoria_y = 5
        self.cadencia = 750
        self.ultimo_gool = pygame.time.get_ticks()

    def update(self):
        self.rect.x += self.velocidad_aleatoria_x
        self.rect.y += self.velocidad_aleatoria_y

        # Limita el margen izquierdo
        if self.rect.left < 0:
            self.velocidad_aleatoria_x += 2

        # Limita el margen derecho
        if self.rect.right > 1000:
            self.velocidad_aleatoria_x -= 2

        teclas = pygame.key.get_pressed()

        #valua el ultmo salto
        if self.rect.bottom >= NIVEL_SUELO:
            self.rect.bottom = NIVEL_SUELO
            #espera un tiempo para sar otro salto
            ahora = pygame.time.get_ticks()
            if ahora - self.ultimo_gool > self.cadencia:
                if teclas[pygame.K_UP]:
                    self.ultimo_gool = ahora
                    self.velocidad_inicial = -25
                    self.velocidad_aleatoria_x = 0
                    self.actualizar_salto()
        else:
            self.actualizar_salto()

        # Limita el margen inferior
        if self.rect.bottom >= 500:
            self.rect.bottom = 500
            # si la velocidad de x esta en 0 se le ponen un valor para que la pelota siempre avance
            if self.velocidad_aleatoria_x == 0:
                self.velocidad_aleatoria_x = 5

        # Limita el margen superior
        if self.rect.top < 0:
            self.rect.top = 0

    def actualizar_salto(self):
        # si está saltando actualiza su posición
        self.rect.y += self.velocidad_inicial
        self.velocidad_inicial += 0.5
