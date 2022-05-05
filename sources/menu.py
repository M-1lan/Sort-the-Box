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
texte = txt_font.render('Jouer', True , color)
texte3 = txt_font.render('Quitter', True, color)


def page_menu():
    run_menu = True
    while run_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_menu = False
                pygame.quit()
                exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if width/3+35 <= mouse[0] <= width/3+245 and height/2+10 <= mouse[1] <= height/2+50:
                main.page_jeu()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if width/3+35 <= mouse[0] <= width/2+210 and height/2+100 <= mouse[1] <= height/2+140:
                pygame.quit()
                exit()
                
        mouse = pygame.mouse.get_pos()

        fenetre.blit(image_fond, (0, 0))

        pygame.draw.rect(fenetre,color2,[width/3+35,height/2+10,210,40])
        fenetre.blit(texte, (width/3+113,height/2+20))

        pygame.draw.rect(fenetre,color2,[width/3+35,height/2+100,210,40])
        fenetre.blit(texte3, (width/3+110,height/2+110))

        pygame.display.update()

page_menu()

