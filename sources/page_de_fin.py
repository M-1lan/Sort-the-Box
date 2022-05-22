# Fin Sort the Box
import pygame, main, sys

fenetre = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Sort the Box")
width, height = fenetre.get_size()

carton = pygame.image.load("images/carton.png")

color = (74, 71, 71)
color2 = (191, 186, 186)

titre_font = pygame.font.SysFont(None, 80)
titre = titre_font.render('Vous avez gagné !', True, color)
width_titre, heigth_titre = titre.get_size()

txt_font = pygame.font.SysFont(None, 30)
txt_btn = txt_font.render('Rejouer', True, color)
txt_score = titre_font.render('10', True, color) 


def page_de_fin():

    fenetre.fill((255, 255, 255))

    btn_rejouer = pygame.draw.rect(fenetre,color2,[295,400,210,40])
    fenetre.blit(txt_btn, (365,410))

    fenetre.blit(titre, (width/2 - width_titre/2, height/4))
    fenetre.blit(pygame.transform.scale(carton, (100, 100)), (320, 240))
    fenetre.blit(txt_score, (440,270))

    pygame.display.update()

    run_menu = True
    while run_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_menu = False
                pygame.quit()
                exit()
        if event.type == pygame.MOUSEBUTTONUP:
            if btn_rejouer.collidepoint(pygame.mouse.get_pos()):
                main.page_jeu()
                exit()
