from pip import main
import pygame

from objets import Objet, ObjetVide, Interactable, Bloquant, NonBloquant, Lit
from grille import Grille, Case
from personnage import Personnage
       
pygame.init()
pygame.font.init()


## Création de la fenêtre de jeu 

fenetre = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Petit Jardin")


plateau = Grille(10, 10, fenetre)
martin = Personnage(0, 0, "Martin", plateau, fenetre)

plateau.change_case(0, 1, Interactable(0, 1, fenetre, "Meuble"))
plateau.change_case(1, 2, Bloquant(1, 1, fenetre))
plateau.change_case(1, 1, NonBloquant(1, 1, fenetre))
plateau.change_case(7, 8, Lit(7, 8, fenetre, martin))
pygame.display.update()


def liste_initiales():
    liste = []
    for line in plateau.plateau:
        d_line = []
        for column in line:
            d_line.append(str(column.get_upper_element())[1])

        liste.append(d_line)
    
    return liste


print(*liste_initiales(), sep="\n")

execution = True

while execution:
    plateau.tout_placer()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            execution = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                try:
                    martin.deplacer("O")
                    print(*liste_initiales(), sep="\n")

                except ValueError:
                    pass

            elif event.key == pygame.K_RIGHT:
                try:
                    martin.deplacer("E")
                    print(*liste_initiales(), sep="\n")
                except ValueError:
                    pass

            elif event.key == pygame.K_UP:
                try:
                    martin.deplacer("N")
                    print(*liste_initiales(), sep="\n")
                except ValueError:
                    pass

            elif event.key == pygame.K_DOWN:
                try:
                    martin.deplacer("S")
                    print(*liste_initiales(), sep="\n")
                except ValueError:
                    pass
            
            elif event.key == pygame.K_i:
                try:
                    martin.interagir()
                except ValueError as err:
                    print(err)
                
    fenetre.fill((255, 255, 255))
    myfont = pygame.font.SysFont("Arial", 20)
    
    # for i, el in enumerate(liste_initiales()):
    #     textsurface = myfont.render(str(el), False, (0, 0, 0))
    #     rect = textsurface.get_rect()

    #     rect.center = (400, 200+20*i)
    #     fenetre.blit(textsurface, rect)
    #     pygame.display.update(rect)
    pygame.display.update()
    
pygame.quit()