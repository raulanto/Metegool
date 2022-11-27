"""
    Porteria
"""
import configuracion
import pygame
import os

NIVEL_SUELO=500
class Porteria(pygame.sprite.Sprite):
    def __init__(self):
        # Heredamos el init de la clase Sprite de Pygame
        super().__init__()
        self.image=pygame.transform.scale(pygame.image.load(os.path.join(configuracion.carpeta_portero,"porteria.tif")),(300,100))
        self.rect=self.image.get_rect()
        self.radius = 50
        self.rect.center=(500,60)