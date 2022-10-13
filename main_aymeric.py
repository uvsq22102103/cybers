import pygame
import pygame_menu

def start_the_game():
    print("Et toc !")
    background = pygame.image.load(background_image).convert()
    perso1 = pygame.image.load(perso1_image)
    perso1 = pygame.transform.scale(perso1,(150, 240)).convert_alpha()
    run = True
    clock = pygame.time.Clock()
    x,y = HAUTEUR//2,LARGEUR//2 #Variable statique
    movex,movey = 0,0 #Variable delta
    clock = pygame.time.Clock()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
            if event.type == pygame.KEYDOWN: # If clée pressée
                if event.key == pygame.K_SPACE:
                    pass
                elif event.key == pygame.K_UP:
                    movey = -2
                elif event.key == pygame.K_DOWN:
                    movey = 2
                elif event.key == pygame.K_RIGHT:
                    movex = 2
                elif event.key == pygame.K_LEFT:
                    movex = -2
                elif event.key == pygame.K_ESCAPE:
                    run = False


            elif event.type == pygame.KEYUP: # If clée relâchée
                if event.key == pygame.K_SPACE:
                    pass
                elif event.key == pygame.K_UP:
                    movey = 0
                elif event.key == pygame.K_DOWN:
                    movey = 0
                elif event.key == pygame.K_RIGHT:
                    movex = 0
                elif event.key == pygame.K_LEFT:
                    movex = 0
        x += movex
        y += movey
        screen.blit(background,(0,0))
        screen.blit(perso1,(x,y))
        pygame.display.update()
        clock.tick(60)


background_image = "tilesheet/background/nuit-etoile-mont-blanc.jpg"
perso1_image = "tilesheet/perso1/pepe1.png"
HAUTEUR, LARGEUR = 1920, 1080

pygame.init()
screen = pygame.display.set_mode((HAUTEUR,LARGEUR))
pygame.display.set_caption("Cyber's")

mytheme = pygame_menu.Theme(widget_font=pygame_menu.font.FONT_8BIT,
                            background_color=(0, 0, 0, 255),
                            title_background_color=(109, 7, 26),
                            title_font_shadow=True,
                            widget_padding=100)

menu = pygame_menu.Menu("Cyber's", HAUTEUR, LARGEUR,theme=mytheme)
menu.add.text_input("Ton CyberNom est ", default='')
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)
menu.mainloop(screen)

pygame.quit()
quit()