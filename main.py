import pygame

background_image = "tilesheet/background/nuit-etoile-mont-blanc.jpg"
HAUTEUR, LARGEUR = 1920, 1080

pygame.init()
screen = pygame.display.set_mode((HAUTEUR,LARGEUR))
pygame.display.set_caption("Cyber's")

background = pygame.image.load(background_image).convert()
run = True

taille,x,y = 10,LARGEUR//2,HAUTEUR//2 #Variable statique
movex,movey,agrandir = 0,0,0 #Variable delta

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.KEYDOWN: # If clée pressée
            if event.key == pygame.K_SPACE:
                agrandir = 1
            elif event.key == pygame.K_UP:
                movey = -2
            elif event.key == pygame.K_DOWN:
                movey = 2
            elif event.key == pygame.K_RIGHT:
                movex = 2
            elif event.key == pygame.K_LEFT:
                movex = -2


        elif event.type == pygame.KEYUP: # If clée relâchée
            if event.key == pygame.K_SPACE:
                agrandir = 0
            elif event.key == pygame.K_UP:
                movey = 0
            elif event.key == pygame.K_DOWN:
                movey = 0
            elif event.key == pygame.K_RIGHT:
                movex = 0
            elif event.key == pygame.K_LEFT:
                movex = 0cercle.move(x,y)
    
    x += movex
    y += movey
    taille += agrandir
    screen.blit(background,(0,0))
    cercle = pygame.draw.circle(background, (90, 50, 250), (x, y), taille)
    pygame.display.update()

pygame.quit()
quit()