import pygame
import pygame_menu


background_image = "tilesheet/background/nuit-etoile-mont-blanc.jpg"
perso1_image = "tilesheet/perso1/pepe1.png"
HAUTEUR, LARGEUR = 1920, 1080

def load_game():
    global afficher_menu
    afficher_menu = True
    print("Et toc !")
    menu._open(loading)
    pygame.time.set_timer(update_loading,30)
    

pygame.init()
screen = pygame.display.set_mode((HAUTEUR,LARGEUR))
pygame.display.set_caption("Cyber's")
########################################################################
#Chargement des images##################################################
background = pygame.image.load(background_image).convert()
perso1 = pygame.image.load(perso1_image)
perso1 = pygame.transform.scale(perso1,(150, 240)).convert_alpha()
########################################################################
#Thème perso############################################################
mytheme = pygame_menu.Theme(widget_font=pygame_menu.font.FONT_BEBAS,
                            background_color=(255, 0, 0, 255),
                            title_background_color=(109, 7, 26),
                            title_font_shadow=True,
                            widget_padding=100)
########################################################################
#Menu main##############################################################
menu = pygame_menu.Menu("Cyber's", HAUTEUR, LARGEUR,theme=mytheme)
arrow = pygame_menu.widgets.LeftArrowSelection(arrow_size = (10,15),)
menu.add.text_input("Ton  CyberNom  est : ", default='')
menu.add.button('Play', load_game)
menu.add.button('Quit', pygame_menu.events.EXIT)
##################################################################################
#Menu de chargement###############################################################
loading = pygame_menu.Menu("Chargement en cours",HAUTEUR,LARGEUR,theme=mytheme)
loading.add.progress_bar("Cyber's Net",progressbar_id="1",width=300)
update_loading = pygame.USEREVENT + 0
##################################################################################
#Variables du Grand While#########################################################
game = True
afficher_menu = True
run = False
clock = pygame.time.Clock()
##################################################
#Coord pepe#######################################
x,y = HAUTEUR//2,LARGEUR//2 #Variable statique
movex,movey = 0,0 #Variable delta
##################################################

while game:
    events = pygame.event.get()
    if afficher_menu:
        for event in events:
            if event.type == pygame.QUIT:
                game = False
            if event.type == update_loading:
                progress = loading.get_widget("1")
                progress.set_value(progress.get_value()+1)
                if progress.get_value() == 100:
                    pygame.time.set_timer(update_loading,0)
                    progress.set_value(0)
                    run, afficher_menu = True, False
        if menu.is_enabled():
            menu.update(events)
            menu.draw(screen)
            if (menu.get_current().get_selected_widget()):
                arrow.draw(screen,menu.get_current().get_selected_widget())
    
    if run:
        for event in events:
            if event.type == pygame.QUIT:
                game = False

            if event.type == pygame.KEYDOWN: # If clée pressée
                if event.key == pygame.K_SPACE:
                    pass
                elif event.key == pygame.K_UP:
                    movey = -10
                elif event.key == pygame.K_DOWN:
                    movey = 10
                elif event.key == pygame.K_RIGHT:
                    movex = 10
                elif event.key == pygame.K_LEFT:
                    movex = -10
                elif event.key == pygame.K_ESCAPE:
                    run = False
                    pause = True # On verra ça plus tard dans le developpement

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
        perso1_rect = perso1.get_rect(center=(x,y))
        screen.blit(perso1,perso1_rect)
    
    clock.tick(60)
    pygame.display.update()

pygame.quit()
quit()