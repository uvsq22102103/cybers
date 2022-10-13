import pygame
import pygame_menu
from scriptes import start

HAUTEUR, LARGEUR = 1920, 1080
background_image = "tilesheet/background/nuit-etoile-mont-blanc.jpg"
perso1_image = "tilesheet/perso1/pepe1.png"
pygame.init()
screen = pygame.display.set_mode((HAUTEUR,LARGEUR))

if __name__ == "__main__":
    pygame.display.set_caption("Cyber's")

    mytheme = pygame_menu.Theme(widget_font=pygame_menu.font.FONT_8BIT,
                                background_color=(0, 0, 0, 255),
                                title_background_color=(109, 7, 26),
                                title_font_shadow=True,
                                widget_padding=100)

    menu = pygame_menu.Menu("Cyber's", HAUTEUR, LARGEUR,theme=mytheme)
    menu.add.text_input("Ton CyberNom est ", default='')
    menu.add.button('Play', start.start_the_game)
    menu.add.button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(screen)

    pygame.quit()
    quit()