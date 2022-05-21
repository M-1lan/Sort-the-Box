# Menu Sort the Box

import pygame, main, sys

pygame.init()

fenetre = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Sort the Box")

txt_font = pygame.font.Font(None ,30)

image_fond = pygame.image.load("images/bg menu.png")
image_fond = pygame.transform.scale(image_fond, (800, 600))
image_fond.convert()

width, height = fenetre.get_size()

color = (74, 71, 71)
color2 = (191, 186, 186)

txt_font = pygame.font.SysFont(None,30)
texte = txt_font.render('Jouer', True, color)
texte3 = txt_font.render('Quitter', True, color)


def page_menu():
    fenetre.blit(image_fond, (0, 0))

    bouton_jouer = pygame.draw.rect(fenetre,color2,[301,310,210,40]) #width, heigth, longueur, largeur
    fenetre.blit(texte, (379,320))

    bouton_quitter = pygame.draw.rect(fenetre,color2,[301,400,210,40])
    fenetre.blit(texte3, (376,410))

    pygame.display.update()

    run_menu = True

    while run_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_menu = False
                pygame.quit() #ferme la fenêtre
                exit() #désactive la librairie Pygame

            elif event.type == pygame.MOUSEBUTTONUP:
                if bouton_jouer.collidepoint(pygame.mouse.get_pos()):
                    main.page_jeu()
                if bouton_quitter.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit() 
                    exit()  
page_menu()