# Menu Sort the Box

import pygame, main, sys

pygame.init()

fenetre = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Sort the Box")
width, height = fenetre.get_size()

txt_font = pygame.font.Font(None ,30)

plaque_metal = pygame.image.load("images/plaque_metal.png")
plaque_metal = pygame.transform.scale(plaque_metal, (350, 191))
plaque_metal.convert()
width_img, height_img = plaque_metal.get_size()

color = (74, 71, 71)
color2 = (191, 186, 186)

titre_font = pygame.font.SysFont(None, 80)
titre = titre_font.render('Sort the Box', True, color) #(txt, gras, couleur)
width_titre, heigth_titre = titre.get_size()

texte_font = pygame.font.SysFont(None, 30)
texte_1 = texte_font.render('Jouer', True, color)
texte_2 = texte_font.render('Quitter', True, color)


def page_menu():
    fenetre.fill((219, 209, 209))
    fenetre.blit(titre, (width/2 - width_titre/2, height/4))
    fenetre.blit(plaque_metal, (width/2 - width_img/2, 280))

    bouton_jouer = pygame.draw.rect(fenetre,color2,[295,310,210,40]) #width, heigth, longueur, largeur
    fenetre.blit(texte_1, (370,320))

    bouton_quitter = pygame.draw.rect(fenetre,color2,[295,400,210,40])
    fenetre.blit(texte_2, (365,410))

    pygame.display.update()

    run_menu = True

    while run_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_menu = False
                pygame.quit() #ferme la fenêtre
                exit() #désactive la librairie Pygame

            elif event.type == pygame.MOUSEBUTTONUP:
                print("clic souris")
                if bouton_jouer.collidepoint(pygame.mouse.get_pos()):
                    print("clic jouer")
                    main.page_jeu()
                if bouton_quitter.collidepoint(pygame.mouse.get_pos()):
                    print("clic quitter")
                    pygame.quit() 
                    exit()  
page_menu()