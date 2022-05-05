# Fin Sort the Box
import pygame, main, sys

pygame.init()

fenetre = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Sort the Box")

width, height = fenetre.get_size()

carton = pygame.image.load("images/carton.png")

color = (74, 71, 71)
color2 = (191, 186, 186)
color3 = (63, 59, 169)

txt_font = pygame.font.SysFont(None,30)
texte = txt_font.render('Rejouer', True, color)

txt_font_2 = pygame.font.SysFont(None,80)
texte_2 = txt_font_2.render('Vous avez gagné !', True, color3) 
texte_3 = txt_font_2.render('20', True, color3) 


def page_fin():
    run_menu = True
    while run_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_menu = False
                pygame.quit()
                exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if width/3+35 <= mouse[0] <= width/2+210 and height/2+100 <= mouse[1] <= height/2+140:
                main.page_jeu()
                exit()
                
        mouse = pygame.mouse.get_pos()

        fenetre.fill((255, 255, 255))

        fenetre.blit(texte_2, (170,150))
        fenetre.blit(pygame.transform.scale(carton, (100, 100)), (320, 240))
        fenetre.blit(texte_3, (440,270))

        pygame.draw.rect(fenetre,color2,[width/3+35,height/2+100,210,40])
        fenetre.blit(texte, (width/3+110,height/2+110))

        pygame.display.update()

page_fin()