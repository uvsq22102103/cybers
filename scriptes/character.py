from start import pygame
# Servira à importer des personnages plus facilement dans l'instance

class Character():
    def __init__(self,name:str):
        if name == "pepe":
            self.name = "pepe"
            self.image = pygame.image.load("tilesheet/perso1/pepe1.png")
            self.image = pygame.transform.scale(self.image,(150, 240)).convert_alpha()