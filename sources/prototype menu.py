# Menu Petit Jardin
import pygame, main, sys

pygame.init()

fenetre = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Petit Jardin")

txt_font = pygame.font.Font(None ,30)

image_fond = pygame.image.load("images/prototype menu 3.jpg")
image_fond = pygame.transform.scale(image_fond, (800, 600))
image_fond.convert()

width = 600
height = 550

color = (141, 73, 14)
color2 = (209, 161, 121)

txt_font = pygame.font.SysFont(None,30)
texte = txt_font.render('Jouer', True , color)
texte2 = txt_font.render('Charger', True, color)
texte3 = txt_font.render('Quitter', True, color)


def page_jeu():
    run_jeu = True
    while run_jeu :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_jeu = False
                pygame.quit()
                sys.exit()

        fenetre.fill((255, 255, 255))
                   
        pygame.display.flip()

def page_chargement(): 
    run_jeu = True
    while run_jeu :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_jeu = False
                pygame.quit()
                sys.exit()

        fenetre.blit(image_fond, (0, 0))
                   
        pygame.display.flip()


def page_menu():
    run_menu = True
    while run_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_menu = False
                pygame.quit()
                sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if width/2 <= mouse[0] <= width/2+210 and height/2 <= mouse[1] <= height/2+40:
                main.page_jeu()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if width/2 <= mouse[0] <= width/2+210 and height/2+70 <= mouse[1] <= height/2+110:
                page_chargement()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if width/2 <= mouse[0] <= width/2+210 and height/2+140 <= mouse[1] <= height/2+180:
                pygame.quit()
                sys.exit()
                

        mouse = pygame.mouse.get_pos()

        fenetre.blit(image_fond, (0, 0))

        pygame.draw.rect(fenetre,color2,[width/2,height/2,210,40])
        fenetre.blit(texte, (width/2+80,height/2+10))

        pygame.draw.rect(fenetre,color2,[width/2,height/2+70,210,40])
        fenetre.blit(texte2, (width/2+70,height/2+80))

        pygame.draw.rect(fenetre,color2,[width/2,height/2+140,210,40])
        fenetre.blit(texte3, (width/2+75,height/2+150))

        pygame.display.update()

page_menu()