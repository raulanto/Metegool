"""
    Portero
"""
import configuracion
import pygame
import os
import random
NIVEL_SUELO=500
class Portero(pygame.sprite.Sprite):
    def __init__(self):
        # Heredamos el init de la clase Sprite de Pygame
        super().__init__()
        i =random.randrange(1,8)
        self.image=pygame.transform.scale(pygame.image.load(os.path.join(configuracion.carpeta_portero,f"portero{i}.tif")),(40,90))
        self.rect=self.image.get_rect()
        self.rect.centerx=375
        self.rect.y=50
        self.velocidad_aleatoria_x = 3
    def update(self):
        self.rect.x += self.velocidad_aleatoria_x
        # Limita el margen izquierdo
        if self.rect.left < 300:
            self.velocidad_aleatoria_x += 1
        # Limita el margen derecho
        if self.rect.right >700:
            self.velocidad_aleatoria_x -= 1

