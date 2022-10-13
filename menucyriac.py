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
    global afficher_menu
    afficher_menu =True
    mainmenu._open(loading)
    pygame.time.set_timer(update_loading,5)

def option_menu():
    mainmenu._open(optionsmenu)



#Initialisation de Pygame##################
###########################################
pygame.init()

screen = pygame.display.set_mode((HAUTEUR,LARGEUR))
pygame.display.set_caption("Cyber's")

########################################################################
#Chargement des images##################################################
background = pygame.image.load(background_image).convert()
perso1 = pygame.image.load(perso1_image)
perso1 = pygame.transform.scale(perso1,(150, 240)).convert_alpha()


#Menus#####################################
###########################################
mainmenu = pygame_menu.Menu("Cyber's",HAUTEUR,LARGEUR,theme = themes.THEME_DARK)
mainmenu.add.text_input(" ",default="Entre ton cyber-nom", maxchar=20)
mainmenu.add.button("Jouer", start_the_game)
mainmenu.add.button("Options", option_menu)
arrow = pygame_menu.widgets.LeftArrowSelection(arrow_size = (100,150))


optionsmenu = pygame_menu.Menu("Options",HAUTEUR,LARGEUR,theme = themes.THEME_DARK)
optionsmenu.add.range_slider("Volume", rangeslider_id = "2", default=100, range_values= (0,100), range_widht= 200, increment= 2)

loading = pygame_menu.Menu("Chargement en cours",HAUTEUR,LARGEUR,theme=themes.THEME_BLUE)
loading.add.progress_bar("Connection au Cybernet", progressbar_id = "1", default=0, width = 200)
update_loading = pygame.USEREVENT + 0

#Variables#################################
###########################################
game = True
run = False
afficher_menu = True
clock = pygame.time.Clock()

#Coord perso###############################
###########################################
x,y = HAUTEUR//2,LARGEUR//2
movex,movey = 0,0

#Boucle principale#########################
###########################################
while game:
    events = pygame.event.get()
    if afficher_menu:
        for event in events:
            if event.type == pygame.QUIT:
                game=False

            if event.type == update_loading:
                progress = loading.get_widget("1")
                progress.set_value(progress.get_value()+1)
                if progress.get_value() == 100:
                    pygame.time.set_timer(update_loading,0)
                    progress.set_value(0)
                    run, afficher_menu = True, False
        
        if mainmenu.is_enabled():
            mainmenu.update(events)
            mainmenu.draw(screen)
            if mainmenu.get_current().get_selected_widget():
                arrow.draw(screen, mainmenu.get_current().get_selected_widget())

    if run:
        for event in events:
            if event.type == pygame.QUIT:
                game=False
        #Gestion mapping/keys##############
            if event.type == pygame.KEYDOWN: # If clée pressée
                if event.key == pygame.K_ESCAPE:
                    pass
                elif event.key == pygame.K_UP:
                    movey = -5
                elif event.key == pygame.K_DOWN:
                    movey = 5
                elif event.key == pygame.K_RIGHT:
                    movex = 5
                elif event.key == pygame.K_LEFT:
                    movex = -5
            elif event.type == pygame.KEYUP: # If clée relâchée
                if event.key == pygame.K_ESCAPE:
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