from main_aymeric import *

class Character(pygame.sprite.Sprite):
    def __init__(self,chemin,animated:bool=False,scale:int=5):
        super().__init__()
        if animated:
            self.chemin = chemin
        else:
            self.image = pygame.image.load(chemin)
            if scale != 1:
                self.image = pygame.transform.scale(perso1,(25*scale, 40*scale)).convert_alpha()
        self.animated = animated
        self.scale = scale