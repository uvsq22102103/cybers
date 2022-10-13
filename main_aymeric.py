import pygame, pygame_menu, random, os

##############
# résolution #

LARGEUR, HAUTEUR = 1920, 1080

###########
# Classes #

class Character(pygame.sprite.Sprite):
    def __init__(self,chemin,animated:bool=False,scale:int=5):
        super().__init__()
        if animated:
            self.images = []
            for i in os.listdir(chemin):
                temp = pygame.image.load(chemin+i)
                temp = pygame.transform.scale(temp,(25*scale, 40*scale)).convert_alpha()
                self.images.append(temp)
            self.image = self.images[0]
        else:
            self.image = pygame.image.load(chemin)
            if scale != 1:
                self.image = pygame.transform.scale(self.image,(25*scale, 40*scale)).convert_alpha()
        self.chemin = chemin
        self.animated = animated
        self.scale = scale
        self.x = random.randint(400,LARGEUR-400)
        self.y = random.randint(300,HAUTEUR-300)
        self.rect = self.image.get_rect(center=(self.x,self.y))


#######################################################
# Fonctions ###########################################

def load_game():
    global afficher_menu
    afficher_menu = True
    print("Et toc !")
    menu._open(loading)
    pygame.time.set_timer(update_loading,30)


#######################################################
# PYGAME INIT #########################################

pygame.init()
screen = pygame.display.set_mode((LARGEUR,HAUTEUR))
pygame.display.set_caption("Cyber's")


###############################################
# TESTs et PATHs ##############################

background_image = "tilesheet/background/nuit-etoile-mont-blanc.jpg"
perso1_image = "tilesheet/perso1/pepe1.png"
perso2_images = "tilesheet/perso2/"


########################################################################
# Chargement des variables #############################################

background = pygame.image.load(background_image).convert()
perso1 = Character(perso1_image,False,scale=5)
perso2 = Character(perso2_images,True,scale=5)


########################################################################
# Thème perso ##########################################################

mytheme = pygame_menu.Theme(widget_font=pygame_menu.font.FONT_BEBAS,
                            background_color=(255, 0, 0, 255),
                            title_background_color=(109, 7, 26),
                            title_font_shadow=True,
                            widget_padding=100)


########################################################################
# Menu main ############################################################

menu = pygame_menu.Menu("Cyber's", LARGEUR, HAUTEUR,theme=mytheme)
arrow = pygame_menu.widgets.LeftArrowSelection(arrow_size = (10,15),)
menu.add.text_input("Ton  CyberNom  est : ", default='')
menu.add.button('Play', load_game)
menu.add.button('Quit', pygame_menu.events.EXIT)


##################################################################################
# Menu de chargement #############################################################

loading = pygame_menu.Menu("Chargement en cours",LARGEUR,HAUTEUR,theme=mytheme)
loading.add.progress_bar("Cyber's Net",progressbar_id="1",width=300)
update_loading = pygame.USEREVENT + 0


##################################################################################
# Variables du Grand While #######################################################

game = True
afficher_menu = True
run = False
clock = pygame.time.Clock()


##################################################
# Mouvement ######################################

movex,movey = 0,0 #Variable delta


##################################################
# Le Grand While #################################

while game:
    events = pygame.event.get()
    if afficher_menu:
        for event in events:
            if event.type == pygame.QUIT:
                game = False
            if event.type == update_loading:
                progress = loading.get_widget("1")
                progress.set_value(progress.get_value()+random.randint(0,3))
                if progress.get_value() > 97:
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
                    pass
                    #run = False
                    #pause = True # On verra ça plus tard dans le developpement

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
        #################
        # Affiche Décor #
        screen.blit(background,(0,0))
        ########
        # Move #
        perso1.rect.left += movex
        perso1.rect.bottom += movey
        ######################
        # Affiche Characters #
        screen.blit(perso2.image,perso2.rect)
        screen.blit(perso1.image,perso1.rect)
    
    clock.tick(30) #Framerate 30 FPS
    pygame.display.update()

pygame.quit()
quit()