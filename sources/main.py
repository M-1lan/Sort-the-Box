def page_jeu():

    import pygame

    from objets import Objet, ObjetVide, Interactable, Bloquant, NonBloquant, Lit
    from grille import Grille, Case
    from personnage import Personnage

    pygame.init()
    pygame.font.init()

    ## Création de la fenêtre de jeu 

    fenetre = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
    pygame.display.set_caption("Petit Jardin")

    plateau = Grille(10, 10, fenetre, 40)
    martin = Personnage(0, 0, "Martin", plateau, fenetre)

    plateau.change_case(0, 1, Interactable(0, 1, fenetre, "Meuble", plateau))
    plateau.change_case(1, 2, Bloquant(1, 2, fenetre, plateau))
    plateau.change_case(1, 1, NonBloquant(1, 1, fenetre, plateau))
    plateau.change_case(7, 8, Lit(7, 8, fenetre, martin, plateau))
    pygame.display.update()


    def liste_initiales():
        liste = []
        for line in plateau.plateau:
            temp_line = []
            for column in line:
                temp_case = []
                for content in column.content:
                    temp_case.append(str(content)[1])
                temp_line.append(temp_case)

            liste.append(temp_line)
        
        return liste


    print(*liste_initiales(), sep="\n")

    execution = True

    while execution:
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
                    
        # fenetre.fill((255, 255, 255))
        plateau.tout_placer()

        pygame.display.flip()
        
    pygame.quit()