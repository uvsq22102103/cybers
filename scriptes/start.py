from main_aymeric import HAUTEUR, LARGEUR, background_image, perso1_image, screen, pygame

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
        screen.blit(perso1,perso1.get_rect(center=(x,y)))
        pygame.display.update()
        clock.tick(60)
