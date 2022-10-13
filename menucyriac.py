import pygame
import pygame_menu
from pygame_menu import themes
import pygame_widgets

#Ressources################################
###########################################
background_image = "tilesheet/background/nuit-etoile-mont-blanc.jpg"
perso1_image = "tilesheet/perso1/pepe1.png"
HAUTEUR, LARGEUR = 1920,1080

#Fonctions#################################
###########################################
def start_the_game():
    mainmenu._open(loading)
    pygame.time.set_timer(update_loading,30)

def option_menu():
    mainmenu._open(optionsmenu)


#Initialisation de Pygame##################
###########################################
pygame.init()

screen = pygame.display.set_mode((HAUTEUR,LARGEUR))
pygame.display.set_caption("Cyber's")

#Menus#####################################
###########################################
mainmenu = pygame_menu.Menu("Cyber's",HAUTEUR,LARGEUR,theme = themes.THEME_DARK)
mainmenu.add.text_input("Pseudo:", default="Entre ton cyber-nom", maxchar=20)
mainmenu.add.button("Jouer", start_the_game)
mainmenu.add.button("Options", option_menu)
arrow = pygame_menu.widgets.LeftArrowSelection(arrow_size = (100,150))


optionsmenu = pygame_menu.Menu("Options",HAUTEUR,LARGEUR,theme = themes.THEME_DARK)
optionsmenu.add.range_slider("Volume", rangeslider_id = "2", default=100, range_values= (0,100), range_widht= 200, increment= 2)

loading = pygame_menu.Menu("Chargement en cours",HAUTEUR,LARGEUR,theme=themes.THEME_BLUE)
loading.add.progress_bar("Connection au Cybernet", progressbar_id = "1", default=0, width = 200)
update_loading = pygame.USEREVENT + 0

#Boucle de démarrage#######################
###########################################
run = True
while run:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()

        if event.type == update_loading:
            progress = loading.get_widget("1")
            progress.set_value(progress.get_value()+1)
            if progress.get_value() == 100:
                pygame.time.set_timer(update_loading,0)

        #Gestion mapping/keys##############
        if event.type == pygame.KEYDOWN: # If clée pressée
            if event.key == pygame.K_ESCAPE:
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
                quit()
        elif event.type == pygame.KEYUP: # If clée relâchée
            if event.key == pygame.K_ESCAPE:
                run = False
            elif event.key == pygame.K_UP:
                movey = 0
            elif event.key == pygame.K_DOWN:
                movey = 0
            elif event.key == pygame.K_RIGHT:
                movex = 0
            elif event.key == pygame.K_LEFT:
                movex = 0

    #Affiche le menu choisi###########
    if mainmenu.is_enabled():
        mainmenu.update(events)
        mainmenu.draw(screen)
        if mainmenu.get_current().get_selected_widget():
            arrow.draw(screen, mainmenu.get_current().get_selected_widget())
    

    pygame.display.update()

pygame.quit()
quit()