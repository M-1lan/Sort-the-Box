import pygame, sys

#color2 = (181, 177, 177)
color = (0, 255, 0)

def bouton_pause(fenetre):
    execution = True
    while execution:

        bouton_depause = pygame.draw.rect(fenetre,color,[301,500,150,40])

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bouton_depause.collidepoint(pygame.mouse.get_pos()):
                    execution = False
        pygame.display.flip()