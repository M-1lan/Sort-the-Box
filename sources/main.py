def page_jeu():

    import pygame, page_de_fin
    from objets import Convoyeur, Bac, Spawner
    from grille import Grille
    from personnage import Personnage

    pygame.init()
    pygame.font.init()

    ## Création de la fenêtre de jeu 

    fenetre = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
    pygame.display.set_caption("Sort the Box")

    clock = pygame.time.Clock()

    plateau = Grille(16, 12, fenetre, 32)
    martin = Personnage(0, 0, "Martin", plateau, fenetre)

    tapis_roulants = pygame.sprite.Group()

    tapis_roulants.add(
        Convoyeur(11, 9, fenetre, plateau, "S", "N", ("N")),
        Convoyeur(11, 8, fenetre, plateau, "S", "O", ("O")),
        Convoyeur(10, 8, fenetre, plateau, "E", "O", ("O")),
        Convoyeur(9, 8, fenetre, plateau, "E", "O", ("O")),
        Convoyeur(8, 8, fenetre, plateau, "E", "O", ("O")),
        Convoyeur(7, 8, fenetre, plateau, "E", "O", ("O")),
        Convoyeur(6, 8, fenetre, plateau, "E", "O", ("O")),
        Convoyeur(5, 8, fenetre, plateau, "E", "O", ("O")),
        Convoyeur(4, 8, fenetre, plateau, "E", "O", ("O")),
        Convoyeur(3, 8, fenetre, plateau, "E", "N", ("O", "N")),
        Convoyeur(2, 8, fenetre, plateau, "E", "O", ("O")),
        Convoyeur(3, 7, fenetre, plateau, "S", "N", ("N")),
        Convoyeur(3, 6, fenetre, plateau, "S", "N", ("N")),
        Convoyeur(3, 5, fenetre, plateau, "S", "N", ("N")),
        Convoyeur(3, 4, fenetre, plateau, "S", "E", ("O", "E")),
        Convoyeur(2, 4, fenetre, plateau, "E", "N", ("N")),
        Convoyeur(2, 3, fenetre, plateau, "S", "N", ("N")),
        Convoyeur(2, 2, fenetre, plateau, "S", "N", ("N")),
        Convoyeur(4, 4, fenetre, plateau, "O", "E", ("E")),
        Convoyeur(5, 4, fenetre, plateau, "O", "N", ("N")),
        Convoyeur(5, 3, fenetre, plateau, "S", "E", ("E")),
        Convoyeur(6, 3, fenetre, plateau, "O", "E", ("E")),
        Convoyeur(7, 3, fenetre, plateau, "O", "E", ("E", "S")),
        Convoyeur(7, 4, fenetre, plateau, "N", "S", ("S")),
        Convoyeur(7, 5, fenetre, plateau, "N", "S", ("S")),
        Convoyeur(8, 3, fenetre, plateau, "O", "E", ("E")),
        Convoyeur(9, 3, fenetre, plateau, "O", "S", ("S")),
        Convoyeur(9, 4, fenetre, plateau, "N", "E", ("E")),
        Convoyeur(10, 4, fenetre, plateau, "O", "E", ("E")),
        Convoyeur(11, 4, fenetre, plateau, "O", "S", ("N", "S")),
        Convoyeur(11, 3, fenetre, plateau, "S", "N", ("N")),
        Convoyeur(11, 5, fenetre, plateau, "N", "S", ("S")),
        Convoyeur(11, 6, fenetre, plateau, "N", "E", ("E")),
        Convoyeur(12, 6, fenetre, plateau, "O", "E", ("E")),
        Convoyeur(13, 6, fenetre, plateau, "O", "S", ("S")),
        Convoyeur(13, 7, fenetre, plateau, "N", "S", ("S")),
        Convoyeur(13, 8, fenetre, plateau, "N", "E", ("E")),
        Spawner(11, 10, fenetre, plateau, "N")
    )

    bacs = pygame.sprite.Group()

    bacs.add(
        Bac(14, 8, fenetre, plateau, "rose", "O"),
        Bac(1, 8, fenetre, plateau, "orange", "E"),
        Bac(2, 1, fenetre, plateau, "bleu", "S"),
        Bac(7, 6, fenetre, plateau, "blanc", "N"),
        Bac(11, 2, fenetre, plateau, "vert", "S")
    )

    for tapis in tapis_roulants:
        plateau.change_case(tapis.pos_x, tapis.pos_y, tapis)

    for bac in bacs:
        plateau.change_case(bac.pos_x, bac.pos_y, bac)

    pygame.display.update()
    txt_font = pygame.font.SysFont(None,40)
    color = (63, 59, 169)

    carton = pygame.image.load("images/carton.png")

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
    compteur = 0
    while execution:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                execution = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    try:
                        martin.deplacer("O")
                        # print(*liste_initiales(), sep="\n")

                    except ValueError:
                        pass

                elif event.key == pygame.K_RIGHT:
                    try:
                        martin.deplacer("E")
                        # print(*liste_initiales(), sep="\n")

                    except ValueError:
                        pass

                elif event.key == pygame.K_UP:
                    try:
                        martin.deplacer("N")
                        # print(*liste_initiales(), sep="\n")

                    except ValueError:
                        pass

                elif event.key == pygame.K_DOWN:
                    try:
                        martin.deplacer("S")
                        # print(*liste_initiales(), sep="\n")
                        
                    except ValueError:
                        pass
                
                elif event.key == pygame.K_i:
                    try:
                        martin.interagir()
                    except ValueError as err:
                        print(err)
                    
        fenetre.fill((255, 255, 255))

        score = 0
        for bac in bacs:
            score += bac.score
        
        score = str(score)

        compteur = txt_font.render(score, True, color)
        pygame.draw.rect(fenetre, (181, 177, 177), (10, 10, 80, 40))
        fenetre.blit(pygame.transform.scale(carton, (30, 30)), (15, 15))
        fenetre.blit(compteur, (55, 20))
        plateau.tout_placer()

        pygame.display.flip()

        clock.tick(15)

        for tapis in tapis_roulants:
            tapis.animation()

        if int(score) >= 1:
            page_de_fin.page_de_fin()
    pygame.quit()
