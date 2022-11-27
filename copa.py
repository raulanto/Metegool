"""
    la clase Copa , muestra a l inicio de la pantalla moviendose arriba y abajo
"""

import pygame
import configuracion
import os


class Copa(pygame.sprite.Sprite):
    def __init__(self):
        # Heredamos el init de la clase Sprite de Pygame
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(os.path.join(configuracion.carpeta_copa, "copa.tif")),
                                            (260, 400))
        self.rect = self.image.get_rect()
        self.rect.centerx = 500
        self.rect.bottom = 460
        self.velocidad_aleatoria_y = 1

    def update(self):
        #actilizamos la posicion de la copa
        self.rect.y += self.velocidad_aleatoria_y
        # Limita el margen inferior
        if self.rect.bottom >= 460:
            self.velocidad_aleatoria_y -= 0.5
        # Limita el margen superior
        if self.rect.top <= 0:
            self.velocidad_aleatoria_y += 0.5

class Gool(pygame.sprite.Sprite):
    def __init__(self):
        # Heredamos el init de la clase Sprite de Pygame
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(os.path.join(configuracion.carpeta_copa, "gool.tif")),
                                            (450, 130))
        self.rect = self.image.get_rect()
        self.rect.centerx = 500
        self.rect.bottom = 460
        self.velocidad_aleatoria_y = -5

    def update(self):

        self.rect.y+=self.velocidad_aleatoria_y
        if self.rect.top <=0:
            self.kill()

